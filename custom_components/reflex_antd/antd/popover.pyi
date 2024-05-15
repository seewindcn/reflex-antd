from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Tuple
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType
from .tooltip import Tooltip

class Popover(Tooltip):

    @overload
    @classmethod
    def create(cls, *children, content: Optional[Union[Var[Union[Component, ContainVar]], Union[Component, ContainVar]]]=None, title: Optional[Union[Var[Union[Component, ContainVar]], Union[Component, ContainVar]]]=None, align: Optional[Union[Var[str], str]]=None, arrow: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, auto_adjust_overflow: Optional[Union[Var[bool], bool]]=None, color: Optional[Union[Var[str], str]]=None, default_open: Optional[Union[Var[bool], bool]]=None, destroy_tooltip_on_hide: Optional[Union[Var[bool], bool]]=None, fresh: Optional[Union[Var[bool], bool]]=None, get_popup_container: Optional[Union[Var[JsValue], JsValue]]=None, mouse_enter_delay: Optional[Union[Var[int], int]]=None, mouse_leave_delay: Optional[Union[Var[int], int]]=None, overlay_class_name: Optional[Union[Var[str], str]]=None, overlay_style: Optional[Union[Var[Dict], Dict]]=None, overlay_inner_style: Optional[Union[Var[Dict], Dict]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, trigger: Optional[Union[Var[Union[Literal['click', 'hover', 'focus', 'contextMenu'], List[Literal['click', 'hover', 'focus', 'contextMenu']]]], Union[Literal['click', 'hover', 'focus', 'contextMenu'], List[Literal['click', 'hover', 'focus', 'contextMenu']]]]]=None, open: Optional[Union[Var[bool], bool]]=None, z_index: Optional[Union[Var[int], int]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Popover':
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
popover = Popover.create