from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import PlacementType, RoleType


class Notification(AntdComponent):
    tag = 'Notification'

    btn: Optional[Var[ReactNode]]
    class_name: Optional[Var[str]]
    close_icon: Optional[Var[ReactNode]]
    description: Optional[Var[ReactNode]]
    duration: Optional[Var[int]]
    icon: Optional[Var[ReactNode]]
    key: Optional[Var[str]]
    message: Optional[Var[ReactNode]]
    placement: Optional[Var[PlacementType]]
    role: Optional[Var[RoleType]]
    props: Optional[Var[Union[dict, ContainVar]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_click": lambda: [],
            "on_close": lambda: [],
        })
        return _triggers


notification = Notification.create
