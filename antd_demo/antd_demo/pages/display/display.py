import random
from typing import List, Any, Dict

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout

from antd_demo.layout import page
from antd_demo.state import GlobalState


class DisplayState(State):
    active_key: str = 'tooltip'

    tag_checked: bool = False
    statistic_v1: int = 112893

    def on_tag_close(self, ev):
        print('on_tag_close', ev)


@rx.memo
def antd_display_tooltip() -> rx.Component:
    return rx.center(
        rx.vstack(
            display.tooltip(
                rx.text('Tooltip will show on mouse enter.'),
                title='prompt text',
                color='blue',
                placement='bottomLeft',
            ),
            layout.divider(),
            display.tooltip(
                general.button('Tooltip will show on mouse enter.'),
                placement='bottomRight',
                title='prompt text',
            ),
        ),
    )


@rx.memo
def antd_display_timeline() -> rx.Component:
    return rx.center(
        rx.vstack(
            display.timeline(
                items=helper.contain([
                    dict(children='Create a services site 2015-09-01'),
                    dict(children='Solve initial network problems 2015-09-01', color='red'),
                    dict(children=rx.box(
                        rx.el.p('Solve initial network problems 1'),
                        rx.el.p('Solve initial network problems 2'),
                        rx.el.p('Solve initial network problems 3'),
                    ), color='red'),
                    dict(children='Technical testing 2015-09-01', dot=general.icon('SmileOutlined')),
                    dict(children='Network problems being solved 2015-09-01'),
                ])
            )
        )
    )


@helper.stateful
def antd_display_tag() -> rx.Component:
    rs = rx.center(
        rx.vstack(
            rx.hstack(
                display.tag(
                    'Twitter',
                    bordered=True,
                    color="#55acee",
                    icon=general.icon('TwitterOutlined'),
                ),
                display.tag(
                    'Tag2-1',
                    color="red",
                    icon=general.icon('SyncOutlined', spin=True),
                    close_icon=True,
                    on_close=helper.js_event(
                        DisplayState.on_tag_close,
                        js="""
                        e.preventDefault();
                        var e = '';
                        """
                    ),
                ),
            ),
            layout.divider(dashed=True),
            display.checkable_tag(
                'Checkable',
                bordered=True,
                checked=DisplayState.tag_checked,
                on_change=DisplayState.set_tag_checked,
            ),
        ),
    )
    return rs


@helper.stateful
def statistic() -> rx.Component:
    return rx.center(
        rx.vstack(
            display.statistic(
                title='Account Balance(CNY)',
                value=DisplayState.statistic_v1,
                precision=2,
            ),
            layout.divider(),
        ),
    )


@page('/demo/display', 'display')
def display_page() -> rx.Component:
    return rx.box(
        display.tabs(
            # active_key=DisplayState.active_key,
            default_active_key='tooltip',
            items=helper.contain([
                display.tab_item(key='tooltip', label='tooltip', children=antd_display_tooltip()),
                display.tab_item(key='timeline', label='timeline', children=antd_display_timeline()),
                display.tab_item(key='tag', label='tag', children=antd_display_tag()),
                display.tab_item(key='statistic', label='statistic', children=statistic()),
            ]),
            on_change=DisplayState.set_active_key,
        ),
    )

