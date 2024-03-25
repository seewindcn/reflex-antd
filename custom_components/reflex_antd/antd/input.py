from typing import Optional, Union, Dict, Any
from reflex import Var
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar
from ..constant import StatusType, SizeType

from .icon import IconComponent


class Input(AntdComponent):
    tag = "Input"

    allow_clear: Optional[Var[bool]]
    count: Optional[Var[Dict]]
    default_value: Optional[Var[str]]
    disabled: Optional[Var[bool]]
    max_length: Optional[Var[int]]
    placeholder: Optional[Var[str]]
    prefix: Optional[Var[IconComponent]]
    show_count: Optional[Var[bool]]
    status: Optional[Var[StatusType]]
    size: Optional[Var[SizeType]]
    suffix: Optional[Var[IconComponent]]
    value: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
            'on_press_enter': lambda e: [e],
        })
        return _triggers


class TextArea(Input):
    tag = "Input.TextArea"

    auto_size: Optional[Var[bool]]


class Search(Input):
    tag = 'Input.Search'

    enter_button: Optional[Var[IconComponent]]
    loading: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            'onSearch': lambda value, event: [value, event],
        })
        return _triggers


class Password(Input):
    tag = 'Input.Password'

    visibility_toggle: Optional[Var[bool]]


input = Input.create  # noqa
text_area = TextArea.create
search = Search.create
password = Password.create



