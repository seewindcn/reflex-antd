from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, JsNode, ReactNode
from ..constant import StatusType, SizeType


class Tree(AntdComponent):
    tag = 'Tree'

    allow_drop: Optional[Var[JsNode]]
    auto_expand_parent: Optional[Var[bool]]
    block_node: Optional[Var[bool]]
    checkable: Optional[Var[bool]]
    checked_keys: Optional[Var[Union[List, Dict]]]
    check_strictly: Optional[Var[bool]]
    default_checked_keys: Optional[Var[List[str]]]
    default_expand_all: Optional[Var[bool]]
    default_expanded_keys: Optional[Var[List[str]]]
    default_expand_parent: Optional[Var[bool]]
    default_selected_keys: Optional[Var[List[str]]]
    disabled: Optional[Var[bool]]
    draggable: Optional[Var[Union[bool, JsNode, ContainVar]]]
    expanded_keys: Optional[Var[List[str]]]
    field_names: Optional[Var[Dict]]
    filter_tree_node: Optional[Var[JsNode]]
    height: Optional[Var[int]]
    icon: Optional[Var[Union[ReactNode, JsNode]]]
    load_data: Optional[Var[JsNode]]
    loaded_keys: Optional[Var[List[str]]]
    multiple: Optional[Var[bool]]
    root_style: Optional[Var[Dict]]
    selectable: Optional[Var[bool]]
    selected_keys: Optional[Var[List[str]]]
    show_icon: Optional[Var[bool]]
    show_line: Optional[Var[Union[bool, ContainVar]]]
    switcher_icon: Optional[Var[Union[ReactNode, JsNode]]]
    title_render: Optional[Var[JsNode]]
    tree_data: Optional[Var[List[Dict]]]
    virtual: Optional[Var[bool]]
    # DirectoryTree
    expand_action: Optional[Var[Union[bool, str]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_check": lambda keys, e: [keys, e],
            "on_drag_end": lambda e: [e.event, e.node],
            "on_drag_enter": lambda e: [e.event, e.node, e.expandedKeys],
            "on_drag_leave": lambda e: [e.event, e.node],
            "on_drag_over": lambda e: [e.event, e.node],
            "on_drag_start": lambda e: [e.event, e.node],
            "on_drop": lambda e: [e.event, e.node, e.dragNode, e.dragNodesKeys],
            "on_expand": lambda keys, e: [keys, e],
            "on_load": lambda keys, e: [keys, e],
            "on_right_click": lambda e: [e.event, e.node],
            "on_select": lambda keys, e: [keys, e],

            "load_data": lambda node: [node],
            "filter_tree_node": lambda node: [node],
        })
        return _triggers


tree = Tree.create



