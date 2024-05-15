import random
from typing import List, Any, Dict
import asyncio

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout

from antd_demo.layout import page


class DisplayState(State):
    active_key: str = 'tooltip'

    tag_checked: bool = False
    statistic_v1: int = 112893

    card_tab_list: list = [
        {
            "key": 'tab1',
            "tab": 'tab1',
        },
        {
            "key": 'tab2',
            "tab": 'tab2',
        },
    ]
    card_content_dict: dict[str, str] = {
        "tab1": "content1",
        "tab2": "content2",
    }
    card_content: str = "content1"

    collapse_items: list = [
        {
            "key": "1",
            "label": "This is panel header 1",
            "children": "this is content 1",
        },
        {
            "key": "2",
            "label": "This is panel header 2",
            "children": "this is content 2",
        },
    ]

    list_data: list = [
        'Racing car sprays burning fuel into crowd.',
        'Japanese princess to wed commoner.',
        'Australian walks 100km after outback crash.',
        'Man charged over missing wedding girl.',
        'Los Angeles battles huge wildfires.',
    ]

    tree_data = [
        dict(title='parent-1', key='0', children=[
            dict(title='child-1', key='0-1', children=[
            ]),
            dict(title='child-2', key='0-2', children=[
                dict(title='node-1', key='0-2-1', )
            ]),
        ]),
    ]

    select_calendar: str = ""

    badge_count: int = 5

    def badge_increment(self):
        self.badge_count += 1

    def badge_decrement(self):
        self.badge_count -= 1

    def badge_random_count(self):
        self.badge_count = random.randint(1, 100)
        return DisplayState.on_tag_close(f'badge_random_count:{self.badge_count}')

    def on_select_calendar(self, date, info):
        self.select_calendar = date

    def on_card_tab_change(self, key):
        self.card_content = self.card_content_dict[key]

    @rx.background
    async def on_tag_close(self, ev):
        print('on_tag_close', ev)
        await asyncio.sleep(3)


class AvatarState(State):
    UserList: list[str] = [
        'Edward', 'Lucy', 'Tom', 'U'
    ]
    ColorList: list[str] = [
        '#f56a00', '#7265e6', '#ffbf00', '#00a2ae'
    ]
    GapList: list[int] = [4, 3, 2, 1]
    user_index: int = 0
    user_name: str = UserList[user_index]
    color: str = ColorList[user_index]
    gap_index: int = 0
    gap: int = GapList[gap_index]
    url1: str = 'https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg'
    url2: str = 'https://api.dicebear.com/7.x/miniavs/svg?seed=1'
    url3: str = 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'
    url4: str = 'https://gd-hbimg.huaban.com/7bc41b57cc4a507d1ffb555bda6505364aabea6214116-KYhXEV_fw192webp'

    def next_user(self):
        self.user_index = (self.user_index + 1) % len(self.UserList)
        self.user_name = self.UserList[self.user_index]
        self.color = self.ColorList[self.user_index]

    def change_gap(self):
        self.gap_index = (self.gap_index + 1) % len(self.GapList)
        self.gap = self.GapList[self.gap_index]


@page('/display/display', 'display')
def display_page() -> rx.Component:
    return rx.box(
        display.tabs(
            # active_key=DisplayState.active_key,
            default_active_key='tooltip',
            items=helper.contain([
                display.tab_item(key='badge', label='badge', children=badge_page()),
                display.tab_item(key='tooltip', label='tooltip', children=antd_display_tooltip()),
                display.tab_item(key='timeline', label='timeline', children=antd_display_timeline()),
                display.tab_item(key='tag', label='tag', children=antd_display_tag()),
                display.tab_item(key='statistic', label='statistic', children=statistic()),
                display.tab_item(key='card', label='card', children=cards()),
                display.tab_item(key='empty', label='empty', children=empty()),
                display.tab_item(key='carousel', label='carousel', children=carousel_page()),
                display.tab_item(key='descriptions', label='descriptions', children=descriptions_page()),
                display.tab_item(key='image', label='image', children=image_page()),
                display.tab_item(key='calendar', label='calendar', children=calendar_page()),
                display.tab_item(key='collapse', label='collapse', children=collapse_page()),
                display.tab_item(key='list', label='list', children=list_page()),
                display.tab_item(key='avatar', label='avatar', children=avatar_page()),
                display.tab_item(key='tree', label='tree', children=tree_page()),
            ]),
            on_change=DisplayState.set_active_key,
            style=dict(
                width='100%',

            ),
        ),
    )


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
def cards() -> rx.Component:
    return rx.vstack(
        rx.text(
            "经典卡片，包含标题、内容、操作区域。"
        ),
        rx.hstack(
            display.card(
                rx.list_item("Example 1"),
                rx.list_item("Example 2"),
                rx.list_item("Example 3"),
                title=rx.text(
                    "Default size card"
                ),
                size="default",
                extra=rx.link(
                    "More",
                    href="/demo/avatar",
                ),
                width=300
            ),
            display.card(
                rx.list_item("Card content"),
                rx.list_item("Card content"),
                rx.list_item("Card content"),
                title=rx.text(
                    "Small size card"
                ),
                size="small",
                extra=rx.link(
                    "More",
                    href="/demo/badge",
                ),
                width=300
            ),
        ),
        rx.text(
            "简洁卡片，只包含内容区域。"
        ),
        rx.hstack(
            display.card(
                rx.list_item("Card content"),
                rx.list_item("Card content"),
                rx.list_item("Card content"),
                size="small",
                width=300
            ),
        ),
        rx.text(
            "栅格卡片,在系统概览页面常常和栅格进行配合。"
        ),
        rx.hstack(
            display.card(
                rx.list_item("Card content"),
                title=rx.text(
                    "Card title"
                ),
                bordered=False
            ),
            display.card(
                rx.list_item("Card content"),
                title=rx.text(
                    "Card title"
                ),
                bordered=False
            ),
            display.card(
                rx.list_item("Card content"),
                title=rx.text(
                    "Card title"
                ),
                bordered=False
            ),
        ),
        rx.text(
            "带页签的卡片,可承载更多内容。"
        ),
        rx.hstack(
            display.card(
                rx.list_item(DisplayState.card_content),
                title=rx.text(
                    "Card title"
                ),
                extra=rx.link(
                    "More",
                    href="/demo/badge",
                ),
                tab_list=DisplayState.card_tab_list,
                active_tab_key="tab1",
                width=600,
                on_tab_change=DisplayState.on_card_tab_change,
            ),
        ),
        spacing="6",

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


@helper.stateful
def empty() -> rx.Component:
    return rx.vstack(
        rx.text("简单的展示。"),
        display.empty(),
        rx.text("自定义图片链接、图片大小、描述、附属内容。"),
        display.empty(
            general.button(
                "Create Now ",
                type="primary"),
            image=rx.image(src="https://gw.alipayobjects.com/zos/antfincdn/ZHrcdLPrvN/empty.svg"),
            image_style={"height": "60"},
            description=rx.text("Customize", rx.link("Description", href="#API")),
        ),
    )


@helper.stateful
def badge_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.center(
                display.badge(
                    color="#faad14",
                    count=3,
                ),
                display.badge(
                    color="#f5222d",
                    count=11,
                ),
                display.badge(
                    color="#f5222d",
                    count=0,
                ),
                display.badge(
                    color="#52c41a",
                    overflow_count=99,
                    count=199,
                ),
                spacing="2",
            ),
        ),
        rx.hstack(
            rx.center(
                display.badge(
                    rx.text(""),
                    count=0,
                    show_zero=True,
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                display.badge(
                    rx.text(""),
                    overflow_count=10,
                    count=11,
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                display.badge(
                    rx.text(""),
                    count=999,
                    text=display.avatar(
                        shape="square",
                    ),
                ),

                display.badge(
                    rx.text(""),
                    overflow_count=999,
                    count=1111,
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                spacing="6",
            ),
        ),
        rx.hstack(
            rx.center(
                display.badge(
                    rx.text(""),
                    count=5,
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                display.badge(
                    rx.text(""),
                    count=5,
                    size="small",
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                spacing="6",
            ),
        ),
        rx.hstack(
            rx.center(
                display.badge(
                    rx.text(""),
                    count=DisplayState.badge_count,
                    text=display.avatar(
                        shape="square",
                    ),
                ),
                entry.radio_group(
                    general.button(
                        icon=general.icon("PlusOutlined"),
                        type="default",
                        on_click=DisplayState.badge_increment,
                    ),
                    general.button(
                        icon=general.icon("MinusOutlined"),
                        type="default",
                        on_click=DisplayState.badge_decrement,
                    ),
                    general.button(
                        icon=general.icon("QuestionOutlined"),
                        type="default",
                        on_click=DisplayState.badge_random_count,
                    ),
                ),
                spacing="4",
            ),
        ),
        spacing="6",

    )


@helper.stateful
def carousel_page() -> rx.Component:
    return rx.vstack(
        display.carousel(
            rx.list_item("Example 1"),
            rx.list_item("Example 2"),
            rx.list_item("Example 3"),
            style={
                "margin": 0,
                "height": '160px',
                "color": '#fff',
                "lineHeight": '160px',
                "textAlign": 'center',
                "background": '#364d79',
            },
            width=600,

        ),

    )


@helper.stateful
def descriptions_page() -> rx.Component:
    return rx.vstack(
        rx.text("简单的展示。"),
        display.descriptions(
            title=rx.text("User Info"),
            items=helper.contain([
                dict(key='1', label='UserName', children="Zhou Maomao"),
                dict(key='2', label='Telephone', children="1810000000"),
                dict(key='3', label='Live', children="Hangzhou, Zhejiang"),
                dict(key='4', label='Remark', children="empty"),
                dict(key='5', label='Address',
                     children="No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China"),
            ])
        ),
        rx.text("带边框和背景颜色列表。"),
        display.descriptions(
            title=rx.text("User Info"),
            bordered=True,
            items=helper.contain([
                dict(key='1', label='Product', children="Cloud Database"),
                dict(key='2', label='Billing Mode', children="Prepaid"),
                dict(key='3', label='Automatic Renewal', children="YES"),
                dict(key='4', label='Order time', children="2018-04-24 18:00:00"),
                dict(key='5', label='Usage Time', children="2019-04-24 18:00:00", span=2),
                dict(key='6', label='Status', children=display.badge(text="Running", status="processing"), span=3),
                dict(key='7', label='Config Info', children=rx.box(
                    rx.el.p('Data disk type: MongoDB'),
                    rx.el.p('Database version: 3.4'),
                    rx.el.p('Package: dds.mongo.mid'),
                    rx.el.p('Storage space: 10 GB'),
                    rx.el.p('Replication factor: 3'),
                )),
            ])
        ),

    )


@helper.stateful
def image_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("单击图像可以放大显示。"),
            display.image(
                width=200,
                src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"
            ),
        ),
        rx.hstack(
            rx.text("加载失败显示图像占位符。"),
            display.image(
                width=200,
                height=200,
                src="error",
                fallback="data:image/png;base64,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"
            ),
        ),
        rx.hstack(
            rx.text("点击左右切换按钮可以预览多张图片。"),
            display.image_preview_group(
                display.image(
                    width=200,
                    src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg"
                ),
                display.image(
                    width=200,
                    src="https://gw.alipayobjects.com/zos/antfincdn/aPkFc8Sj7n/method-draw-image.svg"
                ),
            )
        ),

    )


@helper.stateful
def calendar_page() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text(
                "一个通用的日历面板，支持年/月切换"
            ),
            rx.hstack(
                display.calendar(

                ),
            ),
            rx.text(
                "用于嵌套在空间有限的容器中"
            ),
            rx.hstack(

                display.calendar(
                    width="30%",
                ),
            ),
            rx.text(
                f"You selected date:{DisplayState.select_calendar}"
            ),
            rx.hstack(
                display.calendar(
                    on_select=DisplayState.on_select_calendar,
                ),
            ),
            spacing="3",
        ),
    )


@helper.stateful
def collapse_page() -> rx.Component:
    return rx.vstack(
        rx.text("折叠面板,可以同时展开多个面板，这个例子默认展开了第一个。"),
        display.collapse(
            items=DisplayState.collapse_items,
            default_active_key="1",
            width="100%"
        ),
        rx.text("折叠面板有大、中、小三种尺寸。"),
        layout.divider(
            rx.text("Default Size")
        ),
        display.collapse(
            items=[{"key": "1", "label": "This is default size panel header", "children": "this is content"}],
            width="100%"
        ),
        layout.divider(
            rx.text("Small Size")
        ),
        display.collapse(
            items=[{"key": "1", "label": "This is default size panel header", "children": "this is content"}],
            width="100%",
            size="small"
        ),
        layout.divider(
            rx.text("Large Size")
        ),
        display.collapse(
            items=[{"key": "1", "label": "This is default size panel header", "children": "this is content"}],
            width="100%",
            size="large"
        ),

    )


@helper.stateful
def list_page() -> rx.Component:
    return rx.vstack(
        layout.divider(
            rx.text("Default Size")
        ),
        display.alist(
            header=rx.text("Header"),
            footer=rx.text("Footer"),
            bordered=True,
            data_source=DisplayState.list_data,
            render_item=helper.js_value(lambda: display.list_item(DisplayState.list_data)),
        ),
    )


@helper.stateful
def avatar_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.center(
                display.avatar(
                    alt="test",
                    shape="circle",
                    size=50,
                    src=AvatarState.url1,
                    draggable=False,
                ),
                display.avatar(
                    alt="test",
                    shape="circle",
                    size="large",
                    src=AvatarState.url2,
                    draggable=False,
                ),
                display.avatar(
                    alt="test",
                    shape="circle",
                    size="default",
                    src=AvatarState.url3,
                    draggable=False
                ),
                spacing="2",

            ),

        ),
        rx.hstack(
            rx.center(
                display.avatar(
                    icon=general.icon("UserOutlined"),
                    shape="square",
                ),
                display.avatar(
                    icon=general.icon("UserOutlined"),
                    shape="square",
                    backgroundColor="#87d068"
                ),
                display.avatar(
                    "U",
                    shape="square",
                ),
                display.avatar(
                    "U",
                    shape="square",
                    backgroundColor="#fde3cf",
                    color="#f56a00"
                ),
                display.avatar(
                    "USER",
                    shape="square",
                ),
                display.avatar(
                    src=AvatarState.url4,
                    shape="square",
                    size='large',
                ),
                spacing="2",

            )
        ),
        rx.hstack(
            rx.center(
                display.avatar(
                    shape="square",
                    size=50,
                    icon=general.icon("UserOutlined"),
                    draggable=True
                ),
                display.avatar(
                    shape="square",
                    size="large",
                    icon=general.icon("UserOutlined"),
                    draggable=True
                ),
                display.avatar(
                    shape="square",
                    size="default",
                    icon=general.icon("UserOutlined"),
                    draggable=True
                ),
                spacing="2",

            )
        ),
        rx.hstack(
            rx.center(
                display.avatar(
                    AvatarState.user_name,
                    shape="circle",
                    size="large",
                    backgroundColor=AvatarState.color,
                    gap=AvatarState.gap
                ),
                general.button(
                    "ChangeUser",
                    type="default",
                    on_click=AvatarState.next_user,
                ),
                general.button(
                    "ChangeGap",
                    type="default",
                    on_click=AvatarState.change_gap,
                ),
                spacing="2",

            )
        ),
        rx.hstack(
            rx.center(
                display.badge(
                    rx.text(""),
                    count=3,
                    text=display.avatar(
                        shape="square",
                        size="default",
                        icon=general.icon("UserOutlined"),
                        draggable=True
                    ),
                ),
                spacing="2",

            )
        ),

    )


@helper.stateful
def tree_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            display.tree(
                tree_data=DisplayState.tree_data,
                checkable=True,
            ),
        ),
    )
