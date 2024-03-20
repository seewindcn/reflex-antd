from functools import lru_cache

import reflex as rx
from reflex import Component, Var
from reflex.utils import imports


APP_ROUTER = False

class AntdComponent(Component):
    """A component that wraps a Chakra component."""

    library = "antd"

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (160, "AntdProvider"): antd_provider,
        }


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

    if APP_ROUTER:
        @staticmethod
        @lru_cache(maxsize=None)
        def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
            """ support app router """
            return {
                (170, "AntdRegistryProvider"): antd_registry_provider,
            }


class AntdRegistryProvider(Component):
    library = "@ant-design/nextjs-registry"
    tag = "AntdRegistry"


antd_provider = AntdProvider.create()
antd_registry_provider = AntdRegistryProvider.create()
