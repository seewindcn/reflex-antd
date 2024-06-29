from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Component, Var
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TypeType

class Popconfirm(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, cancel_button_orops: Optional[Union[Var[dict], dict]]=None, cancel_text: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, ok_button_props: Optional[Union[Var[dict], dict]]=None, ok_text: Optional[Union[Var[str], str]]=None, ok_type: Optional[Union[Var[Literal['default', 'primary', 'dashed', 'link', 'text']], Literal['default', 'primary', 'dashed', 'link', 'text']]]=None, open: Optional[Union[Var[bool], bool]]=None, show_cancel: Optional[Union[Var[bool], bool]]=None, title: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, description: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, _custom_components: Optional[Set[CustomComponent]]=None, _ex_hooks: Optional[List[ContainVar]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_confirm: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_popup_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Popconfirm':
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
popconfirm = Popconfirm.create