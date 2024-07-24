from typing import Optional, Union, Type, Dict, List, Any, Iterator
from reflex import Component, Var, EventChain, Base
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode, pydantic
from ..constant import ThemeType, DirectionType, TriggerType


class MenuItem(pydantic.BaseModel):
    key: str
    label: str
    icon: Component
    children: Optional[List["MenuItem"]] = None


# class MenuItems(ContainVar):
#     pass

class OnSelectEvent(Base):
    item: Any
    key: Any
    keyPath: Any
    selectedKeys: List[str]


def on_menu_select(ev: OnSelectEvent):
    return [ev.selectedKeys]


def on_menu_click(ev: OnSelectEvent):
    return [ev.key, ev.keyPath]


class Menu(AntdComponent):
    tag = 'Menu'

    default_open_keys: Optional[Var[List[str]]]
    default_selected_keys: Optional[Var[List[str]]]
    expand_icon: Optional[Var[ReactNode]]
    force_sub_menu_render: Optional[Var[bool]]
    inline_collapsed: Optional[Var[bool]]
    inline_indent: Optional[Var[bool]]

    items: Var[Union[ContainVar, list]]
    mode: Optional[Var[DirectionType]]
    multiple: Optional[Var[bool]]
    open_keys: Optional[Var[List[str]]]
    overflowed_indicator: Optional[Var[ReactNode]]
    selectable: Optional[Var[bool]]
    selected_keys: Optional[Var[List[str]]]
    sub_menu_close_delay: Optional[Var[float]]
    sub_menu_open_delay: Optional[Var[float]]

    theme: Optional[Var[ThemeType]]
    trigger_sub_menu_action: Optional[Var[TriggerType]]

    @classmethod
    def get_menu_triggers(cls, triggers: dict, prepare: str = ''):
        triggers.update({
            f'{prepare}{EventTriggers.ON_OPEN_CHANGE}': lambda open_keys: [open_keys],
            f'{prepare}{EventTriggers.ON_SELECT}': on_menu_select,
            f'{prepare}{EventTriggers.ON_CLICK}': on_menu_click,
            f'{prepare}on_deselect': on_menu_click,
        })

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        self.get_menu_triggers(_triggers)
        return _triggers


menu = Menu.create
# menu_items = ContainVar.create
