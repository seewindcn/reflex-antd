from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Tuple
from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import TypographyTextType

class TypographyBase(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, code: Optional[Union[Var[bool], bool]]=None, copyable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, delete: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, editable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, ellipsis: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, mark: Optional[Union[Var[bool], bool]]=None, italic: Optional[Union[Var[bool], bool]]=None, type: Optional[Union[Var[Literal['secondary', 'success', 'warning', 'danger']], Literal['secondary', 'success', 'warning', 'danger']]]=None, underline: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, copyable.on_copy: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_end: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_start: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_ellipsis: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TypographyBase':
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

class TypographyText(TypographyBase):

    @overload
    @classmethod
    def create(cls, *children, keyboard: Optional[Union[Var[bool], bool]]=None, strong: Optional[Union[Var[bool], bool]]=None, code: Optional[Union[Var[bool], bool]]=None, copyable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, delete: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, editable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, ellipsis: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, mark: Optional[Union[Var[bool], bool]]=None, italic: Optional[Union[Var[bool], bool]]=None, type: Optional[Union[Var[Literal['secondary', 'success', 'warning', 'danger']], Literal['secondary', 'success', 'warning', 'danger']]]=None, underline: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, copyable.on_copy: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_end: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_start: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_ellipsis: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TypographyText':
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

class TypographyTitle(TypographyBase):

    @overload
    @classmethod
    def create(cls, *children, level: Optional[Union[Var[int], int]]=None, code: Optional[Union[Var[bool], bool]]=None, copyable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, delete: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, editable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, ellipsis: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, mark: Optional[Union[Var[bool], bool]]=None, italic: Optional[Union[Var[bool], bool]]=None, type: Optional[Union[Var[Literal['secondary', 'success', 'warning', 'danger']], Literal['secondary', 'success', 'warning', 'danger']]]=None, underline: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, copyable.on_copy: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_end: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_start: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_ellipsis: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TypographyTitle':
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

class TypographyParagraph(TypographyBase):

    @overload
    @classmethod
    def create(cls, *children, strong: Optional[Union[Var[bool], bool]]=None, code: Optional[Union[Var[bool], bool]]=None, copyable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, delete: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, editable: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, ellipsis: Optional[Union[Var[Union[bool, ContainVar]], Union[bool, ContainVar]]]=None, mark: Optional[Union[Var[bool], bool]]=None, italic: Optional[Union[Var[bool], bool]]=None, type: Optional[Union[Var[Literal['secondary', 'success', 'warning', 'danger']], Literal['secondary', 'success', 'warning', 'danger']]]=None, underline: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, copyable.on_copy: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_cancel: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_end: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, editable.on_start: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_ellipsis: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, ellipsis.on_expand: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'TypographyParagraph':
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
typography_text = TypographyText.create
typography_title = TypographyTitle.create
typography_paragraph = TypographyParagraph.create