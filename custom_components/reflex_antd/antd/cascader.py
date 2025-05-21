from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TriggerType, PlacementType, SizeType, StatusType, VariantType


class Cascader(AntdComponent):
    tag = 'Cascader'

    allow_clear: Var[bool]
    auto_clear_search_value: Var[bool]
    auto_focus: Var[bool]
    change_on_select: Var[bool]
    default_value: Var[Union[List[int], List[str]]]
    disabled: Var[bool]
    display_render: Var[JsValue]
    tag_render: Var[JsValue]
    popup_class_name: Var[str]
    dropdown_render: Var[JsValue]
    expand_icon: Var[ReactNode]
    expand_trigger: Var[TriggerType]
    field_names: Var[ContainVar]
    get_popup_container: Var[JsValue]
    load_data: Var[JsValue]
    max_tag_count: Var[int]
    max_tag_placeholder: Var[Union[ReactNode, JsValue]]
    max_tag_text_length: Var[int]
    not_found_content: Var[str]
    open: Var[bool]
    options: Var[Union[ContainVar, list]]
    placeholder: Var[ReactNode]
    placement: Var[PlacementType]
    show_search: Var[Union[bool, ContainVar]]
    size: Var[SizeType]
    status: Var[StatusType]
    suffix_icon: Var[ReactNode]
    value: Var[Union[List[str], List[int]]]
    variant: Var[VariantType]
    multiple: Var[bool]
    remove_icon: Var[ReactNode]
    show_checked_strategy: Var[str]
    search_value: Var[str]
    dropdown_menu_column_style: Var[ContainVar]
    loading_icon: Var[ReactNode]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value, options: [value, options],
            "on_dropdown_visible_change": lambda value: [value],
            "on_search": lambda search: [search]
        })
        return _triggers


cascader = Cascader.create
