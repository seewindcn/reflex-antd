from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import VariantType, SizeType


class AutoComplete(AntdComponent):
    tag = "AutoComplete"

    allow_clear: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    backfill: Optional[Var[bool]]
    children: Optional[Var[Union[Component, ContainVar]]]
    default_active_first_option: Optional[Var[bool]]
    default_open: Optional[Var[bool]]
    default_value: Optional[Var[str]]
    disabled: Optional[Var[bool]]
    popup_class_name: Optional[Var[str]]
    dropdown_match_select_width: Optional[Var[Union[bool, int]]]
    filter_option: Optional[Var[bool]]
    not_found_content: Optional[Var[Component]]
    open: Optional[Var[bool]]
    options: Optional[Var[ContainVar]]
    placeholder: Optional[Var[str]]
    status: Optional[Var[str]]
    size: Optional[Var[SizeType]]
    value: Optional[Var[str]]
    variant: Optional[Var[VariantType]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_BLUR: lambda: [],
            EventTriggers.ON_CLOSE: lambda value: [value],
            "on_dropdown_visible_change": lambda open: [open],
            EventTriggers.ON_FOCUS: lambda: [],
            "on_search": lambda value: [value],
            EventTriggers.ON_SELECT: lambda value, option: [value, option],
            "on_clear": lambda: [],
        })
        return _triggers

