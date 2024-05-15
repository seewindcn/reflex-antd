from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import ColorFormatType, SizeType, PlacementType, TriggerType

class ColorPicker(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_clear: Optional[Union[Var[bool], bool]]=None, arrow: Optional[Union[Var[bool], bool]]=None, default_value: Optional[Union[Var[str], str]]=None, default_format: Optional[Union[Var[str], str]]=None, disabled: Optional[Union[Var[bool], bool]]=None, disabled_alpha: Optional[Union[Var[bool], bool]]=None, destroy_tooltip_on_hide: Optional[Union[Var[bool], bool]]=None, format: Optional[Union[Var[Literal['rgb', 'hex', 'hsb']], Literal['rgb', 'hex', 'hsb']]]=None, open: Optional[Union[Var[bool], bool]]=None, presets: Optional[Union[Var[ContainVar], ContainVar]]=None, placement: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, panel_render: Optional[Union[Var[JsValue], JsValue]]=None, show_text: Optional[Union[Var[Union[bool, JsValue]], Union[bool, JsValue]]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, trigger: Optional[Union[Var[Literal['click', 'hover', 'focus', 'contextMenu']], Literal['click', 'hover', 'focus', 'contextMenu']]]=None, value: Optional[Union[Var[str], str]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change_complete: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_clear: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_format_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'ColorPicker':
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
color_picker = ColorPicker.create