from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict
from types import SimpleNamespace
from functools import lru_cache
import reflex as rx
from reflex import Var, Component
from reflex.vars import BaseVar, VarData
from reflex.utils import imports
from .. import base
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType
next_theme_var_data = VarData(imports={f'next-themes': {imports.ImportVar(tag='useTheme')}, 'react': {imports.ImportVar(tag='useContext')}, 'antd': {imports.ImportVar(tag='theme', alias='AntdTheme')}}, hooks={f'const nextTheme = useTheme()': None})
next_theme_var = BaseVar(_var_name='nextTheme.theme', _var_type='str', _var_data=next_theme_var_data)
light_theme_var = BaseVar(_var_name='AntdTheme.defaultAlgorithm')
dark_theme_var = BaseVar(_var_name='AntdTheme.darkAlgorithm')

def theme(**kwargs):
    ...

class Locale(JsValue):

    @property
    def lang(self) -> str:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

class ConfigProvider(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, auto_insert_space_in_button: Optional[Union[Var[bool], bool]]=None, component_disabled: Optional[Union[Var[bool], bool]]=None, component_size: Optional[Union[Var[Literal['default', 'small', 'medium', 'middle', 'large']], Literal['default', 'small', 'medium', 'middle', 'large']]]=None, csp: Optional[Union[Var[ContainVar], ContainVar]]=None, direction: Optional[Union[Var[str], str]]=None, get_popup_container: Optional[Union[Var[JsValue], JsValue]]=None, get_target_container: Optional[Union[Var[JsValue], JsValue]]=None, icon_prefix_cls: Optional[Union[Var[str], str]]=None, locale: Optional[Union[Var[Locale], Locale]]=None, popup_match_select_width: Optional[Union[Var[Union[bool, int]], Union[bool, int]]]=None, popup_overflow: Optional[Union[Var[str], str]]=None, prefix_cls: Optional[Union[Var[str], str]]=None, render_empty: Optional[Union[Var[JsValue], JsValue]]=None, theme: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, virtual: Optional[Union[Var[bool], bool]]=None, warning: Optional[Union[Var[Dict], Dict]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'ConfigProvider':
        """Create a new ConfigProvider component.

        Returns:
            A new ConfigProvider component.
        """
        ...

class AntdRegistryProvider(Component):

    @overload
    @classmethod
    def create(cls, *children, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'AntdRegistryProvider':
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
config_provider = ConfigProvider.create
antd_registry_provider = AntdRegistryProvider.create