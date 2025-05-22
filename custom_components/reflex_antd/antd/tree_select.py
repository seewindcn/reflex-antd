from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsNode, ReactNode


class TreeSelect(AntdComponent):
    tag = 'TreeSelect'

    allow_clear: Var[Union[bool, ReactNode]]
    auto_clear_search_value: Var[bool]
    default_value: Var[Union[str, List[str]]]
    disabled: Var[bool]
    popup_class_name: Var[str]
    popup_match_select_width: Var[Union[bool, int]]
    dropdown_render: Var[JsNode]
    dropdown_style: Var[Dict]
    field_names: Var[Dict]
    filter_tree_node: Var[Union[bool, JsNode]]
    get_popup_container: Var[JsNode]
    label_in_value: Var[bool]
    list_height: Var[int]
    load_data: Var[JsNode]
    max_tag_count: Var[int]
    max_tag_placeholder: Var[Union[ReactNode, JsNode]]
    max_tag_text_length: Var[int]
    multiple: Var[bool]
    not_found_content: Var[ReactNode]
    placeholder: Var[str]
    placement: Var[str]
    search_value: Var[str]
    show_checked_strategy: Var[str]
    show_search: Var[bool]
    size: Var[str]
    status: Var[str]
    suffix_icon: Var[ReactNode]
    switcher_icon: Var[Union[ReactNode, ContainVar]]
    tag_render: Var[JsNode]
    tree_checkable: Var[bool]
    tree_check_strictly: Var[bool]
    tree_data: Var[List[Dict]]
    tree_data_simple_mode: Var[Union[bool, Dict]]
    tree_default_expand_all: Var[bool]
    tree_default_expanded_keys: Var[List]
    tree_expand_action: Var[Union[str, bool]]
    tree_expanded_keys: Var[List[str]]
    tree_icon: Var[bool]
    tree_line: Var[Union[bool, Dict]]
    tree_loaded_keys: Var[List[str]]
    tree_node_filter_prop: Var[str]
    tree_node_label_prop: Var[str]
    value: Var[Union[str, List[str]]]
    variant: Var[str]
    virtual: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value, label, extra: [value, label, extra],
            EventTriggers.ON_SELECT: lambda value, node, extra: [value, node, extra],
            "on_dropdown_visible_change": lambda open: [open],
            "on_search": lambda value: [value],
            "on_tree_expand": lambda keys: [keys],

            "filter_tree_node": lambda node: [node],
            "load_data": lambda node: [node],
        })
        return _triggers


tree_select = TreeSelect.create
