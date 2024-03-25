from typing import Optional, Union, Dict, Any
from reflex import Var
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar
from ..constant import ButtonType, FloatGroupTriggerType, FloatGroupShapeType

from .icon import IconComponent
from .badge import Badge


class FloatButton(AntdComponent):
    tag = "FloatButton"

    icon: Optional[Var[IconComponent]]
    tooltip: Optional[Var[Union[ContainVar]]]
    type: Optional[Var[ButtonType]]
    shape: Optional[Var[FloatGroupShapeType]]
    href: Optional[Var[str]]
    target: Optional[Var[str]]
    badge: Optional[Var[Union[Dict]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


class FloatGroup(FloatButton):
    tag = "FloatButton.Group"

    open: Optional[Var[bool]]
    trigger: Optional[Var[FloatGroupTriggerType]]

    close_icon: Optional[Var[IconComponent]]


float_button = FloatButton.create
float_group = FloatGroup.create
