from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Set
import uuid
from reflex import Component, Var
from reflex.utils import imports
from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, FakeComponentMixin
from ..constant import TypeType
from . import helper

class Modal(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, class_names: Optional[Union[Var[ContainVar], ContainVar]]=None, styles: Optional[Union[Var[ContainVar], ContainVar]]=None, cancel_button_props: Optional[Union[Var[ContainVar], ContainVar]]=None, cancel_text: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, centered: Optional[Union[Var[bool], bool]]=None, close_icon: Optional[Union[Var[Union[str, Component, bool]], Union[str, Component, bool]]]=None, confirm_loading: Optional[Union[Var[bool], bool]]=None, destroy_on_close: Optional[Union[Var[bool], bool]]=None, focus_trigger_after_close: Optional[Union[Var[bool], bool]]=None, footer: Optional[Union[Var[ContainVar], ContainVar]]=None, force_render: Optional[Union[Var[bool], bool]]=None, get_container: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, keyboard: Optional[Union[Var[bool], bool]]=None, mask: Optional[Union[Var[bool], bool]]=None, mask_closable: Optional[Union[Var[bool], bool]]=None, modal_render: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, ok_button_props: Optional[Union[Var[ContainVar], ContainVar]]=None, ok_text: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, ok_type: Optional[Union[Var[Literal['default', 'primary']], Literal['default', 'primary']]]=None, title: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, open: Optional[Union[Var[bool], bool]]=None, width: Optional[Union[Var[Union[str, int]], Union[str, int]]]=None, wrapClassName: Optional[Union[Var[str], str]]=None, zIndex: Optional[Union[Var[int], int]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, after_close: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, after_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_ok: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Modal':
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

class Confirm(FakeComponentMixin, JsValue):
    config: Optional[Var[dict]]

    @property
    def config_item(self) -> Optional[ExStateItem]:
        ...

    @property
    def uid(self) -> str:
        ...

    def get_name(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    def serialize(self) -> str:
        ...
modal = Modal.create
confirm = Confirm