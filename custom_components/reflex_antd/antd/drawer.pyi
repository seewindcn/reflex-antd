from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Component, Var
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import OrientationType, SizeType

class Drawer(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, auto_focus: Optional[Union[Var[bool], bool]]=None, class_name: Optional[Union[Var[str], str]]=None, class_names: Optional[Union[Var[ContainVar], ContainVar]]=None, close_icon: Optional[Union[Var[Union[str, Component, bool]], Union[str, Component, bool]]]=None, destroy_on_close: Optional[Union[Var[bool], bool]]=None, extra: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, footer: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, force_render: Optional[Union[Var[bool], bool]]=None, get_container: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, height: Optional[Union[Var[Union[int, str]], Union[int, str]]]=None, keyboard: Optional[Union[Var[bool], bool]]=None, mask: Optional[Union[Var[bool], bool]]=None, mask_closable: Optional[Union[Var[bool], bool]]=None, placement: Optional[Union[Var[Literal['left', 'right', 'top', 'bottom', 'center']], Literal['left', 'right', 'top', 'bottom', 'center']]]=None, push: Optional[Union[Var[Union[bool, dict]], Union[bool, dict]]]=None, root_style: Optional[Union[Var[dict], dict]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, styles: Optional[Union[Var[ContainVar], ContainVar]]=None, title: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, open: Optional[Union[Var[bool], bool]]=None, width: Optional[Union[Var[Union[int, str]], Union[int, str]]]=None, z_index: Optional[Union[Var[int], int]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, after_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_close: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Drawer':
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
drawer = Drawer.create