from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode, JsValue
from ..constant import TypeType, TriggerType, FloatGroupShapeType

from .badge import Badge


class FloatButton(AntdComponent):
    tag = "FloatButton"

    icon: Var[ReactNode]
    description: Var[ReactNode]
    tooltip: Var[Union[ReactNode, JsValue]]
    type: Var[TypeType]
    shape: Var[FloatGroupShapeType]
    href: Var[str]
    target: Var[str]
    badge: Var[Union[Dict]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


class FloatGroup(FloatButton):
    tag = "FloatButton.Group"

    open: Var[bool]
    trigger: Var[TriggerType]
    close_icon: Var[ReactNode]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
        })
        return _triggers


class FloatBackTop(FloatButton):
    tag = "FloatButton.BackTop"

    duration: Var[int]
    target: Var[Union[ReactNode, JsValue]]
    visibility_height: Var[int]


float_button = FloatButton.create
float_group = FloatGroup.create
float_back_top = FloatBackTop.create
