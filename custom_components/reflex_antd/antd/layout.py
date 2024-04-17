from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, AntdSubComponent, ReactNode, ContainVar
from ..constant import BreakpointType, ThemeType


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

    breakpoint: Optional[Var[Union[BreakpointType, Dict]]]
    collapsed: Optional[Var[bool]]
    collapsed_width: Optional[Var[int]]
    collapsible: Optional[Var[bool]]
    default_collapsed: Optional[Var[bool]]
    reverse_arrow: Optional[Var[bool]]
    theme: Optional[Var[ThemeType]]
    trigger: Optional[Var[ReactNode]]
    zero_width_trigger_style: Optional[Var[Union[Dict, ContainVar]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_breakpoint': lambda broken: [broken],
            'on_collapse': lambda collapsed, type: [collapsed, type],
        })
        return _triggers


layout = Layout.create
header = Header.create
content = Content.create
footer = Footer.create
sider = Sider.create

