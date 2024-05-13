from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any
from reflex import Component, Var
from ..base import AntdComponent, ContainVar, JsValue
from reflex.constants import EventTriggers
from .base import Locale
from reflex.utils import imports

class DayJS(JsValue):

    def serialize(self) -> str:
        ...

class Calendar(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, cell_render: Optional[Union[Var[JsValue], JsValue]]=None, full_cell_render: Optional[Union[Var[JsValue], JsValue]]=None, default_value: Optional[Union[Var[JsValue], JsValue]]=None, disabled_date: Optional[Union[Var[JsValue], JsValue]]=None, fullscreen: Optional[Union[Var[bool], bool]]=None, header_render: Optional[Union[Var[JsValue], JsValue]]=None, locale: Optional[Union[Var[Locale], Locale]]=None, mode: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[JsValue], JsValue]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_panel_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Calendar':
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
dayjs = DayJS
calendar = Calendar.create