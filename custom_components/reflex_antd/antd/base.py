from typing import Optional, Union, Dict
from functools import lru_cache

import reflex as rx
from reflex import Var, Component
from reflex.utils import imports


from .. import base
from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType


class Locale(JsValue):

    @property
    def lang(self) -> str:
        return self.value.replace("_", "")

    def serialize(self) -> str:
        return self.lang

    def get_imports(self) -> imports.ImportDict:
        return {
            f'antd/locale/{self.value}': [imports.ImportVar(tag=self.lang, install=False, is_default=True)],
        }


class ConfigProvider(AntdComponent):
    """Top level antd provider must be included in any app using antd components."""

    tag = "ConfigProvider"
    alias = "AntdConfigProvider"

    auto_insert_space_in_button: Optional[Var[bool]]
    component_disabled: Optional[Var[bool]]
    component_size: Optional[Var[SizeType]]
    csp: Optional[Var[ContainVar]]
    direction: Optional[Var[str]]
    get_popup_container: Optional[Var[JsValue]]
    get_target_container: Optional[Var[JsValue]]
    icon_prefix_cls: Optional[Var[str]]
    locale: Optional[Var[Locale]]
    popup_match_select_width: Optional[Var[Union[bool, int]]]
    popup_overflow: Optional[Var[str]]
    prefix_cls: Optional[Var[str]]
    render_empty: Optional[Var[JsValue]]
    theme: Optional[Var[Union[Dict, ContainVar]]]
    virtual: Optional[Var[bool]]
    warning: Optional[Var[Dict]]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a new ConfigProvider component.

        Returns:
            A new ConfigProvider component.
        """
        if 'theme' not in props:
            theme = Var.create('theme.styles.global.body.antd', _var_is_local=False)
            props['theme'] = theme

        return super().create(
            *children,
            **props
        )

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("/utils/theme.js", []).append(
            imports.ImportVar(tag="theme", is_default=True),
        )
        return _imports

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        """ support app router """
        if base.APP_ROUTER:
            return {
                (170, "AntdRegistryProvider"): antd_registry_provider(),
            }
        else:
            return {}


class AntdRegistryProvider(Component):
    library = "@ant-design/nextjs-registry"
    tag = "AntdRegistry"


config_provider = ConfigProvider.create
antd_registry_provider = AntdRegistryProvider.create

