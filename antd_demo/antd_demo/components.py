import reflex as rx

from reflex_antd import navigation, layout, general


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
            items=navigation.menu_items([
                dict(key='nav1', label='SubNav 1', icon=general.UserOutlined()),
                dict(key='nav2', label='SubNav 2', icon=general.LaptopOutlined()),
            ]),

            height='100%',
            class_name="border-2 border-gray-300"
        ),
        width=200,
        background='white',
    )
