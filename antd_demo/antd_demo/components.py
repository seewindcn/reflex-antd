import reflex as rx

from reflex_antd import navigation, layout, general, display, helper

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
            items=helper.contain([
                dict(key='general', label='general', icon=general.UserOutlined(), children=[
                    dict(key='nav1-1', label=rx.link('页面1', href='/')),
                    dict(key='nav1-general', label=rx.link('general', href='/general'), icon=general.CustomerServiceOutlined()),
                    dict(key='nav1-3', label=general.button('按钮3')),
                ]),
                dict(key='layout', label='layout', icon=general.LaptopOutlined(), children=[

                ]),
                dict(key='entry', label='entry', icon=general.LaptopOutlined(), children=[
                    dict(key='entry-form1', label=rx.link('form1', href='/entry/form1')),
                ]),
                dict(key='display', label='display', icon=general.LaptopOutlined(), children=[
                    dict(key='display-table1', label=rx.link('table1', href='/display/table1')),
                    dict(key='display-table2', label=rx.link('table2', href='/display/table2')),
                    dict(key='display-table3', label=rx.link('table3', href='/display/table3')),
                ]),

            ]),
            # selected_keys=['nav1-1'],
            open_keys=GlobalState.navbar_open_keys,
            selected_keys=GlobalState.navbar_selected_keys,
            on_open_change=GlobalState.set_navbar_open_keys,
            on_select=GlobalState.set_navbar_selected_keys,
            height='100%',
            class_name="border-2 border-gray-300"
        ),
        width=200,
        background='white',
    )


def subnav() -> rx.Component:
    return navigation.breadcrumb(
        items=helper.contain([
            dict(title=rx.link('Home', href='/')),
            dict(title=rx.link('Level1', href='/general')),
            dict(title=rx.link('Level2')),
        ]),
    )


def content(*args, **kwargs) -> rx.Component:
    return layout.content(
        general.float_group(
            general.float_button(
                icon=general.CommentOutlined.create(),
                badge=dict(count=5, color="blue"),
                href='/',
            ),
            general.float_button(
                icon=general.QuestionCircleOutlined.create(),
                on_click=GlobalState.on_event0,
            ),
            trigger='hover',
            type='primary',
            icon=general.CustomerServiceOutlined.create(),
            close_icon=general.CloseCircleOutlined.create(),
        ),
        *args,
        **kwargs
    )

