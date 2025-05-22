from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType


class Input(AntdComponent):
    tag = "Input"

    addon_after: Var[ReactNode]
    addon_before: Var[ReactNode]
    allow_clear: Var[Union[bool, ContainVar]]
    count: Var[Union[Dict, ContainVar]]
    default_value: Var[str]
    disabled: Var[bool]
    max_length: Var[int]
    prefix: Var[ReactNode]
    show_count: Var[Union[bool, JsValue]]
    status: Var[StatusType]
    size: Var[SizeType]
    suffix: Var[ReactNode]
    type: Var[str]
    value: Var[str]
    variant: Var[VariantType]
    placeholder: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
            'on_press_enter': lambda e: [e],
        })
        return _triggers


class TextArea(Input):
    tag = "Input.TextArea"

    auto_size: Var[Union[bool, Dict, ContainVar]]


class Search(Input):
    tag = 'Input.Search'

    enter_button: Var[ReactNode]
    loading: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_search': lambda value, event, info: [value],
        })
        return _triggers


class Password(Input):
    tag = 'Input.Password'

    icon_render: Var[JsValue]
    visibility_toggle: Var[Union[bool, ContainVar]]


input = Input.create  # noqa
text_area = TextArea.create
search = Search.create
password = Password.create



