from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, memo_never_no_recursive
from ..constant import PlacementType, DirectionType


class Dropdown(AntdComponent):
    tag = 'Dropdown'

    arrow: Var[bool]
    auto_adjust_overflow: Var[bool]
    auto_focus: Var[bool]
    disabled: Var[bool]
    destroy_popup_on_hide: Var[bool]
    dropdown_render: Var[JsValue]
    menu: Var[Union[ContainVar, list]]
    placement: Var[PlacementType]
    trigger: Var[ContainVar]
    open: Var[bool]

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

    buttons_render: Var[JsValue]
    loading: Var[bool]
    danger: Var[bool]
    icon: Var[ReactNode]
    size: Var[str]
    type: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


dropdown = Dropdown.create
dropdown_button = DropdownButton.create
