from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TriggerType, PlacementType, SizeType, StatusType, VariantType

class Cascader(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_clear: Optional[Union[Var[bool], bool]]=None, auto_clear_search_value: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, change_on_select: Optional[Union[Var[bool], bool]]=None, default_value: Optional[Union[Var[Union[List[int], List[str]]], Union[List[int], List[str]]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, display_render: Optional[Union[Var[JsValue], JsValue]]=None, tag_render: Optional[Union[Var[JsValue], JsValue]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, dropdown_render: Optional[Union[Var[JsValue], JsValue]]=None, expand_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, expand_trigger: Optional[Union[Var[Literal['click', 'hover', 'focus', 'contextMenu']], Literal['click', 'hover', 'focus', 'contextMenu']]]=None, field_names: Optional[Union[Var[ContainVar], ContainVar]]=None, get_popup_container: Optional[Union[Var[JsValue], JsValue]]=None, load_data: Optional[Union[Var[JsValue], JsValue]]=None, max_tag_count: Optional[Union[Var[int], int]]=None, max_tag_placeholder: Optional[Union[Var[Union[str, Component, JsValue]], Union[str, Component, JsValue]]]=None, max_tag_text_length: Optional[Union[Var[int], int]]=None, not_found_content: Optional[Union[Var[str], str]]=None, open: Optional[Union[Var[bool], bool]]=None, options: Optional[Union[Var[Union[ContainVar, list]], Union[ContainVar, list]]]=None, placeholder: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, show_search: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, suffix_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, value: Optional[Union[Var[Union[List[int], List[str]]], Union[List[int], List[str]]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, multiple: Optional[Union[Var[bool], bool]]=None, remove_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, show_checked_strategy: Optional[Union[Var[str], str]]=None, search_value: Optional[Union[Var[str], str]]=None, dropdown_menu_column_style: Optional[Union[Var[ContainVar], ContainVar]]=None, loading_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_dropdown_visible_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_search: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Cascader':
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
cascader = Cascader.create