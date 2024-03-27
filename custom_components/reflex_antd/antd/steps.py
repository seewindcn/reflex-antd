from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import PlacementType, DirectionType, SizeType, StepsStatusType, StepsType


class Steps(AntdComponent):
    tag = 'Steps'

    current: Optional[Var[int]]
    direction: Optional[Var[DirectionType]]
    initial: Optional[Var[int]]
    label_placement: Optional[Var[DirectionType]]
    percent: Optional[Var[int]]
    progress_dot: Optional[Var[Union[bool, JsValue]]]
    responsive: Optional[Var[bool]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[StepsStatusType]]
    type: Optional[Var[StepsType]]

    items: Optional[Var[ContainVar]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda current: [current],
        })
        return _triggers


steps = Steps.create


