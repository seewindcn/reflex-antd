from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, RadioStyleType, RadioType


class Rate(AntdComponent):
    tag = 'Rate'

    allow_clear: Var[bool]
    allow_half: Var[bool]
    auto_focus: Var[bool]
    character: Var[Union[Component, JsValue]]
    count: Var[int]
    default_value: Var[int]
    disabled: Var[bool]
    tooltips: Var[List[str]]
    value: Var[int]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda v: [v],
            "on_hover_change": lambda v: [v],
            EventTriggers.ON_KEY_DOWN: lambda e: [e],
        })
        return _triggers


rate = Rate.create

