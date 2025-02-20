import reflex as rx
from reflex.constants import MemoizationDisposition
from reflex.components.core.cond import color_mode_cond
from reflex_antd import navigation, layout, general, display, helper, feedback

from .state import GlobalState


def header() -> rx.Component:
    return layout.header(
        rx.cond(
            GlobalState.collapsed,
            general.button(
                icon=general.icon('MenuUnfoldOutlined'),
                on_click=GlobalState.collapsed_switch,
            ),
            general.button(
                icon=general.icon('MenuFoldOutlined'),
                on_click=GlobalState.collapsed_switch,
            ),
        ),
        navigation.menu(
            items=[
                dict(key='nav1', label='Nav 1'),
                dict(key='nav2', label='Nav 2'),
                dict(key='nav3', label='Nav 3'),
            ],
            mode='horizontal',
            flex=1,
            min_width=0,
        ),

        layout.space(size='middle'),
        rx.color_mode.switch(),
        align_items='center',
        display='flex',
        padding='0 24px 16px 16px',
        justify_content='space-between',
        background=color_mode_cond('#fff', '#141414'),
        border_bottom=color_mode_cond('1px solid #343A46', '1px solid #EBECF0'),

    )


def footer() -> rx.Component:
    return layout.footer(
        rx.box(
            class_name="border-2 border-gray-300"
        ),
    )


def nav_items() -> list:
    from .layout import routes, get_route_groups
    items = [
        dict(key='index', label=rx.link('index', href='/')),
    ]
    for _, g in get_route_groups().items():
        group = dict(key=g.name,
                     label=g.name if not g.path else rx.link(g.name, href=g.path),
                     icon=g.icon, children=[])
        for _, r in routes.items():
            if r.group != g.name:
                continue
            group['children'].append(
                dict(key=f'{g.name}-{r.path}',
                     label=rx.link(r.path, href=r.path),
                     icon=r.icon))
        items.append(group)
    return helper.contain(items)


def navbar() -> rx.Component:
    return layout.sider(
        navigation.menu(
            items=nav_items(),
            # selected_keys=['nav1-1'],
            open_keys=GlobalState.navbar_open_keys,
            selected_keys=GlobalState.navbar_selected_keys,
            on_open_change=GlobalState.set_navbar_open_keys,
            on_select=GlobalState.set_navbar_selected_keys,
            mode='inline',
            height='100%',
            border_right=0,
            class_name="border-2 border-gray-300",
        ),
        collapsed=GlobalState.collapsed,
        width=200,
        # background='white',
        border_right=color_mode_cond('1px solid #343A46', '1px solid #EBECF0'),
        box_shadow='0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
    )


def _sub_item(i: dict) -> rx.Component:
    b = helper.container(
        dict(title=rx.link(i['title'], href=i['href'])),
    )
    return b


def subnav() -> rx.Component:
    return rx.hstack(
        navigation.breadcrumb(
            items=helper.js_value(rx.foreach(GlobalState.subnav_items, _sub_item)),
        ),
        height='22px',
    )


def content(*children: rx.Component, **kwargs) -> rx.Component:
    return layout.content(
        # feedback.message_holder(
        #     msg=feedback.message(
        #         is_global=False,
        #         config=dict(type='info', content=''),
        #     ),
        # ),
        *children,
        general.float_group(
            general.float_button(
                icon=general.icon('CommentOutlined'),
                badge=dict(count=5, color="blue"),
                href='/',
            ),
            general.float_button(
                icon=general.icon('QuestionCircleOutlined'),
                on_click=GlobalState.on_event0,
            ),
            trigger='hover',
            type='primary',
            icon=general.icon('CustomerServiceOutlined'),
            close_icon=general.icon('CloseCircleOutlined'),
        ),
        ex_hooks=[
            feedback.notification(is_global=True),
        ],
        **kwargs
    )
