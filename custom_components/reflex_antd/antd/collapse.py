from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Collapse(AntdComponent):
    tag = 'Collapse'

    accordion: Var[bool]
    active_key: Var[Union[list[str], str, list[int], int]]
    bordered: Var[bool]
    default_active_key: Var[Union[list[str], str, list[int], int]]
    destroy_inactive_panel: Var[bool]
    expand_icon: Var[ReactNode]
    collapsible: Var[str]
    expand_icon_position: Var[str]
    ghost: Var[bool]
    size: Var[str]
    items: Var[Union[ContainVar, list]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_change': lambda e: [e],
        })
        return _triggers


collapse = Collapse.create
