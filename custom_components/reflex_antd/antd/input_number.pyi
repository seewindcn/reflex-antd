from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType

class InputNumber(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, addon_after: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, addon_before: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, change_on_blur: Optional[Union[Var[bool], bool]]=None, change_on_wheel: Optional[Union[Var[bool], bool]]=None, controls: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, decimal_separator: Optional[Union[Var[str], str]]=None, placeholder: Optional[Union[Var[str], str]]=None, default_value: Optional[Union[Var[int], int]]=None, disabled: Optional[Union[Var[bool], bool]]=None, formatter: Optional[Union[Var[JsValue], JsValue]]=None, keyboard: Optional[Union[Var[bool], bool]]=None, max: Optional[Union[Var[int], int]]=None, min: Optional[Union[Var[int], int]]=None, parser: Optional[Union[Var[JsValue], JsValue]]=None, precision: Optional[Union[Var[int], int]]=None, read_only: Optional[Union[Var[bool], bool]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, prefix: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, step: Optional[Union[Var[Union[int, str]], Union[int, str]]]=None, string_mode: Optional[Union[Var[bool], bool]]=None, value: Optional[Union[Var[int], int]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_press_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_step: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'InputNumber':
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
input_number = InputNumber.create