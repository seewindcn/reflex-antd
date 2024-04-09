from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType

class Select(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_clear: Optional[Union[Var[bool], bool]]=None, auto_clear_search_value: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, default_active_first_option: Optional[Union[Var[bool], bool]]=None, default_open: Optional[Union[Var[bool], bool]]=None, default_value: Optional[Union[Var[Union[int, str, List[str], List[int], ContainVar]], Union[int, str, List[str], List[int], ContainVar]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, popup_match_select_width: Optional[Union[Var[Union[bool, int]], Union[bool, int]]]=None, dropdown_render: Optional[Union[Var[JsValue], JsValue]]=None, dropdown_style: Optional[Union[Var[Dict], Dict]]=None, field_names: Optional[Union[Var[Dict], Dict]]=None, filter_option: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, filter_sort: Optional[Union[Var[JsValue], JsValue]]=None, get_popup_container: Optional[Union[Var[JsValue], JsValue]]=None, label_in_value: Optional[Union[Var[bool], bool]]=None, list_height: Optional[Union[Var[int], int]]=None, loading: Optional[Union[Var[bool], bool]]=None, max_count: Optional[Union[Var[int], int]]=None, max_tag_count: Optional[Union[Var[Union[str, int]], Union[str, int]]]=None, max_tag_placeholder: Optional[Union[Var[Union[Component, JsValue]], Union[Component, JsValue]]]=None, max_tag_text_length: Optional[Union[Var[int], int]]=None, menu_item_selected_icon: Optional[Union[Var[Component], Component]]=None, mode: Optional[Union[Var[Literal['multiple', 'tags']], Literal['multiple', 'tags']]]=None, not_found_content: Optional[Union[Var[Component], Component]]=None, open: Optional[Union[Var[bool], bool]]=None, option_filter_prop: Optional[Union[Var[str], str]]=None, option_label_prop: Optional[Union[Var[str], str]]=None, options: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, option_render: Optional[Union[Var[JsValue], JsValue]]=None, placeholder: Optional[Union[Var[Component], Component]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, remove_icon: Optional[Union[Var[Component], Component]]=None, search_value: Optional[Union[Var[str], str]]=None, show_search: Optional[Union[Var[bool], bool]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, suffix_icon: Optional[Union[Var[Component], Component]]=None, tag_render: Optional[Union[Var[JsValue], JsValue]]=None, label_render: Optional[Union[Var[JsValue], JsValue]]=None, token_separators: Optional[Union[Var[List[str]], List[str]]]=None, value: Optional[Union[Var[Union[int, str, List[str], List[int], ContainVar]], Union[int, str, List[str], List[int], ContainVar]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, virtual: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_clear: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_deselect: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_dropdown_visible_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_input_key_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_popup_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_search: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Select':
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

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
select = Select.create