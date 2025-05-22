from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, JsNode, ReactNode
from ..constant import StatusType, SizeType


class Tree(AntdComponent):
    tag = 'Tree'

    allow_drop: Var[JsNode]
    auto_expand_parent: Var[bool]
    block_node: Var[bool]
    checkable: Var[bool]
    checked_keys: Var[Union[List, Dict]]
    check_strictly: Var[bool]
    default_checked_keys: Var[List[str]]
    default_expand_all: Var[bool]
    default_expanded_keys: Var[List[str]]
    default_expand_parent: Var[bool]
    default_selected_keys: Var[List[str]]
    disabled: Var[bool]
    draggable: Var[Union[bool, JsNode, ContainVar]]
    expanded_keys: Var[List[str]]
    field_names: Var[Dict]
    filter_tree_node: Var[JsNode]
    height: Var[int]
    icon: Var[Union[ReactNode, JsNode]]
    load_data: Var[JsNode]
    loaded_keys: Var[List[str]]
    multiple: Var[bool]
    root_style: Var[Dict]
    selectable: Var[bool]
    selected_keys: Var[List[str]]
    show_icon: Var[bool]
    show_line: Var[Union[bool, ContainVar]]
    switcher_icon: Var[Union[ReactNode, JsNode]]
    title_render: Var[JsNode]
    tree_data: Var[List[Dict]]
    virtual: Var[bool]
    # DirectoryTree
    expand_action: Var[Union[bool, str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_check": lambda keys, e: [keys, e],
            "on_drag_end": lambda e: [e.event, e.node],
            "on_drag_enter": lambda e: [e.event, e.node, e.expandedKeys],
            "on_drag_leave": lambda e: [e.event, e.node],
            "on_drag_over": lambda e: [e.event, e.node],
            "on_drag_start": lambda e: [e.event, e.node],
            "on_drop": lambda e: [e.node, e.dragNode, e.dragNodesKeys, e.dropPosition, e.dropToGap],  # e.event,
            "on_expand": lambda keys, e: [keys, e],
            "on_load": lambda keys, e: [keys, e],
            "on_right_click": lambda e: [e.event, e.node],
            "on_select": lambda keys, e: [keys, e],

            "load_data": lambda node: [node],
            "filter_tree_node": lambda node: [node],
        })
        return _triggers


tree = Tree.create



