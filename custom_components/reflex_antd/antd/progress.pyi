from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Tuple
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, ProgressType, SizeType, OrientationType

class Progress(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, format: Optional[Union[Var[JsValue], JsValue]]=None, percent: Optional[Union[Var[int], int]]=None, show_info: Optional[Union[Var[bool], bool]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, stroke_color: Optional[Union[Var[Union[str, List[str], Dict]], Union[str, List[str], Dict]]]=None, stroke_linecap: Optional[Union[Var[str], str]]=None, success: Optional[Union[Var[Dict], Dict]]=None, trail_color: Optional[Union[Var[str], str]]=None, type: Optional[Union[Var[Literal['line', 'circle', 'dashboard']], Literal['line', 'circle', 'dashboard']]]=None, size: Optional[Union[Var[Union[int, Literal['default', 'small', 'medium', 'middle', 'large'], List[Union[int, Literal['default', 'small', 'medium', 'middle', 'large']]]]], Union[int, Literal['default', 'small', 'medium', 'middle', 'large'], List[Union[int, Literal['default', 'small', 'medium', 'middle', 'large']]]]]]=None, steps: Optional[Union[Var[Union[int, Dict]], Union[int, Dict]]]=None, stroke_width: Optional[Union[Var[int], int]]=None, gap_degree: Optional[Union[Var[int], int]]=None, gap_position: Optional[Union[Var[Literal['left', 'right', 'top', 'bottom', 'center']], Literal['left', 'right', 'top', 'bottom', 'center']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Progress':
        """Create the component.

        Args:
            *children: The children of the component.
            steps: type=...
            gap_degree: dashboard
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
progress = Progress.create