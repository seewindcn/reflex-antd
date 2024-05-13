from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports
from ..base import AntdComponent, ContainVar, JsNode, ReactNode
from ..constant import StatusType, SizeType

class Tree(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, allow_drop: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, auto_expand_parent: Optional[Union[Var[bool], bool]]=None, block_node: Optional[Union[Var[bool], bool]]=None, checkable: Optional[Union[Var[bool], bool]]=None, checked_keys: Optional[Union[Var[Union[List, Dict]], Union[List, Dict]]]=None, check_strictly: Optional[Union[Var[bool], bool]]=None, default_checked_keys: Optional[Union[Var[List[str]], List[str]]]=None, default_expand_all: Optional[Union[Var[bool], bool]]=None, default_expanded_keys: Optional[Union[Var[List[str]], List[str]]]=None, default_expand_parent: Optional[Union[Var[bool], bool]]=None, default_selected_keys: Optional[Union[Var[List[str]], List[str]]]=None, disabled: Optional[Union[Var[bool], bool]]=None, draggable: Optional[Union[Var[Union[bool, JsValue, JsEvent, ContainVar]], Union[bool, JsValue, JsEvent, ContainVar]]]=None, expanded_keys: Optional[Union[Var[List[str]], List[str]]]=None, field_names: Optional[Union[Var[Dict], Dict]]=None, filter_tree_node: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, height: Optional[Union[Var[int], int]]=None, icon: Optional[Union[Var[Union[str, Component, JsValue, JsEvent]], Union[str, Component, JsValue, JsEvent]]]=None, load_data: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, loaded_keys: Optional[Union[Var[List[str]], List[str]]]=None, multiple: Optional[Union[Var[bool], bool]]=None, root_style: Optional[Union[Var[Dict], Dict]]=None, selectable: Optional[Union[Var[bool], bool]]=None, selected_keys: Optional[Union[Var[List[str]], List[str]]]=None, show_icon: Optional[Union[Var[bool], bool]]=None, show_line: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, switcher_icon: Optional[Union[Var[Union[str, Component, JsValue, JsEvent]], Union[str, Component, JsValue, JsEvent]]]=None, title_render: Optional[Union[Var[Union[JsValue, JsEvent]], Union[JsValue, JsEvent]]]=None, tree_data: Optional[Union[Var[List[Dict]], List[Dict]]]=None, virtual: Optional[Union[Var[bool], bool]]=None, expand_action: Optional[Union[Var[Union[bool, str]], Union[bool, str]]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, filter_tree_node: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, load_data: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_check: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drag_end: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drag_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drag_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drag_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drag_start: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drop: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_load: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_right_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Tree':
        """Create the component.

        Args:
            *children: The children of the component.
            expand_action: DirectoryTree
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
tree = Tree.create