from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import uuid
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from ..base import AntdComponent, ContainVar, JsValue, ReactNode, js_value, memo_never_no_recursive, memo_always_no_recursive
from ..constant import AlignType, DirectionType, SizeType, VariantType

class Form(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, colon: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, fields: Optional[Union[Var[ContainVar], ContainVar]]=None, form: Optional[Union[Var[str], str]]=None, initial_values: Optional[Union[Var[Dict], Dict]]=None, label_align: Optional[Union[Var[Literal['start', 'end', 'center', 'baseline', 'left', 'right']], Literal['start', 'end', 'center', 'baseline', 'left', 'right']]]=None, label_wrap: Optional[Union[Var[bool], bool]]=None, label_col: Optional[Union[Var[Dict], Dict]]=None, layout: Optional[Union[Var[Literal['vertical', 'horizontal', 'inline']], Literal['vertical', 'horizontal', 'inline']]]=None, name: Optional[Union[Var[str], str]]=None, preserve: Optional[Union[Var[bool], bool]]=None, required_mark: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, scrollTo_first_error: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, validate_messages: Optional[Union[Var[Dict], Dict]]=None, validate_trigger: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, wrapper_col: Optional[Union[Var[Dict], Dict]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_fields_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_finish: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_finish_failed: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_values_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Form':
        """"""
        ...

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

class FormItem(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, colon: Optional[Union[Var[bool], bool]]=None, dependencies: Optional[Union[Var[List[Union[str, int, List[Union[str, int]]]]], List[Union[str, int, List[Union[str, int]]]]]]=None, extra: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, getValue_from_event: Optional[Union[Var[JsValue], JsValue]]=None, get_value_props: Optional[Union[Var[JsValue], JsValue]]=None, has_feedback: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, help: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, hidden: Optional[Union[Var[bool], bool]]=None, html_for: Optional[Union[Var[str], str]]=None, initial_value: Optional[Union[Var[str], str]]=None, label: Optional[Union[Var[str], str]]=None, label_align: Optional[Union[Var[Literal['start', 'end', 'center', 'baseline', 'left', 'right']], Literal['start', 'end', 'center', 'baseline', 'left', 'right']]]=None, label_col: Optional[Union[Var[Dict], Dict]]=None, message_variables: Optional[Union[Var[JsValue], JsValue]]=None, name: Optional[Union[Var[Union[str, int, List[Union[str, int]]]], Union[str, int, List[Union[str, int]]]]]=None, normalize: Optional[Union[Var[JsValue], JsValue]]=None, no_style: Optional[Union[Var[bool], bool]]=None, preserve: Optional[Union[Var[bool], bool]]=None, required: Optional[Union[Var[bool], bool]]=None, rules: Optional[Union[Var[List[Dict]], List[Dict]]]=None, should_update: Optional[Union[Var[bool], bool]]=None, tooltip: Optional[Union[Var[Union[Component, ContainVar]], Union[Component, ContainVar]]]=None, trigger: Optional[Union[Var[str], str]]=None, validate_debounce: Optional[Union[Var[float], float]]=None, validate_first: Optional[Union[Var[Union[bool, str]], Union[bool, str]]]=None, validate_status: Optional[Union[Var[str], str]]=None, validate_trigger: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, value_prop_name: Optional[Union[Var[str], str]]=None, wrapper_col: Optional[Union[Var[Dict], Dict]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'FormItem':
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

class FormList(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, initial_value: Optional[Union[Var[List], List]]=None, name: Optional[Union[Var[Union[str, int, List[Union[str, int]]]], Union[str, int, List[Union[str, int]]]]]=None, rules: Optional[Union[Var[ContainVar], ContainVar]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'FormList':
        """Create the component.

        Args:
            *children: The children of the component.
            initial_value: children: Optional[Var[JsValue]]
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

class FormProvider(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_form_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_form_finish: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'FormProvider':
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
form = Form.create
form_item = FormItem.create
form_list = FormList.create
form_provider = FormProvider.create

def modal_form(*children, modal_config=None, form_id: str=None, **props) -> Component:
    ...

def confirm_form(*children, confirm_config=None, form_id: str=None, **props) -> JsValue:
    ...