from typing import Optional

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, AntdSubComponent


class Layout(AntdComponent):
    tag = 'Layout'

    has_sider: Optional[Var[bool]]

    def _get_custom_code(self) -> str | None:
        return """
        const { Header, Content, Footer, Sider } = Layout;
        """


class SubLayout(AntdSubComponent):
    width: Var[int]


class Header(SubLayout):
    tag = 'Header'


class Content(SubLayout):
    tag = 'Content'


class Footer(SubLayout):
    tag = 'Footer'


class Sider(SubLayout):
    tag = 'Sider'


layout = Layout.create
header = Header.create
content = Content.create
footer = Footer.create
sider = Sider.create

