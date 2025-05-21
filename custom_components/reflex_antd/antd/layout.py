from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ReactNode, ContainVar, memo_never
from ..constant import BreakpointType, ThemeType


class LayoutBase(AntdComponent):
    pass


class Layout(LayoutBase):
    tag = 'Layout'

    has_sider: Var[bool]

    # def _get_custom_code(self) -> str | None:
    #     return """
    #     const { Header, Content, Footer, Sider } = Layout;
    #     """


class SubLayout(AntdComponent):
    width: Var[Union[int, str]]


class Header(SubLayout):
    tag = 'Layout.Header'

    _memoization_mode = memo_never


class Content(SubLayout):
    tag = 'Layout.Content'

    _memoization_mode = memo_never


class Footer(SubLayout):
    tag = 'Layout.Footer'

    _memoization_mode = memo_never


class Sider(SubLayout):
    tag = 'Layout.Sider'

    breakpoint: Var[Union[BreakpointType, Dict]]
    collapsed: Var[bool]
    collapsed_width: Var[int]
    collapsible: Var[bool]
    default_collapsed: Var[bool]
    reverse_arrow: Var[bool]
    theme: Var[ThemeType]
    trigger: Var[ReactNode]
    zero_width_trigger_style: Var[Union[Dict, ContainVar]]

    _memoization_mode = memo_never

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

