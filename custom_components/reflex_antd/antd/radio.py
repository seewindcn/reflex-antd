from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, RadioStyleType, RadioType


class Radio(AntdComponent):
    tag = 'Radio'

    auto_focus: Optional[Var[bool]]
    checked: Optional[Var[bool]]
    default_checked: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    value: Optional[Var[Any]]


class RadioButton(Radio):
    tag = 'Radio.Button'


class RadioGroup(AntdComponent):
    tag = 'Radio.Group'

    button_style: Optional[Var[RadioStyleType]]
    default_value: Optional[Var[Any]]
    disabled: Optional[Var[bool]]
    name: Optional[Var[str]]
    options: Optional[Var[Union[List[Union[str, int]], ContainVar]]]
    option_type: Optional[Var[RadioType]]
    size: Optional[Var[SizeType]]
    value: Optional[Var[Any]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
        })
        return _triggers


radio = Radio.create
radio_button = RadioButton.create
radio_group = RadioGroup.create

