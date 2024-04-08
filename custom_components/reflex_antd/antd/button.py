from typing import Optional, Union, Dict, Any

from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import TypeType, ButtonShape, SizeType


class Button(AntdComponent):
    tag = "Button"

    block: Optional[Var[bool]]
    danger: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    ghost: Optional[Var[bool]]
    href: Optional[Var[str]]
    target: Optional[Var[str]]
    html_type: Optional[Var[str]]
    icon: Optional[Var[ReactNode]]
    loading: Optional[Var[bool]]
    shape: Optional[Var[ButtonShape]]
    size: Optional[Var[SizeType]]
    type: Optional[Var[TypeType]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CLICK: lambda: [],
        })
        return _triggers


button = Button.create
