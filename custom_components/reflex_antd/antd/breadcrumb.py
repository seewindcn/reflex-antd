from typing import Optional, Union, Dict, Any
from reflex import Var, Component

from ..base import AntdComponent, ContainVar, ReactNode


class Breadcrumb(AntdComponent):
    tag = "Breadcrumb"

    params: Optional[Var[dict]]
    items: Optional[Var[Union[ContainVar, list, Component]]]
    separator: Optional[Var[ReactNode]]


class RouteItemType(AntdComponent):
    tag = "RouteItemType"

    class_name: Optional[Var[str]]
    href: Optional[Var[str]]
    path: Optional[Var[str]]
    title: Optional[Var[ReactNode]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_click': lambda e: [e],
        })
        return _triggers


breadcrumb = Breadcrumb.create
