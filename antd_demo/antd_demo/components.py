import reflex as rx

from reflex_antd import navigation, layout, general

from .state import GlobalState


def header() -> rx.Component:
    return layout.header(
        navigation.menu(
            items=[
                dict(key='nav1', label='Nav 1'),
                dict(key='nav2', label='Nav 2'),
                dict(key='nav3', label='Nav 3'),
            ],
            theme='dark',
            mode='horizontal',
            flex=1,
            min_width=0,
        ),
        align_items='center',
        display='flex',
    )


def footer() -> rx.Component:
    return layout.footer(
        rx.box(
            class_name="border-2 border-gray-300"
        ),
    )


# navigation.MI(key='sub1', label='subnav1', icon=general.UserOutlined()),
# navigation.MI(key='sub2', label='subnav2', icon=general.LaptopOutlined()),


def navbar() -> rx.Component:
    return layout.sider(
        navigation.menu(
            mode='inline',
            items=navigation.items([
                dict(key='nav1', label='SubNav 1', icon=general.UserOutlined(), children=[
                    dict(key='nav1-1', label=rx.link('页面1', href='/')),
                    dict(key='nav1-general', label=rx.link('general', href='/general'), icon=general.CustomerServiceOutlined()),
                    dict(key='nav1-3', label=general.button('按钮3')),
                ]),
                dict(key='nav2', label='SubNav 2', icon=general.LaptopOutlined()),
            ]),
            # selected_keys=['nav1-1'],
            open_keys=GlobalState.navbar_open_keys,
            selected_keys=GlobalState.navbar_selected_keys,
            onOpenChange=GlobalState.set_navbar_open_keys,
            onSelect=GlobalState.set_navbar_selected_keys,
            height='100%',
            class_name="border-2 border-gray-300"
        ),
        width=200,
        background='white',
    )


def subnav() -> rx.Component:
    return navigation.breadcrumb(
        items=navigation.items([
            dict(title=rx.link('Home', href='/')),
            dict(title=rx.link('Level1', href='/general')),
            dict(title=rx.link('Level2')),
        ]),
    )