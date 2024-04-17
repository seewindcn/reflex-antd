from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType, VariantType

class Input(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, addon_after: Optional[Union[Var[Component], Component]]=None, addon_before: Optional[Union[Var[Component], Component]]=None, allow_clear: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, count: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, default_value: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, id: Optional[Union[Var[str], str]]=None, max_length: Optional[Union[Var[int], int]]=None, prefix: Optional[Union[Var[Component], Component]]=None, show_count: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, suffix: Optional[Union[Var[Component], Component]]=None, type: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[str], str]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, placeholder: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_press_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Input':
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

class TextArea(Input):

    @overload
    @classmethod
    def create(cls, *children, auto_size: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, addon_after: Optional[Union[Var[Component], Component]]=None, addon_before: Optional[Union[Var[Component], Component]]=None, allow_clear: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, count: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, default_value: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, id: Optional[Union[Var[str], str]]=None, max_length: Optional[Union[Var[int], int]]=None, prefix: Optional[Union[Var[Component], Component]]=None, show_count: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, suffix: Optional[Union[Var[Component], Component]]=None, type: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[str], str]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, placeholder: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_press_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TextArea':
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

class Search(Input):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, enter_button: Optional[Union[Var[Component], Component]]=None, loading: Optional[Union[Var[bool], bool]]=None, addon_after: Optional[Union[Var[Component], Component]]=None, addon_before: Optional[Union[Var[Component], Component]]=None, allow_clear: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, count: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, default_value: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, id: Optional[Union[Var[str], str]]=None, max_length: Optional[Union[Var[int], int]]=None, prefix: Optional[Union[Var[Component], Component]]=None, show_count: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, suffix: Optional[Union[Var[Component], Component]]=None, type: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[str], str]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, placeholder: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_press_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_search: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Search':
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

class Password(Input):

    @overload
    @classmethod
    def create(cls, *children, icon_render: Optional[Union[Var[JsValue], JsValue]]=None, visibility_toggle: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, addon_after: Optional[Union[Var[Component], Component]]=None, addon_before: Optional[Union[Var[Component], Component]]=None, allow_clear: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, count: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, default_value: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, id: Optional[Union[Var[str], str]]=None, max_length: Optional[Union[Var[int], int]]=None, prefix: Optional[Union[Var[Component], Component]]=None, show_count: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, suffix: Optional[Union[Var[Component], Component]]=None, type: Optional[Union[Var[str], str]]=None, value: Optional[Union[Var[str], str]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, placeholder: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_press_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Password':
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
input = Input.create
text_area = TextArea.create
search = Search.create
password = Password.create