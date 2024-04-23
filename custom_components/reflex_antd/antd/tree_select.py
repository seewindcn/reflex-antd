from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsNode, ReactNode


class TreeSelect(AntdComponent):
    tag = 'TreeSelect'

    allow_clear: Optional[Var[Union[bool, ReactNode]]]
    auto_clear_search_value: Optional[Var[bool]]
    default_value: Optional[Var[Union[str, List[str]]]]
    disabled: Optional[Var[bool]]
    popup_class_name: Optional[Var[str]]
    popup_match_select_width: Optional[Var[Union[bool, int]]]
    dropdown_render: Optional[Var[JsNode]]
    dropdown_style: Optional[Var[Dict]]
    field_names: Optional[Var[Dict]]
    filter_tree_node: Optional[Var[Union[bool, JsNode]]]
    get_popup_container: Optional[Var[JsNode]]
    label_in_value: Optional[Var[bool]]
    list_height: Optional[Var[int]]
    load_data: Optional[Var[JsNode]]
    max_tag_count: Optional[Var[int]]
    max_tag_placeholder: Optional[Var[Union[ReactNode, JsNode]]]
    max_tag_text_length: Optional[Var[int]]
    multiple: Optional[Var[bool]]
    not_found_content: Optional[Var[ReactNode]]
    placeholder: Optional[Var[str]]
    placement: Optional[Var[str]]
    search_value: Optional[Var[str]]
    show_checked_strategy: Optional[Var[str]]
    show_search: Optional[Var[bool]]
    size: Optional[Var[str]]
    status: Optional[Var[str]]
    suffix_icon: Optional[Var[ReactNode]]
    switcher_icon: Optional[Var[Union[ReactNode, ContainVar]]]
    tag_render: Optional[Var[JsNode]]
    tree_checkable: Optional[Var[bool]]
    tree_check_strictly: Optional[Var[bool]]
    tree_data: Optional[Var[List[Dict]]]
    tree_data_simple_mode: Optional[Var[Union[bool, Dict]]]
    tree_default_expand_all: Optional[Var[bool]]
    tree_default_expanded_keys: Optional[Var[List]]
    tree_expand_action: Optional[Var[Union[str, bool]]]
    tree_expanded_keys: Optional[Var[List[str]]]
    tree_icon: Optional[Var[bool]]
    tree_line: Optional[Var[Union[bool, Dict]]]
    tree_loaded_keys: Optional[Var[List[str]]]
    tree_node_filter_prop: Optional[Var[str]]
    tree_node_label_prop: Optional[Var[str]]
    value: Optional[Var[Union[str, List[str]]]]
    variant: Optional[Var[str]]
    virtual: Optional[Var[str]]

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
