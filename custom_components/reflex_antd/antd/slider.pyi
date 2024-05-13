from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType

class Slider(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, auto_adjust_overflow: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, default_value: Optional[Union[Var[Union[int, List[int]]], Union[int, List[int]]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, keyboard: Optional[Union[Var[bool], bool]]=None, dots: Optional[Union[Var[bool], bool]]=None, included: Optional[Union[Var[bool], bool]]=None, marks: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, max: Optional[Union[Var[int], int]]=None, min: Optional[Union[Var[int], int]]=None, range: Optional[Union[Var[bool], bool]]=None, reverse: Optional[Union[Var[bool], bool]]=None, step: Optional[Union[Var[int], int]]=None, tooltip: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, value: Optional[Union[Var[Union[int, List[int]]], Union[int, List[int]]]]=None, vertical: Optional[Union[Var[bool], bool]]=None, draggable_track: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change_complete: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Slider':
        """Create the component.

        Args:
            *children: The children of the component.
            draggable_track: range
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
slider = Slider.create