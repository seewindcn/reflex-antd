"""Stub file for custom_components/reflex_antd/antd/avatar.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload
from reflex.vars import Var, BaseVar
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any
from reflex import Component, Var
from ..base import AntdComponent, ContainVar

class Avatar(AntdComponent):
    def get_event_triggers(self) -> Dict[str, Any]: ...
    @overload
    @classmethod
    def create(  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore
        cls,
        *children,
        alt: Optional[Union[Var[str], str]] = None,
        gap: Optional[Union[Var[int], int]] = None,
        icon: Optional[Union[Var[Union[Component, str]], str, Component]] = None,
        shape: Optional[Union[Var[str], str]] = None,
        size: Optional[Union[Var[Union[Dict, int, str]], str, int, Dict]] = None,
        src: Optional[Union[Var[Union[Component, str]], str, Component]] = None,
        src_set: Optional[Union[Var[str], str]] = None,
        draggable: Optional[Union[Var[bool], bool]] = None,
        _custom_components: Optional[Set[CustomComponent]] = None,
        _ex_hooks: Optional[List[ContainVar]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_error: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "Avatar":
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

class AvatarGroup(AntdComponent):
    @overload
    @classmethod
    def create(  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore
        cls,
        *children,
        max_count: Optional[Union[Var[int], int]] = None,
        max_popover_placement: Optional[Union[Var[str], str]] = None,
        max_popover_trigger: Optional[Union[Var[str], str]] = None,
        max_style: Optional[Union[Var[Dict], Dict]] = None,
        size: Optional[Union[Var[Union[Dict, int, str]], str, int, Dict]] = None,
        shape: Optional[Union[Var[str], str]] = None,
        _custom_components: Optional[Set[CustomComponent]] = None,
        _ex_hooks: Optional[List[ContainVar]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "AvatarGroup":
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

avatar = Avatar.create
avatar_group = AvatarGroup.create
