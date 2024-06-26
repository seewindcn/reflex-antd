from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType


class Slider(AntdComponent):
    tag = 'Slider'

    auto_adjust_overflow: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    default_value: Optional[Var[Union[int, List[int]]]]
    disabled: Optional[Var[bool]]
    keyboard: Optional[Var[bool]]
    dots: Optional[Var[bool]]
    included: Optional[Var[bool]]
    marks: Optional[Var[Union[Dict, ContainVar]]]
    max: Optional[Var[int]]
    min: Optional[Var[int]]
    range: Optional[Var[bool]]
    reverse: Optional[Var[bool]]
    step: Optional[Var[int]]
    tooltip: Optional[Var[Union[ReactNode, Dict, ContainVar]]]
    value: Optional[Var[Union[int, List[int]]]]
    vertical: Optional[Var[bool]]
    # range
    draggable_track: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_change_complete": lambda v: [v],
            EventTriggers.ON_CHANGE: lambda v: [v],
        })
        return _triggers


slider = Slider.create


