from typing import Optional, Union, Dict, Any, List, Tuple
from dataclasses import dataclass, asdict

from reflex import Component, Var, Base
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, DataClassMixin, PropBase, vt
from ..constant import SizeType, OrientationType, TabsType


# @dataclass(frozen=True)
class TabItem(PropBase):
    close_icon: ReactNode = None
    destroy_inactive_tab_pane: vt(bool) = None
    disabled: vt(bool) = None
    force_render: vt(bool) = None
    key: vt(str) = None
    label: vt(ReactNode) = None
    icon: ReactNode = None
    children: ReactNode = None
    closable: vt(bool) = None


class Tabs(AntdComponent):
    tag = 'Tabs'

    active_key: Var[Union[str, int]]
    add_icon: Var[ReactNode]
    animated: Var[Union[bool, Dict]]
    centered: Var[bool]
    default_active_key: Var[Union[str, int]]
    hide_add: Var[bool]
    indicator: Var[Union[Dict, ContainVar]]
    items: Var[Union[ContainVar, List]]
    more: Var[ContainVar | dict]
    remove_icon: Var[ReactNode]
    popup_class_name: Var[str]
    render_tab_bar: Var[JsValue]
    size: Var[SizeType]
    tab_bar_extra_content: Var[Union[ReactNode, ContainVar]]
    tab_bar_gutter: Var[int]
    tab_bar_style: Var[Dict]
    tab_position: Var[OrientationType]
    destroy_inactive_tab_pane: Var[bool]
    type: Var[TabsType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda key: [key],
            EventTriggers.ON_EDIT: lambda e0, e1: [e0, e1],
            "on_tab_click": lambda key, ev: [key, ev],
            "on_tab_scroll": lambda ev: [ev],
            "on_edit": lambda key, ev: [key, ev],
        })
        return _triggers


tabs = Tabs.create
tab_item = TabItem
