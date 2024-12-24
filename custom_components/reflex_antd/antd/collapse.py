from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Collapse(AntdComponent):
    tag = 'Collapse'

    accordion: Optional[Var[bool]]
    active_key: Optional[Var[Union[list[str], str, list[int], int]]]
    bordered: Optional[Var[bool]]
    default_active_key: Optional[Var[Union[list[str], str, list[int], int]]]
    destroy_inactive_panel: Optional[Var[bool]]
    expand_icon: Optional[Var[ReactNode]]
    collapsible: Optional[Var[str]]
    expand_icon_position: Optional[Var[str]]
    ghost: Optional[Var[bool]]
    size: Optional[Var[str]]
    items: Optional[Var[Union[ContainVar, list]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_change': lambda e: [e],
        })
        return _triggers


collapse = Collapse.create
