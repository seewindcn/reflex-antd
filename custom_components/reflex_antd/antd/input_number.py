from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType


class InputNumber(AntdComponent):
    tag = "InputNumber"

    addon_after: Var[ReactNode]
    addon_before: Var[ReactNode]
    auto_focus: Var[bool]
    change_on_blur: Var[bool]
    change_on_wheel: Var[bool]
    controls: Var[Union[bool, ContainVar]]
    decimal_separator: Var[str]
    placeholder: Var[str]
    default_value: Var[int]
    disabled: Var[bool]
    formatter: Var[JsValue]
    keyboard: Var[bool]
    max: Var[int]
    min: Var[int]
    parser: Var[JsValue]
    precision: Var[int]
    read_only: Var[bool]
    status: Var[StatusType]
    prefix: Var[ReactNode]
    size: Var[SizeType]
    step: Var[Union[int, str]]
    string_mode: Var[bool]
    value: Var[int]
    variant: Var[VariantType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value: [value],
            'on_press_enter': lambda e: [e],
            "on_step": lambda value, info: [value, info],
        })
        return _triggers


input_number = InputNumber.create
