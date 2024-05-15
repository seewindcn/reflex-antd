from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsNode, ReactNode

class TreeSelect(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_clear: Optional[Union[Var[Union[bool, str, Component]], Union[bool, str, Component]]]=None, auto_clear_search_value: Optional[Union[Var[bool], bool]]=None, default_value: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, popup_match_select_width: Optional[Union[Var[Union[bool, int]], Union[bool, int]]]=None, dropdown_render: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, dropdown_style: Optional[Union[Var[Dict], Dict]]=None, field_names: Optional[Union[Var[Dict], Dict]]=None, filter_tree_node: Optional[Union[Var[Union[bool, JsValue, JsEvent]], Union[bool, JsValue, JsEvent]]]=None, get_popup_container: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, label_in_value: Optional[Union[Var[bool], bool]]=None, list_height: Optional[Union[Var[int], int]]=None, load_data: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, max_tag_count: Optional[Union[Var[int], int]]=None, max_tag_placeholder: Optional[Union[Var[Union[str, Component, JsValue, JsEvent]], Union[str, Component, JsValue, JsEvent]]]=None, max_tag_text_length: Optional[Union[Var[int], int]]=None, multiple: Optional[Union[Var[bool], bool]]=None, not_found_content: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, placeholder: Optional[Union[Var[str], str]]=None, placement: Optional[Union[Var[str], str]]=None, search_value: Optional[Union[Var[str], str]]=None, show_checked_strategy: Optional[Union[Var[str], str]]=None, show_search: Optional[Union[Var[bool], bool]]=None, size: Optional[Union[Var[str], str]]=None, status: Optional[Union[Var[str], str]]=None, suffix_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, switcher_icon: Optional[Union[Var[Union[str, Component, ContainVar]], Union[str, Component, ContainVar]]]=None, tag_render: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, tree_checkable: Optional[Union[Var[bool], bool]]=None, tree_check_strictly: Optional[Union[Var[bool], bool]]=None, tree_data: Optional[Union[Var[List[Dict]], List[Dict]]]=None, tree_data_simple_mode: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, tree_default_expand_all: Optional[Union[Var[bool], bool]]=None, tree_default_expanded_keys: Optional[Union[Var[List], List]]=None, tree_expand_action: Optional[Union[Var[Union[bool, str]], Union[bool, str]]]=None, tree_expanded_keys: Optional[Union[Var[List[str]], List[str]]]=None, tree_icon: Optional[Union[Var[bool], bool]]=None, tree_line: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, tree_loaded_keys: Optional[Union[Var[List[str]], List[str]]]=None, tree_node_filter_prop: Optional[Union[Var[str], str]]=None, tree_node_label_prop: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, variant: Optional[Union[Var[str], str]]=None, virtual: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, filter_tree_node: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, load_data: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_dropdown_visible_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_search: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_tree_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TreeSelect':
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...
tree_select = TreeSelect.create