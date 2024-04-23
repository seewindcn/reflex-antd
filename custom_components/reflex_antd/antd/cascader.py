from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TriggerType, PlacementType, SizeType, StatusType, VariantType


class Cascader(AntdComponent):
    tag = 'Cascader'

    allow_clear: Optional[Var[bool]]
    auto_clear_search_value: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    change_on_select: Optional[Var[bool]]
    default_value: Optional[Var[Union[List[int], List[str]]]]
    disabled: Optional[Var[bool]]
    display_render: Optional[Var[JsValue]]
    tag_render: Optional[Var[JsValue]]
    popup_class_name: Optional[Var[str]]
    dropdown_render: Optional[Var[JsValue]]
    expand_icon: Optional[Var[ReactNode]]
    expand_trigger: Optional[Var[TriggerType]]
    field_names: Optional[Var[ContainVar]]
    get_popup_container: Optional[Var[JsValue]]
    load_data: Optional[Var[JsValue]]
    max_tag_count: Optional[Var[int]]
    max_tag_placeholder: Optional[Var[Union[ReactNode, JsValue]]]
    max_tag_text_length: Optional[Var[int]]
    not_found_content: Optional[Var[str]]
    open: Optional[Var[bool]]
    options: Optional[Var[Union[ContainVar, list]]]
    placeholder: Optional[Var[ReactNode]]
    placement: Optional[Var[PlacementType]]
    show_search: Optional[Var[Union[bool, ContainVar]]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[StatusType]]
    suffix_icon: Optional[Var[ReactNode]]
    value: Optional[Var[Union[List[str], List[int]]]]
    variant: Optional[Var[VariantType]]
    multiple: Optional[Var[bool]]
    remove_icon: Optional[Var[ReactNode]]
    show_checked_strategy: Optional[Var[str]]
    search_value: Optional[Var[str]]
    dropdown_menu_column_style: Optional[Var[ContainVar]]
    loading_icon: Optional[Var[ReactNode]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value, options: [value, options],
            "on_dropdown_visible_change": lambda value: [value],
            "on_search": lambda search: [search]
        })
        return _triggers


cascader = Cascader.create
