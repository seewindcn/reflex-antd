from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType


class Select(AntdComponent):
    tag = 'Select'

    allow_clear: Optional[Var[bool]]
    auto_clear_search_value: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    default_active_first_option: Optional[Var[bool]]
    default_open: Optional[Var[bool]]
    default_value: Optional[Var[Union[int, str, List[str], List[int], ContainVar]]]
    disabled: Optional[Var[bool]]
    popup_class_name: Optional[Var[str]]
    popup_match_select_width: Optional[Var[Union[bool, int]]]
    dropdown_render: Optional[Var[JsValue]]
    dropdown_style: Optional[Var[Dict]]
    field_names: Optional[Var[Dict]]
    filter_option: Optional[Var[Union[bool, JsValue]]]
    filter_sort: Optional[Var[JsValue]]
    get_popup_container: Optional[Var[JsValue]]
    label_in_value: Optional[Var[bool]]
    list_height: Optional[Var[int]]
    loading: Optional[Var[bool]]
    max_count: Optional[Var[int]]
    max_tag_count: Optional[Var[Union[int, str]]]
    max_tag_placeholder: Optional[Var[Union[ReactNode, JsValue]]]
    max_tag_text_length: Optional[Var[int]]
    menu_item_selected_icon: Optional[Var[ReactNode]]
    mode: Optional[Var[SelectModeType]]
    not_found_content: Optional[Var[ReactNode]]
    open: Optional[Var[bool]]
    option_filter_prop: Optional[Var[str]]
    option_label_prop: Optional[Var[str]]
    options: Optional[Var[Union[list, ContainVar]]]
    option_render: Optional[Var[JsValue]]
    placeholder: Optional[Var[ReactNode]]
    placement: Optional[Var[PlacementType]]
    remove_icon: Optional[Var[ReactNode]]
    search_value: Optional[Var[str]]
    show_search: Optional[Var[bool]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[StatusType]]
    suffix_icon: Optional[Var[ReactNode]]
    tag_render: Optional[Var[JsValue]]
    label_render: Optional[Var[JsValue]]
    token_separators: Optional[Var[List[str]]]
    value: Optional[Var[Union[str, int, List[str], List[int], ContainVar]]]
    variant: Optional[Var[VariantType]]
    virtual: Optional[Var[bool]]

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

