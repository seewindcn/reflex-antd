from os import path
from functools import lru_cache
from typing import Any

import reflex as rx
from reflex import Component, Var
from reflex.utils import imports
from reflex.vars import BaseVar

my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, '.templates')

APP_ROUTER = False


class ExVar(BaseVar):
    _var_value: Any

    @classmethod
    def create(
            cls, value: Any, _var_is_local: bool = True, _var_is_string: bool = False
    ) -> Var | None:
        v: BaseVar = super().create(value, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        return cls(
            _var_name=v._var_name,
            _var_type=v._var_type,
            _var_is_local=v._var_is_local,
            _var_is_string=v._var_is_string,
            _var_data=v._var_data,
            _var_value=value,
        )


class ContainVar(ExVar):

    @property
    def _var_full_name(self) -> str:
        return self._var_name


class AntdBaseMixin:
    def _get_style(self) -> dict:
        """Get the style for the component.

        Returns:
            The dictionary of the component style as value and the style notation as key.
        """
        return {"style": self.style}


class AntdComponent(AntdBaseMixin, Component):
    """A component that wraps a Chakra component."""

    library = "antd"

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (160, "AntdProvider"): antd_provider,
        }


class AntdSubComponent(AntdBaseMixin, Component):
    def _get_imports(self) -> imports.ImportDict:
        return {}


class AntdProvider(AntdComponent):
    """Top level antd provider must be included in any app using antd components."""

    tag = "ConfigProvider"
    alias = "AntdConfigProvider"

    theme: Var[str]

    @classmethod
    def create(cls) -> Component:
        """Create a new AntdProvider component.

        Returns:
            A new AntdProvider component.
        """
        return super().create(
            theme=Var.create("theme", _var_is_local=False),
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
        if APP_ROUTER:
            return {
                (170, "AntdRegistryProvider"): antd_registry_provider,
            }
        else:
            return {}


class AntdRegistryProvider(Component):
    library = "@ant-design/nextjs-registry"
    tag = "AntdRegistry"


antd_provider = AntdProvider.create()
antd_registry_provider = AntdRegistryProvider.create()


def patch_all():
    from reflex import constants
    from reflex.compiler import templates

    constants.Templates.Dirs.JINJA_TEMPLATE = [path.join(template_path, 'jinja'),
                                               constants.Templates.Dirs.JINJA_TEMPLATE]

    templates.DOCUMENT_ROOT = templates.get_template("web/pages/_document.js.jinja2")
