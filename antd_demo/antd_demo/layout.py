from typing import Iterable, Callable, Dict
from types import ModuleType
from typing_extensions import Self
import importlib
import pkgutil
from collections import OrderedDict

import reflex as rx
from reflex.base import Base


def load_modules(parent_md, is_pkg=True) -> Iterable[ModuleType]:
    """ 遍历子目录包, 加载services, 调用init方法进行初始化
    :param parent_md: package, service包对象
    :param is_pkg: bool, 子模块是否必须是pkg
    """
    for mf in pkgutil.iter_modules(parent_md.__path__):
        if is_pkg and not mf.ispkg:
            continue
        n = f'.{mf.name}'
        md = importlib.import_module(n, package=parent_md.__name__)
        yield md


class Route(Base):
    """A page route."""

    # The path of the route.
    path: str

    # The page title.
    title: str | None = None

    # The component to render for the route.
    component: Callable[[], rx.Component]

    def register(self) -> Self:
        routes[self.path] = self
        return self

    def add_page(self, app: rx.App):
        app.add_page(self.component, self.path, self.title)


routes: Dict[str, Route] = OrderedDict()


def page(path: str, title: str = "antd demo", props=None) -> Callable:
    props = props or {}
    # props.setdefault('height', '100%')

    def _webpage(contents: Callable[[tuple, dict], rx.Component]) -> Route:
        def wrapper(*children, **c_props) -> rx.Component:
            from antd_demo.components import footer, navbar, header

            return rx.flex(
                header(),
                navbar(),
                rx.flex(
                    rx.flex(
                        contents(*children, **c_props),
                    ),
                ),
                footer(),
                **props,
            )

        r = Route(path=path, title=title, component=wrapper).register()
        return r

    return _webpage
