from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, List, Dict, Any
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent

class Pagination(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, current: Optional[Union[Var[int], int]]=None, default_current: Optional[Union[Var[int], int]]=None, default_page_size: Optional[Union[Var[int], int]]=None, disabled: Optional[Union[Var[bool], bool]]=None, hide_on_single_page: Optional[Union[Var[bool], bool]]=None, page_size: Optional[Union[Var[int], int]]=None, page_size_options: Optional[Union[Var[List[int]], List[int]]]=None, responsive: Optional[Union[Var[bool], bool]]=None, show_less_items: Optional[Union[Var[bool], bool]]=None, show_quick_jumper: Optional[Union[Var[bool], bool]]=None, show_size_changer: Optional[Union[Var[bool], bool]]=None, show_title: Optional[Union[Var[bool], bool]]=None, simple: Optional[Union[Var[bool], bool]]=None, size: Optional[Union[Var[int], int]]=None, total: Optional[Union[Var[int], int]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, show_total: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Pagination':
        """Create the component.

        Args:
            *children: The children of the component.
            simple: showTotal
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
pagination = Pagination.create