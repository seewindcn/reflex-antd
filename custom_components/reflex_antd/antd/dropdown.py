from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, memo_never_no_recursive
from ..constant import PlacementType, DirectionType


class Dropdown(AntdComponent):
    tag = 'Dropdown'

    arrow: Optional[Var[bool]]
    auto_adjust_overflow: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    destroy_popup_on_hide: Optional[Var[bool]]
    dropdown_render: Optional[Var[JsValue]]
    menu: Optional[Var[Union[ContainVar, list]]]
    placement: Optional[Var[PlacementType]]
    trigger: Optional[Var[ContainVar]]
    open: Optional[Var[bool]]

    _memoization_mode = memo_never_no_recursive

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        # add menu events
        from . import menu
        menu.Menu.get_menu_triggers(_triggers, prepare='menu.')
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open, info: [open, info],
        })
        return _triggers


class DropdownButton(Dropdown):
    tag = 'Dropdown.Button'

    buttons_render: Optional[Var[JsValue]]
    loading: Optional[Var[bool]]
    danger: Optional[Var[bool]]
    icon: Optional[Var[ReactNode]]
    size: Optional[Var[str]]
    type: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


dropdown = Dropdown.create
dropdown_button = DropdownButton.create
