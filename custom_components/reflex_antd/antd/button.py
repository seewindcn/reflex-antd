from typing import Optional, Union, Dict, Any

from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import TypeType, ButtonShape, SizeType


class Button(AntdComponent):
    tag = "Button"

    block: Var[bool]
    danger: Var[bool]
    disabled: Var[bool]
    ghost: Var[bool]
    href: Var[str]
    target: Var[str]
    html_type: Var[str]
    icon: Var[ReactNode]
    icon_position: Var[str]
    loading: Var[bool]
    shape: Var[ButtonShape]
    size: Var[SizeType]
    type: Var[TypeType]
    variant: Var[str]
    color: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


button = Button.create
