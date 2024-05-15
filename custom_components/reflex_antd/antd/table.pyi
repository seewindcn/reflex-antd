from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports
from ..base import AntdComponent, ContainVar, JsValue, JsEvent
from ..constant import StatusType, SizeType

class Table(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, bordered: Optional[Union[Var[bool], bool]]=None, columns: Optional[Union[Var[Union[ContainVar, list]], Union[ContainVar, list]]]=None, data_source: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]]=None, expandable: Optional[Union[Var[ContainVar], ContainVar]]=None, footer: Optional[Union[Var[JsValue], JsValue]]=None, get_popup_container: Optional[Union[Var[JsValue], JsValue]]=None, loading: Optional[Union[Var[bool], bool]]=None, locale: Optional[Union[Var[ContainVar], ContainVar]]=None, pagination: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, row_key: Optional[Union[Var[Union[str, JsValue]], Union[str, JsValue]]]=None, row_selection: Optional[Union[Var[ContainVar], ContainVar]]=None, scroll: Optional[Union[Var[Union[ContainVar, Dict]], Union[ContainVar, Dict]]]=None, show_header: Optional[Union[Var[bool], bool]]=None, show_sorter_tooltip: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, sort_directions: Optional[Union[Var[ContainVar], ContainVar]]=None, sticky: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, summary: Optional[Union[Var[JsValue], JsValue]]=None, table_layout: Optional[Union[Var[str], str]]=None, title: Optional[Union[Var[JsValue], JsValue]]=None, virtual: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, columns.*.on_cell: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, columns.*.on_filter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, columns.*.on_filter_dropdown_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, columns.*.on_header_cell: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, expandable.on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, expandable.on_expanded_rows_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_header_row: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_row: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, pagination.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, pagination.on_show_size_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, row_selection.on_cell: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, row_selection.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, row_selection.on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, row_selection.on_select_all: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Table':
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
table = Table.create