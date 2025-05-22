from typing import Optional, Union, Dict, Any
from reflex import Var, Component

from ..base import AntdComponent, ContainVar, ReactNode, ExTypes


class Breadcrumb(AntdComponent):
    tag = "Breadcrumb"

    params: Var[dict]
    items: Var[ExTypes | list | Component]
    separator: Var[ReactNode]


class RouteItemType(AntdComponent):
    tag = "RouteItemType"

    href: Var[str]
    path: Var[str]
    title: Var[ReactNode]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_click': lambda e: [e],
        })
        return _triggers


breadcrumb = Breadcrumb.create
