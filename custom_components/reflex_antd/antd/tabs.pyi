from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Tuple
from dataclasses import dataclass
from reflex import Component, Var, Base
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType, PlacementType, TabsType

@dataclass(frozen=True)
class TabItem:
    close_icon: Optional[Var[ReactNode]]
    destroy_inactive_tab_pane: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    force_render: Optional[Var[bool]]
    key: Optional[Union[str, Var[str]]]
    label: Optional[Union[ReactNode, Var[ReactNode]]]
    icon: Optional[Var[ReactNode]]
    children: Optional[Union[ReactNode, Var[ReactNode]]]
    closable: Optional[Var[bool]]

class Tabs(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, active_key: Optional[Union[Var[str], str]]=None, add_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, animated: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, centered: Optional[Union[Var[bool], bool]]=None, default_active_key: Optional[Union[Var[str], str]]=None, hide_add: Optional[Union[Var[bool], bool]]=None, indicator: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, items: Optional[Union[Var[Union[ContainVar, List]], Union[ContainVar, List]]]=None, more_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, remove_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, popup_class_name: Optional[Union[Var[str], str]]=None, render_tab_bar: Optional[Union[Var[JsValue], JsValue]]=None, size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, tab_bar_extra_content: Optional[Union[Var[Union[str, Component, ContainVar]], Union[str, Component, ContainVar]]]=None, tab_bar_gutter: Optional[Union[Var[int], int]]=None, tab_bar_style: Optional[Union[Var[Dict], Dict]]=None, tab_position: Optional[Union[Var[Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']], Literal['start', 'end', 'bottom', 'bottomLeft', 'bottomRight', 'top', 'topLeft', 'topRight']]]=None, destroy_inactive_tab_pane: Optional[Union[Var[bool], bool]]=None, type: Optional[Union[Var[Literal['line', 'card', 'editable-card']], Literal['line', 'card', 'editable-card']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_edit: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_tab_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_tab_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Tabs':
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
tabs = Tabs.create
tab_item = TabItem