import time
from typing import List, Any, Dict, Optional
import asyncio

import reflex as rx
from reflex import State, Var, Component

from reflex_antd import helper, display, general, entry, layout, feedback, navigation

from antd_demo.layout import page


class AntdNavigationPage(State):
    active_key: str = "anchor"


@helper.stateful
def antd_navigation_anchor() -> rx.Component:
    return rx.vstack(
        layout.row(
            layout.col(
                rx.el.div(
                    id='part-1',
                    height='80vh',
                    background='rgba(255,0,0,0.2)',
                ),
                rx.el.div(
                    id='part-2',
                    height='80vh',
                    background='rgba(0,255,0,0.2)',
                ),
                rx.el.div(
                    id='part-3',
                    height='80vh',
                    background='rgba(0,0,255,0.2)',
                ),
                span=16,
            ),
            layout.col(
                navigation.anchor(
                    items=[
                        dict(key='part-1', href='#part-1', title='part-1'),
                        dict(key='part-2', href='#part-2', title='part-2'),
                        dict(key='part-3', href='#part-3', title='part-3'),
                    ],
                ),
                span=8,
            ),
            width='100%',
        ),
        layout.divider(),
    )


class BreadcrumbListItem(rx.Base):
    title: str


class NavigationBreadcrumbState(State):
    items: list[BreadcrumbListItem] = [
        BreadcrumbListItem(title="Home"),
        BreadcrumbListItem(title="Application Center"),
    ]


@rx.memo
def antd_navigation_breadcrumb() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            navigation.breadcrumb(
                separator=rx.text("/"),
                items=NavigationBreadcrumbState.items
            )
        ),
        width="100%",
    )


class NavigationDropdownState(State):

    def on_click(self):
        pass


@rx.memo
def antd_navigation_dropdown() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            navigation.dropdown_button(
                "Dropdown",
                on_click=feedback.message(
                    is_global=True,
                    type="success",
                    content='Hello, Ant Design!',
                ),
                placement="bottom",
                # icon=general.icon("UserOutlined"),
                menu=helper.contain({
                    "items": [
                        dict(key='1', label="1st menu item"),
                        dict(key='2', label="2st menu item"),
                    ]})
            )

        ),
        width="100%",
    )


class MenuListItem(rx.Base):
    key: str
    label: str
    title: str
    icon: Any
    children: Any


class NavigationMenuState(State):
    items: list[MenuListItem] = [
        MenuListItem(key="mail", label="Navigation One", title="Navigation One",
                     icon=general.icon("LaptopOutlined")),
        # MenuListItem(key="mail",label="Navigation One",title="Navigation One"),
        MenuListItem(key="app", label="Navigation Two", title="Navigation Two"),
        MenuListItem(
            key="ttt",
            label="Navigation three",
            title="Navigation three",
            children=[
                {"type": 'group', "label": 'Item 1', "children": [{"label": 'Option 1', "key": 'setting:1'}]},
            ]
        ),
    ]


@rx.memo
def antd_navigation_menu() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            navigation.menu(
                selectedKeys=["email"],
                mode="vertical",
                items=helper.contain([
                    dict(key="mail", label="Navigation One", title="Navigation One",
                         icon=general.icon("MailOutlined")),
                    dict(key="app", label="Navigation Two", title="Navigation Two",
                         icon=general.icon("AppstoreOutlined")),
                    dict(key="SubMenu", label="Navigation Three - Submenu", icon=general.icon("SettingOutlined"),
                         children=[
                             dict(type="group", label="Item 1", children=[
                                 dict(label="Option 1", key="setting:1"),
                                 dict(label="Option 2", key="setting:2"),
                             ]),
                             dict(type="group", label="Item 2", children=[
                                 dict(label="Option 3", key="setting:3"),
                                 dict(label="Option 4", key="setting:4"),
                             ])
                         ]),
                ])
            ),
            width=600
        ),
    )


class NavigationPaginationState(State):

    def show_total(self, total, range) -> str:
        print(total, range)


@rx.memo
def antd_navigation_pagination() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("基础分页。"),
            navigation.pagination(
                default_current=1,
                page_size=10,
                total=50,
            ),
        ),
        rx.vstack(
            rx.text("更多分页。"),
            navigation.pagination(
                default_current=6,
                total=500,
            ),
        ),
        rx.vstack(
            rx.text("展示所有配置选项。"),
            navigation.pagination(
                default_current=6,
                show_size_changer=True,
                show_quick_jumper=True,
                total=500,
                show_total=helper.js_value('((total, range) => `${range[0]}-${range[1]} of ${total} items`)')
            ),
        ),
        width="100%",
    )


class NavigationStepState(State):
    current: int = 1
    current2: int = 0
    items: list = [
        dict(title="Finished", description="step1"),
        dict(title="In Progress", description="step2", subTitle="Left 00:00:08"),
        dict(title="Waiting", description="step3"),
    ]

    def on_load(self):
        self.current2 = 0

    def on_change(self, current):
        self.current = current

    @rx.var
    def return_items_len(self) -> int:
        return len(self.items)

    def increment(self):
        self.current2 += 1

    def decrement(self):
        self.current2 -= 1


@rx.memo
def antd_navigation_steps() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("简单的步骤条。"),
            navigation.steps(
                current=1,
                items=helper.contain([
                    dict(title="Finished", description="step1"),
                    dict(title="In Progress", description="step2", subTitle="Left 00:00:08"),
                    dict(title="Waiting", description="step3"),
                ]),
                width=600,
            ),
            rx.text("带有进度的步骤。"),
            navigation.steps(
                current=0,
                percent=60,
                items=helper.contain([
                    dict(title="Finished", description="step1"),
                    dict(title="In Progress", description="step2", subTitle="Left 00:00:08"),
                    dict(title="Waiting", description="step3"),
                ]),
                width=600,
            ),
            rx.text("设置 onChange 后，Steps 变为可点击状态。"),
            navigation.steps(
                current=NavigationStepState.current,
                items=helper.contain([
                    dict(title="Finished", description="step1"),
                    dict(title="In Progress", description="step2", subTitle="Left 00:00:08"),
                    dict(title="Waiting", description="step3"),
                ]),
                width=600,
                on_change=NavigationStepState.on_change
            ),
            rx.text("通常配合内容及按钮使用，表示一个流程的处理进度。"),
            navigation.steps(
                current=NavigationStepState.current2,
                percent=60,
                items=helper.contain(NavigationStepState.items),
                width=600,
            ),
            rx.cond(
                NavigationStepState.current2 < NavigationStepState.return_items_len - 1,
                rx.button("Next", on_click=NavigationStepState.increment),
                rx.text("")
            ),
            rx.cond(
                NavigationStepState.current2 == NavigationStepState.return_items_len - 1,
                general.button("Done", on_click=feedback.message(
                    is_global=True,
                    type="success",
                    content='Hello, Ant Design!',
                )),
                rx.text("")
            ),
            rx.cond(
                NavigationStepState.current2 > 0,
                rx.button("Previous", on_click=NavigationStepState.decrement),
                rx.text("")
            ),

        ),
        width="100%",
    )


@page('/navigation/navigation', 'navigation', on_load=NavigationStepState.on_load)
def navigation_page() -> rx.Component:
    return rx.box(
        display.tabs(
            active_key=AntdNavigationPage.active_key,
            default_active_key='anchor',
            items=helper.contain([
                display.tab_item(key='anchor', label='anchor', children=antd_navigation_anchor()),
                display.tab_item(key='breadcrumb', label='breadcrumb', children=antd_navigation_breadcrumb()),
                display.tab_item(key='dropdown', label='dropdown', children=antd_navigation_dropdown()),
                display.tab_item(key='menu', label='menu', children=antd_navigation_menu()),
                display.tab_item(key='pagination', label='pagination', children=antd_navigation_pagination()),
                display.tab_item(key='steps', label='steps', children=antd_navigation_steps()),
            ]),
            on_change=AntdNavigationPage.set_active_key,
        ),
    )
