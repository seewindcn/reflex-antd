from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import ContainVar, JsValue, ReactNode, ExTypes
from .base import AntdProBaseComponent


class ProCard(AntdProBaseComponent):
    tag = 'ProCard'

    title: Var[ReactNode]
    sub_title: Var[ReactNode]
    tooltip: Var[str]
    head_style: Var[dict | ContainVar]
    body_style: Var[dict | ContainVar]
    box_shadow: Var[bool]
    extra: Var[ReactNode]
    layout: Var[str]
    loading: Var[bool | ReactNode]
    col_span: Var[int | str]
    gutter: Var[int | list | dict]
    split: Var[str]  # horizontal | vertical
    type: Var[str]
    size: Var[str]
    actions: Var[ReactNode | ExTypes]
    direction: Var[str]
    wrap: Var[bool]
    bordered: Var[bool]
    ghost: Var[bool]
    header_bordered: Var[bool]
    collapsed: Var[bool]
    collapsible: Var[bool]
    collapsible_icon_render: Var[ExTypes]
    default_collapsed: Var[bool]
    tabs: Var[ExTypes | ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_collapse': lambda collapsed: [collapsed],
        })
        return _triggers


pro_card = ProCard.create


