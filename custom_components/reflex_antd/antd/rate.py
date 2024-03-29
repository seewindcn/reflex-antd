from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, RadioStyleType, RadioType


class Rate(AntdComponent):
    tag = 'Rate'

    allow_clear: Optional[Var[bool]]
    allow_half: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    character: Optional[Var[Union[Component, JsValue]]]
    count: Optional[Var[int]]
    default_value: Optional[Var[int]]
    disabled: Optional[Var[bool]]
    tooltips: Optional[Var[List[str]]]
    value: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda v: [v],
            "on_hover_change": lambda v: [v],
            EventTriggers.ON_KEY_DOWN: lambda e: [e],
        })
        return _triggers


rate = Rate.create

