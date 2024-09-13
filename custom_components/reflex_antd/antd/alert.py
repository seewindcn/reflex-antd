from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType


class Alert(AntdComponent):
    tag = 'Alert'

    action: Optional[Var[ReactNode]]
    banner: Optional[Var[bool]]
    closable: Optional[Var[Union[bool, dict]]]
    description: Optional[Var[ReactNode]]
    icon: Optional[Var[ReactNode]]
    message: Optional[Var[ReactNode]]
    show_icon: Optional[bool]
    type: Optional[StatusType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_close": lambda event: [],
            "after_close": lambda: [],
        })
        return _triggers


class AlertErrorBoundary(AntdComponent):
    tag = 'Alert.ErrorBoundary'

    description: Optional[ReactNode]
    message: Optional[ReactNode]


alert = Alert.create
alert_error_boundary = AlertErrorBoundary.create
