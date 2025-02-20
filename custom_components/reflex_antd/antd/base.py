from typing import Optional, Union, Dict
from types import SimpleNamespace
from functools import lru_cache

import reflex as rx
from reflex import Var, Component
from reflex.components.tags import Tag
from reflex.vars import VarData
from reflex.utils import imports


from .. import base
from ..base import AntdComponent, AntdBaseComponent, ContainVar, JsValue
from ..constant import SizeType


AntdNextTheme = 'AntdNextTheme'
next_theme_var_data = VarData(  # type: ignore
    imports={
        f"next-themes": {imports.ImportVar(tag="useTheme")},
        "react": {imports.ImportVar(tag="useContext")},
        "antd": {imports.ImportVar(tag="theme", alias=AntdNextTheme)}
    },
    hooks={
        f"const nextTheme = useTheme()": None,
    },
)
next_theme_var = Var(
    _js_expr='nextTheme.theme',
    _var_type="str",
    _var_data=next_theme_var_data,
)
light_theme_var = Var(
    _js_expr=f'{AntdNextTheme}.defaultAlgorithm',
    _var_data=next_theme_var_data,
)
dark_theme_var = Var(
    _js_expr=f'{AntdNextTheme}.darkAlgorithm',
    _var_data=next_theme_var_data,
)


def theme(**kwargs):
    return ContainVar.create(**kwargs)


class DayJS(JsValue):
    def serialize(self) -> str:
        if isinstance(self.value, list):
            return f"""dayjs({[f"'{v}', " for v in self.value]})"""
        return f"dayjs('{self.value}')"


dayjs = DayJS


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
    _is_root: bool

    @classmethod
    def create(cls, *children, is_root: bool = False, **props) -> Component:
        """Create a new ConfigProvider component.

        Returns:
            A new ConfigProvider component.
        """
        rs = super().create(
            *children,
            **props
        )
        rs._is_root = is_root
        return rs

    def _render(self, *args, **kwargs) -> Tag:
        rs = super()._render(*args, **kwargs)
        return rs

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("/utils/theme.js", []).append(
            imports.ImportVar(tag="theme", is_default=True),
        )
        _imports.setdefault("@ant-design/cssinjs", []).append(
            imports.ImportVar(tag="Theme", alias='AntdTheme'),
        )
        return _imports

    # @staticmethod
    # @lru_cache(maxsize=None)
    # def _get_app_wrap_components(self) -> dict[tuple[int, str], Component]:
    #     """ support app router """
    #     if self._is_root and base.APP_ROUTER:
    #         return {
    #             (170, "AntdRegistryProvider"): antd_registry_provider(),
    #         }
    #     else:
    #         return {}


class AntdRegistryProvider(AntdBaseComponent):
    library = "@ant-design/nextjs-registry"
    tag = "AntdRegistry"


class AntdApp(AntdComponent):
    tag = "App"
    alias = "AntdApp"

    component: Optional[Var[Union[bool, str]]]
    message: Optional[Var[Union[dict, ContainVar]]]
    notification: Optional[Var[Union[dict, ContainVar]]]


config_provider = ConfigProvider.create
antd_registry_provider = AntdRegistryProvider.create
antd_app = AntdApp.create

