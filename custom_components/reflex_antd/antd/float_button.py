from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode, JsValue
from ..constant import TypeType, TriggerType, FloatGroupShapeType

from .badge import Badge


class FloatButton(AntdComponent):
    tag = "FloatButton"

    icon: Optional[Var[ReactNode]]
    description: Optional[Var[ReactNode]]
    tooltip: Optional[Var[Union[ReactNode, JsValue]]]
    type: Optional[Var[TypeType]]
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
    trigger: Optional[Var[TriggerType]]
    close_icon: Optional[Var[ReactNode]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
        })
        return _triggers


class FloatBackTop(FloatButton):
    tag = "FloatButton.BackTop"

    duration: Optional[Var[int]]
    target: Optional[Var[Union[ReactNode, JsValue]]]
    visibility_height: Optional[Var[int]]


float_button = FloatButton.create
float_group = FloatGroup.create
float_back_top = FloatBackTop.create
