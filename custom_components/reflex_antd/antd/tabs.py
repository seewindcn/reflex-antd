from typing import Optional, Union, Dict, Any, List, Tuple
from dataclasses import dataclass, asdict

from reflex import Component, Var, Base
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, DataClassMixin
from ..constant import SizeType, OrientationType, TabsType


@dataclass(frozen=True)
class TabItem(DataClassMixin):
    close_icon: Optional[Var[ReactNode]] = None
    destroy_inactive_tab_pane: Optional[Var[bool]] = None
    disabled: Optional[Var[bool]] = None
    force_render: Optional[Var[bool]] = None
    key: Optional[Union[str, Var[str]]] = None
    label: Optional[Union[ReactNode, Var[ReactNode]]] = None
    icon: Optional[Union[ReactNode, Var[ReactNode]]] = None
    children: Optional[Union[ReactNode, Var[ReactNode]]] = None
    closable: Optional[Var[bool]] = None


class Tabs(AntdComponent):
    tag = 'Tabs'

    active_key: Optional[Var[Union[str, int]]]
    add_icon: Optional[Var[ReactNode]]
    animated: Optional[Var[Union[bool, Dict]]]
    centered: Optional[Var[bool]]
    default_active_key: Optional[Var[Union[str, int]]]
    hide_add: Optional[Var[bool]]
    indicator: Optional[Var[Union[Dict, ContainVar]]]
    items: Optional[Var[Union[ContainVar, List]]]
    more_icon: Optional[Var[ReactNode]]
    remove_icon: Optional[Var[ReactNode]]
    popup_class_name: Optional[Var[str]]
    render_tab_bar: Optional[Var[JsValue]]
    size: Optional[Var[SizeType]]
    tab_bar_extra_content: Optional[Var[Union[ReactNode, ContainVar]]]
    tab_bar_gutter: Optional[Var[int]]
    tab_bar_style: Optional[Var[Dict]]
    tab_position: Optional[Var[OrientationType]]
    destroy_inactive_tab_pane: Optional[Var[bool]]
    type: Optional[Var[TabsType]]

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
