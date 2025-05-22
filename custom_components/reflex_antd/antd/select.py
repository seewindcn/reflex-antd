from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExTypes
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType


class Select(AntdComponent):
    tag = 'Select'

    allow_clear: Var[bool]
    auto_clear_search_value: Var[bool]
    auto_focus: Var[bool]
    default_active_first_option: Var[bool]
    default_open: Var[bool]
    default_value: Var[Union[int, str, List[str], List[int], ContainVar]]
    disabled: Var[bool]
    popup_class_name: Var[str]
    popup_match_select_width: Var[Union[bool, int]]
    dropdown_render: Var[JsValue]
    dropdown_style: Var[Dict]

    popup_render: Var[ExTypes]
    styles: Var[dict | ContainVar]

    field_names: Var[Dict]
    filter_option: Var[Union[bool, JsValue]]
    filter_sort: Var[JsValue]
    get_popup_container: Var[JsValue]
    label_in_value: Var[bool]
    list_height: Var[int]
    loading: Var[bool]
    max_count: Var[int]
    max_tag_count: Var[Union[int, str]]
    max_tag_placeholder: Var[Union[ReactNode, JsValue]]
    max_tag_text_length: Var[int]
    menu_item_selected_icon: Var[ReactNode]
    mode: Var[SelectModeType]
    not_found_content: Var[ReactNode]
    open: Var[bool]
    option_filter_prop: Var[str]
    option_label_prop: Var[str]
    options: Var[Union[list, ContainVar]]
    option_render: Var[JsValue]
    placeholder: Var[ReactNode]
    placement: Var[PlacementType]
    remove_icon: Var[ReactNode]
    search_value: Var[str]
    show_search: Var[bool]
    size: Var[SizeType]
    status: Var[StatusType]
    suffix_icon: Var[ReactNode]
    tag_render: Var[JsValue]
    label_render: Var[JsValue]
    token_separators: Var[List[str]]
    value: Var[Union[str, int, List[str], List[int], ContainVar]]
    variant: Var[VariantType]
    virtual: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda v, option: [v, option],
            "on_clear": lambda: [],
            "on_deselect": lambda v: [v],
            "on_dropdown_visible_change": lambda open: [open],
            "on_input_key_down": lambda: [],
            "on_popup_scroll": lambda: [],
            "on_search": lambda v: [v],
            "on_select": lambda v, option: [v, option],
        })
        return _triggers


select = Select.create

