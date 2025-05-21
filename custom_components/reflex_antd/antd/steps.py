from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import PlacementType, DirectionType, SizeType, StepsStatusType, StepsType


class Steps(AntdComponent):
    tag = 'Steps'

    current: Var[int]
    direction: Var[DirectionType]
    initial: Var[int]
    label_placement: Var[DirectionType]
    percent: Var[int]
    progress_dot: Var[Union[bool, JsValue]]
    responsive: Var[bool]
    size: Var[SizeType]
    status: Var[StepsStatusType]
    type: Var[StepsType]

    items: Var[ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda current: [current],
        })
        return _triggers


steps = Steps.create


