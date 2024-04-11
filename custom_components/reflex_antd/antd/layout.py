from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, AntdSubComponent


class LayoutBase(AntdComponent):
    pass


class Layout(LayoutBase):
    tag = 'Layout'

    has_sider: Optional[Var[bool]]

    # def _get_custom_code(self) -> str | None:
    #     return """
    #     const { Header, Content, Footer, Sider } = Layout;
    #     """


class SubLayout(AntdComponent):
    width: Optional[Var[Union[int, str]]]


class Header(SubLayout):
    tag = 'Layout.Header'


class Content(SubLayout):
    tag = 'Layout.Content'


class Footer(SubLayout):
    tag = 'Layout.Footer'


class Sider(SubLayout):
    tag = 'Layout.Sider'


layout = Layout.create
header = Header.create
content = Content.create
footer = Footer.create
sider = Sider.create

