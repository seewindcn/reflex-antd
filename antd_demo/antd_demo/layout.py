from typing import Iterable, Callable, Dict, Type
from types import ModuleType
from typing_extensions import Self
import importlib
import pkgutil
from collections import OrderedDict

import reflex as rx
from reflex import Component, ImportDict, ImportVar
from reflex.vars import VarData
from reflex.base import Base
from reflex.event import EventHandler, EventSpec
from reflex.components.core.cond import color_mode_cond


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

    group: str = 'other'
    # The path of the route.
    path: str

    icon: Component = None
    # The page title.
    title: str | None = None

    # The component to render for the route.
    component: Callable[[], rx.Component]

    on_load: EventHandler | EventSpec | list[EventHandler | EventSpec] | None
    sub_on_load: EventHandler | EventSpec | list[EventHandler | EventSpec] | None

    state: Type[rx.State] | None = None

    def register(self) -> Self:
        routes[self.path] = self
        return self

    def add_page(self, app: rx.App):
        app.add_page(self.component, self.path, self.title, on_load=self.on_load)


class RouteGroup(Base):
    icon: Component
    name: str
    path: str = ''


routes: Dict[str, Route] = OrderedDict()
_route_groups: dict = None


def get_route_groups() -> dict:
    global _route_groups
    if _route_groups:
        return _route_groups
    from reflex_antd import layout, general
    _route_groups = dict(
        general=RouteGroup(name='general', icon=general.icon('UserOutlined'), path='/'),
        layout=RouteGroup(name='layout', icon=general.icon('AlignCenterOutlined')),
        navigation=RouteGroup(name='navigation', icon=general.icon('RadarChartOutlined')),
        feedback=RouteGroup(name='feedback', icon=general.icon('MediumOutlined')),
        display=RouteGroup(name='display', icon=general.icon('PicLeftOutlined')),
        entry=RouteGroup(name='entry', icon=general.icon('LaptopOutlined')),
        other=RouteGroup(name='other', icon=general.icon('QuestionOutlined')),
    )
    return _route_groups


def get_root_hooks() -> list:
    hook = rx.Var(
        _js_expr=f"",
        _var_data=VarData(
            imports={
                "$/utils/state": [ImportVar(tag="refs")],
            }
        ),
    )
    return [hook]


def layout0(*children: rx.Component, min_height: str = '50vh', **kwargs) -> rx.Component:
    return rx.hstack(
        *children,
    )


# @rx.memo
def layout1(*children: rx.Component, min_height: str = '50vh', **kwargs) -> rx.Component:
    from reflex_antd import layout, general
    from antd_demo.components import footer, navbar, header, subnav, content
    # color_bg_contain = 'white'
    return layout.layout(
        navbar(),
        layout.layout(
            header(),
            layout.layout(
                subnav(),
                content(
                    *children,
                    # background=color_bg_contain,
                    min_height=280,
                    background=color_mode_cond('#f5f5f5', '#000'),
                    padding='24px 24px 24px 24px',
                ),
                # padding='0 24px 24px',
            ),
            footer(),
        ),
        min_height=min_height,
        **kwargs
    )


def page(path: str, group: str = 'other',
         icon: Component = None,
         title: str = "antd demo",
         props=None,
         on_load: (
                 EventHandler | EventSpec | list[EventHandler | EventSpec] | None
         ) = None,
         state: Type[rx.State] = None,
         ) -> Callable:
    layout_props = props or {}

    layout_props.setdefault('min_height', '100vh')

    def _webpage(contents: Callable[[tuple, dict], rx.Component]) -> Route:
        def wrapper(*children, **c_props) -> rx.Component:
            child = contents(*children, **c_props)
            return layout1(
                child,
                ex_hooks=get_root_hooks(),
                **layout_props)

        from .state import GlobalState

        r = Route(group=group, path=path,
                  icon=icon, title=title,
                  component=wrapper,
                  on_load=GlobalState.on_page_load,
                  sub_on_load=on_load,
                  state=state,
                  ).register()
        return r

    return _webpage
