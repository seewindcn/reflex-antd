from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Tuple
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import DatePickerModeType, DatePickerType, SizeType, PlacementType, StatusType, VariantType
from .base import Locale

class DayJS(JsValue):

    def serialize(self) -> str:
        ...

class BaseDatePicker(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_clear: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, date_render: Optional[Union[Var[JsValue], JsValue]]=None, cell_render: Optional[Union[Var[JsValue], JsValue]]=None, components: Optional[Union[Var[Union[str, Component, list, dict, ContainVar]], Union[str, Component, list, dict, ContainVar]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, disabled_date: Optional[Union[Var[JsValue], JsValue]]=None, format: Optional[Union[Var[ContainVar], ContainVar]]=None, order: Optional[Union[Var[bool], bool]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, preserve_invalidOn_blur: Optional[Union[Var[bool], bool]]=None, getPopup_container: Optional[Union[Var[JsValue], JsValue]]=None, input_readOnly: Optional[Union[Var[bool], bool]]=None, locale: Optional[Union[Var[Locale], Locale]]=None, min_date: Optional[Union[Var[JsValue], JsValue]]=None, max_date: Optional[Union[Var[JsValue], JsValue]]=None, mode: Optional[Union[Var[Literal['time', 'date', 'month', 'year', 'decade']], Literal['time', 'date', 'month', 'year', 'decade']]]=None, need_confirm: Optional[Union[Var[bool], bool]]=None, next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, open: Optional[Union[Var[bool], bool]]=None, panel_render: Optional[Union[Var[JsValue], JsValue]]=None, picker: Optional[Union[Var[Literal['date', 'week', 'month', 'quarter', 'year']], Literal['date', 'week', 'month', 'quarter', 'year']]]=None, placeholder: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, popup_style: Optional[Union[Var[ContainVar], ContainVar]]=None, presets: Optional[Union[Var[ContainVar], ContainVar]]=None, prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, suffix_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_panel_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'BaseDatePicker':
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

class DatePicker(BaseDatePicker):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, default_picker_value: Optional[Union[Var[JsValue], JsValue]]=None, default_value: Optional[Union[Var[ContainVar], ContainVar]]=None, disabled_time: Optional[Union[Var[JsValue], JsValue]]=None, format: Optional[Union[Var[ContainVar], ContainVar]]=None, multiple: Optional[Union[Var[bool], bool]]=None, picker_value: Optional[Union[Var[ContainVar], ContainVar]]=None, render_extra_footer: Optional[Union[Var[JsValue], JsValue]]=None, show_now: Optional[Union[Var[bool], bool]]=None, show_time: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, show_week: Optional[Union[Var[bool], bool]]=None, value: Optional[Union[Var[ContainVar], ContainVar]]=None, allow_clear: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, date_render: Optional[Union[Var[JsValue], JsValue]]=None, cell_render: Optional[Union[Var[JsValue], JsValue]]=None, components: Optional[Union[Var[Union[str, Component, list, dict, ContainVar]], Union[str, Component, list, dict, ContainVar]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, disabled_date: Optional[Union[Var[JsValue], JsValue]]=None, order: Optional[Union[Var[bool], bool]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, preserve_invalidOn_blur: Optional[Union[Var[bool], bool]]=None, getPopup_container: Optional[Union[Var[JsValue], JsValue]]=None, input_readOnly: Optional[Union[Var[bool], bool]]=None, locale: Optional[Union[Var[Locale], Locale]]=None, min_date: Optional[Union[Var[JsValue], JsValue]]=None, max_date: Optional[Union[Var[JsValue], JsValue]]=None, mode: Optional[Union[Var[Literal['time', 'date', 'month', 'year', 'decade']], Literal['time', 'date', 'month', 'year', 'decade']]]=None, need_confirm: Optional[Union[Var[bool], bool]]=None, next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, open: Optional[Union[Var[bool], bool]]=None, panel_render: Optional[Union[Var[JsValue], JsValue]]=None, picker: Optional[Union[Var[Literal['date', 'week', 'month', 'quarter', 'year']], Literal['date', 'week', 'month', 'quarter', 'year']]]=None, placeholder: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, popup_style: Optional[Union[Var[ContainVar], ContainVar]]=None, presets: Optional[Union[Var[ContainVar], ContainVar]]=None, prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, suffix_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_ok: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_panel_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'DatePicker':
        """Create the component.

        Args:
            *children: The children of the component.
            show_week: showTime.defaultValue
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

class RangePicker(BaseDatePicker):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_empty: Optional[Union[Var[Tuple[bool, bool]], Tuple[bool, bool]]]=None, cell_render: Optional[Union[Var[JsValue], JsValue]]=None, date_render: Optional[Union[Var[JsValue], JsValue]]=None, default_picker_value: Optional[Union[Var[ContainVar], ContainVar]]=None, default_value: Optional[Union[Var[ContainVar], ContainVar]]=None, disabled: Optional[Union[Var[Tuple[bool, bool]], Tuple[bool, bool]]]=None, disabled_time: Optional[Union[Var[JsValue], JsValue]]=None, format: Optional[Union[Var[ContainVar], ContainVar]]=None, id: Optional[Union[Var[Dict[str, str]], Dict[str, str]]]=None, picker_value: Optional[Union[Var[ContainVar], ContainVar]]=None, presets: Optional[Union[Var[ContainVar], ContainVar]]=None, render_extra_footer: Optional[Union[Var[JsValue], JsValue]]=None, separator: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, show_time: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, value: Optional[Union[Var[ContainVar], ContainVar]]=None, allow_clear: Optional[Union[Var[bool], bool]]=None, auto_focus: Optional[Union[Var[bool], bool]]=None, components: Optional[Union[Var[Union[str, Component, list, dict, ContainVar]], Union[str, Component, list, dict, ContainVar]]]=None, disabled_date: Optional[Union[Var[JsValue], JsValue]]=None, order: Optional[Union[Var[bool], bool]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, preserve_invalidOn_blur: Optional[Union[Var[bool], bool]]=None, getPopup_container: Optional[Union[Var[JsValue], JsValue]]=None, input_readOnly: Optional[Union[Var[bool], bool]]=None, locale: Optional[Union[Var[Locale], Locale]]=None, min_date: Optional[Union[Var[JsValue], JsValue]]=None, max_date: Optional[Union[Var[JsValue], JsValue]]=None, mode: Optional[Union[Var[Literal['time', 'date', 'month', 'year', 'decade']], Literal['time', 'date', 'month', 'year', 'decade']]]=None, need_confirm: Optional[Union[Var[bool], bool]]=None, next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, open: Optional[Union[Var[bool], bool]]=None, panel_render: Optional[Union[Var[JsValue], JsValue]]=None, picker: Optional[Union[Var[Literal['date', 'week', 'month', 'quarter', 'year']], Literal['date', 'week', 'month', 'quarter', 'year']]]=None, placeholder: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, popup_style: Optional[Union[Var[ContainVar], ContainVar]]=None, prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, suffix_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_next_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, super_prev_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, variant: Optional[Union[Var[Literal['outlined', 'borderless', 'filled']], Literal['outlined', 'borderless', 'filled']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_calendar_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_panel_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'RangePicker':
        """Create the component.

        Args:
            *children: The children of the component.
            value: showTime.defaultValue
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
dayjs = DayJS
date_picker = DatePicker.create
range_picker = RangePicker.create