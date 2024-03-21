from typing import Optional, Union, Type, Dict, List, Any, Iterator
from pydantic import BaseModel
from reflex import Component, Var, EventChain, Base
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, AntdSubComponent, ContainVar
from ..constant import ThemeType, MenuModeType


class MenuItem(BaseModel):
    key: str
    label: str
    icon: Component
    children: Optional[List["MenuItem"]] = None


# class MenuItems(ContainVar):
#     pass

class OnSelectEvent(Base):
    selectedKeys: List[str]


class Menu(AntdComponent):
    tag = 'Menu'

    theme: Optional[Var[ThemeType]]
    mode: Optional[Var[MenuModeType]]
    selected_keys: Optional[Var[List[str]]]

    items: Var[Union[ContainVar, list]]  # Var[Union[MenuItems, List[MenuItem], List[dict]]]

    open_keys: Optional[Var[List[str]]]
    selected_keys: Optional[Var[List[str]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        def _onSelect(ev: OnSelectEvent):
            return [ev.selectedKeys]

        _triggers.update({
            'onOpenChange': lambda open_keys: [open_keys],
            'onSelect': _onSelect,
            # EventTriggers.ON_CHANGE: lambda e0: [e0.target.checked],
        })
        return _triggers


menu = Menu.create
# menu_items = ContainVar.create
