from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import VariantType, SizeType


class AutoComplete(AntdComponent):
    tag = "AutoComplete"

    allow_clear: Var[bool]
    auto_focus: Var[bool]
    backfill: Var[bool]
    default_active_first_option: Var[bool]
    default_open: Var[bool]
    default_value: Var[str]
    disabled: Var[bool]
    popup_class_name: Var[str]
    dropdown_match_select_width: Var[Union[bool, int]]
    filter_option: Var[bool]
    not_found_content: Var[ReactNode]
    open: Var[bool]
    options: Var[list]
    placeholder: Var[str]
    status: Var[str]
    size: Var[SizeType]
    value: Var[str]
    variant: Var[VariantType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_BLUR: lambda: [],
            "on_dropdown_visible_change": lambda open: [open],
            EventTriggers.ON_FOCUS: lambda: [],
            "on_search": lambda value: [value],
            EventTriggers.ON_SELECT: lambda value, option: [value, option],
            "on_clear": lambda: [],
        })
        return _triggers


auto_complete = AutoComplete.create
