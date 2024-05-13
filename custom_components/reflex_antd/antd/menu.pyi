from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Type, Dict, List, Any, Iterator
from reflex import Component, Var, EventChain, Base
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, ReactNode, pydantic
from ..constant import ThemeType, DirectionType, TriggerType

class MenuItem(pydantic.BaseModel):
    key: str
    label: str
    icon: Component
    children: Optional[List['MenuItem']]

class OnSelectEvent(Base):
    item: Any
    key: Any
    keyPath: Any
    selectedKeys: List[str]

class Menu(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, default_open_keys: Optional[Union[Var[List[str]], List[str]]]=None, default_selected_keys: Optional[Union[Var[List[str]], List[str]]]=None, expand_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, force_sub_menu_render: Optional[Union[Var[bool], bool]]=None, inline_collapsed: Optional[Union[Var[bool], bool]]=None, inline_indent: Optional[Union[Var[bool], bool]]=None, items: Optional[Union[Var[Union[ContainVar, list]], Union[ContainVar, list]]]=None, mode: Optional[Union[Var[Literal['vertical', 'horizontal', 'inline']], Literal['vertical', 'horizontal', 'inline']]]=None, multiple: Optional[Union[Var[bool], bool]]=None, open_keys: Optional[Union[Var[List[str]], List[str]]]=None, overflowed_indicator: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, selectable: Optional[Union[Var[bool], bool]]=None, selected_keys: Optional[Union[Var[List[str]], List[str]]]=None, sub_menu_close_delay: Optional[Union[Var[float], float]]=None, sub_menu_open_delay: Optional[Union[Var[float], float]]=None, theme: Optional[Union[Var[Literal['light', 'dark']], Literal['light', 'dark']]]=None, trigger_sub_menu_action: Optional[Union[Var[Literal['click', 'hover', 'focus', 'contextMenu']], Literal['click', 'hover', 'focus', 'contextMenu']]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_deselect: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_open_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Menu':
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
menu = Menu.create