from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, RadioStyleType, RadioType


class Radio(AntdComponent):
    tag = 'Radio'

    auto_focus: Var[bool]
    checked: Var[bool]
    default_checked: Var[bool]
    disabled: Var[bool]
    value: Var[Any]


class RadioButton(Radio):
    tag = 'Radio.Button'


class RadioGroup(AntdComponent):
    tag = 'Radio.Group'

    button_style: Var[RadioStyleType]
    default_value: Var[Any]
    disabled: Var[bool]
    name: Var[str]
    options: Var[Union[List[Union[str, int]], ContainVar]]
    option_type: Var[RadioType]
    size: Var[SizeType]
    value: Var[Any]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
        })
        return _triggers


radio = Radio.create
radio_button = RadioButton.create
radio_group = RadioGroup.create

