from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Component, Var
from ..base import AntdComponent, ContainVar, JsValue

class Collapse(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, accordion: Optional[Union[Var[bool], bool]]=None, active_key: Optional[Union[Var[Union[list[str], str, list[int], int]], Union[list[str], str, list[int], int]]]=None, bordered: Optional[Union[Var[bool], bool]]=None, default_active_key: Optional[Union[Var[Union[list[str], str, list[int], int]], Union[list[str], str, list[int], int]]]=None, destroy_inactive_panel: Optional[Union[Var[bool], bool]]=None, expand_icon: Optional[Union[Var[Component], Component]]=None, collapsible: Optional[Union[Var[str], str]]=None, expand_icon_position: Optional[Union[Var[str], str]]=None, ghost: Optional[Union[Var[bool], bool]]=None, size: Optional[Union[Var[str], str]]=None, items: Optional[Union[Var[Union[ContainVar, list]], Union[ContainVar, list]]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Collapse':
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
collapse = Collapse.create