from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType


class Input(AntdComponent):
    tag = "Input"

    addon_after: Optional[Var[ReactNode]]
    addon_before: Optional[Var[ReactNode]]
    allow_clear: Optional[Var[Union[bool, ContainVar]]]
    count: Optional[Var[Union[Dict, ContainVar]]]
    default_value: Optional[Var[str]]
    disabled: Optional[Var[bool]]
    id: Optional[Var[str]]
    max_length: Optional[Var[int]]
    prefix: Optional[Var[ReactNode]]
    show_count: Optional[Var[Union[bool, JsValue]]]
    status: Optional[Var[StatusType]]
    size: Optional[Var[SizeType]]
    suffix: Optional[Var[ReactNode]]
    type: Optional[Var[str]]
    value: Optional[Var[str]]
    variant: Optional[Var[VariantType]]
    placeholder: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
            'on_press_enter': lambda e: [e],
        })
        return _triggers


class TextArea(Input):
    tag = "Input.TextArea"

    auto_size: Optional[Var[Union[bool, Dict, ContainVar]]]


class Search(Input):
    tag = 'Input.Search'

    enter_button: Optional[Var[ReactNode]]
    loading: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_search': lambda value, event, info: [value],
        })
        return _triggers


class Password(Input):
    tag = 'Input.Password'

    icon_render: Optional[Var[JsValue]]
    visibility_toggle: Optional[Var[Union[bool, ContainVar]]]


input = Input.create  # noqa
text_area = TextArea.create
search = Search.create
password = Password.create



