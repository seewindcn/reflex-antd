from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType


class Slider(AntdComponent):
    tag = 'Slider'

    auto_adjust_overflow: Var[bool]
    auto_focus: Var[bool]
    default_value: Var[Union[int, List[int]]]
    disabled: Var[bool]
    keyboard: Var[bool]
    dots: Var[bool]
    included: Var[bool]
    marks: Var[Union[Dict, ContainVar]]
    max: Var[int]
    min: Var[int]
    range: Var[bool]
    reverse: Var[bool]
    step: Var[int]
    tooltip: Var[Union[ReactNode, Dict, ContainVar]]
    value: Var[Union[int, List[int]]]
    vertical: Var[bool]
    # range
    draggable_track: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_change_complete": lambda v: [v],
            EventTriggers.ON_CHANGE: lambda v: [v],
        })
        return _triggers


slider = Slider.create


