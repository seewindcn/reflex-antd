"""Stub file for custom_components/reflex_antd/antd/space.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict
from reflex import Component, Var
from ..base import AntdComponent, ContainVar

class Space(AntdComponent):
    @overload
    @classmethod
    def create(  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore
        cls,
        *children,
        align: Optional[
            Union[
                Var[Literal["start", "end", "center", "baseline", "left", "right"]],
                Literal["start", "end", "center", "baseline", "left", "right"],
            ]
        ] = None,
        class_names: Optional[Union[Var[Dict], Dict]] = None,
        direction: Optional[
            Union[
                Var[Literal["vertical", "horizontal", "inline"]],
                Literal["vertical", "horizontal", "inline"],
            ]
        ] = None,
        size: Optional[
            Union[
                Var[Literal["default", "small", "medium", "middle", "large"]],
                Literal["default", "small", "medium", "middle", "large"],
            ]
        ] = None,
        split: Optional[Union[Var[Union[Component, str]], str, Component]] = None,
        styles: Optional[Union[Var[Dict], Dict]] = None,
        wrap: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "Space":
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

class SpaceCompact(AntdComponent):
    @overload
    @classmethod
    def create(  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore  # type: ignore
        cls,
        *children,
        block: Optional[Union[Var[bool], bool]] = None,
        direction: Optional[
            Union[
                Var[Literal["vertical", "horizontal", "inline"]],
                Literal["vertical", "horizontal", "inline"],
            ]
        ] = None,
        size: Optional[
            Union[
                Var[Literal["default", "small", "medium", "middle", "large"]],
                Literal["default", "small", "medium", "middle", "large"],
            ]
        ] = None,
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
    ) -> "SpaceCompact":
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

space = Space.create
space_compact = SpaceCompact.create
