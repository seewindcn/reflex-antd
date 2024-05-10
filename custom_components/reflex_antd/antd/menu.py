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

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        def _on_select(ev: OnSelectEvent):
            return [ev.selectedKeys]

        def _on_click(ev: OnSelectEvent):
            return [ev.key, ev.keyPath]

        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open_keys: [open_keys],
            EventTriggers.ON_SELECT: _on_select,
            EventTriggers.ON_CLICK: _on_click,
            'on_deselect': _on_click,
        })
        return _triggers


menu = Menu.create
# menu_items = ContainVar.create
