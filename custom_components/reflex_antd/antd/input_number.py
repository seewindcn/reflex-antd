from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType


class InputNumber(AntdComponent):
    tag = "InputNumber"

    addon_after: Optional[Var[ReactNode]]
    addon_before: Optional[Var[ReactNode]]
    auto_focus: Optional[Var[bool]]
    change_on_blur: Optional[Var[bool]]
    change_on_wheel: Optional[Var[bool]]
    controls: Optional[Var[Union[bool, ContainVar]]]
    decimal_separator: Optional[Var[str]]
    placeholder: Optional[Var[str]]
    default_value: Optional[Var[int]]
    disabled: Optional[Var[bool]]
    formatter: Optional[Var[JsValue]]
    keyboard: Optional[Var[bool]]
    max: Optional[Var[int]]
    min: Optional[Var[int]]
    parser: Optional[Var[JsValue]]
    precision: Optional[Var[int]]
    read_only: Optional[Var[bool]]
    status: Optional[Var[StatusType]]
    prefix: Optional[Var[ReactNode]]
    size: Optional[Var[SizeType]]
    step: Optional[Var[Union[int, str]]]
    string_mode: Optional[Var[bool]]
    value: Optional[Var[int]]
    variant: Optional[Var[VariantType]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value: [value],
            'on_press_enter': lambda e: [e],
            "on_step": lambda value, info: [value, info],
        })
        return _triggers


input_number = InputNumber.create
