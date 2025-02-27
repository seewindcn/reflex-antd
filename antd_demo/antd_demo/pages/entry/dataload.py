import random
import asyncio
from typing import List, Any, Dict
import json

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout

from antd_demo.layout import page

from reflex_antd.base import js_value, js_event


class DataLoadState(State):
    data = [{'key': str(i), 'title': f'content {i}', 'description': f'description {i}'} for i in range(1, 15)]
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

    select_calendar: str = ""

    badge_count: int = 5

    def badge_increment(self):
        self.badge_count += 1

    def badge_decrement(self):
        self.badge_count -= 1

    def badge_random_count(self):
        self.badge_count = random.randint(1, 100)

    def on_select_calendar(self, date, info):
        self.select_calendar = date

    def on_card_tab_change(self, key):
        self.card_content = self.card_content_dict[key]

    @rx.event(background=True)
    async def on_tag_close(self, ev):
        print('on_tag_close', ev)
        await asyncio.sleep(3)


class TransferState(rx.State):
    target_keys: list = []
    selected_keys: list = []

    def change_target_keys(self, target_keys, direction, move_keys):
        # print(target_keys, direction, move_keys)
        self.target_keys = target_keys

    def on_select_keys(self, s_keys: list, t_keys: list):
        print(s_keys, t_keys)
        self.selected_keys = [*s_keys, *t_keys]
        # self.selected_keys = s_keys.extend(t_keys)


@helper.stateful
def antd_transfer() -> rx.Component:
    return rx.stack(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.heading("基本穿梭框"),
                    entry.transfer(
                        data_source=[{'key': str(i), 'title': f'content {i}', 'description': f'description {i}'} for i
                                     in range(1, 15)],
                        titles=helper.contain(['Source', 'Target']),
                        target_keys=TransferState.target_keys,
                        selected_keys=TransferState.selected_keys,
                        on_select_change=TransferState.on_select_keys,
                        on_change=TransferState.change_target_keys,
                        operation_style={'background_color': 'blue'}
                    ),
                ),
                rx.box(
                    rx.heading("自定义题目样式"),
                    entry.transfer(
                        data_source=[{'key': str(i), 'title': f'content {i}', 'description': f'description {i}'} for i
                                     in range(1, 15)],
                        titles=helper.contain(['Source', 'Target']),
                        target_keys=TransferState.target_keys,
                        selected_keys=TransferState.selected_keys,
                        on_select_change=TransferState.on_select_keys,
                        on_change=TransferState.change_target_keys,
                        item_render=helper.js_value(
                            lambda record:
                            rx.hstack(
                                rx.badge(record.key.to_react()),
                                '-',
                                rx.code(record['title'].to_react()),
                            )
                        ),
                    ),
                ),
            ),
            rx.divider(),
            rx.hstack(
                rx.box(
                    rx.heading("带搜索框"),
                    entry.transfer(
                        data_source=[{'key': str(i), 'title': f'content {i}', 'description': f'description {i}'} for i
                                     in range(1, 15)],
                        titles=helper.contain(['Source', 'Target']),
                        target_keys=TransferState.target_keys,
                        selected_keys=TransferState.selected_keys,
                        on_select_change=TransferState.on_select_keys,
                        on_change=TransferState.change_target_keys,
                        operation_style={'background_color': 'blue'},
                        show_search=True
                    ),
                ),
                rx.box(
                    rx.heading("带分页"),
                    entry.transfer(
                        data_source=[{'key': str(i), 'title': f'content {i}', 'description': f'description {i}'} for i
                                     in range(1, 1000)],
                        titles=helper.contain(['Source', 'Target']),
                        target_keys=TransferState.target_keys,
                        selected_keys=TransferState.selected_keys,
                        on_select_change=TransferState.on_select_keys,
                        on_change=TransferState.change_target_keys,
                        operation_style={'background_color': 'blue'},
                        show_search=True,
                        pagination=True
                    )
                )

            )
        ),

    )


class TreeState(rx.State):
    value: list = []
    init_data: list = [
        {'value': '1', 'title': 'key1-Expand to load', 'children': None},
        {'value': '2', 'title': 'key2-Expand to load', 'children': None},
        {'value': '3', 'title': 'key3-TreeLeaf', 'isLeaf': True},
    ]
    simple_data: list = [
        dict(id=1, pId=0, value='key1', title='key1-Expand to load'),
        dict(id=2, pId=0, value='key2', title='key2-Expand to load'),
        dict(id=3, pId=0, value='key3', title='key3-Leaf', isLeaf=True),
    ]
    _r = 1

    def change_value(self, value, label, extra):
        print(value, label, extra)
        self.value = value

    def on_load_value(self, node):
        if node.get('children', None):
            return
        key = node['value']
        keys = key.split('-')
        nodes = self.init_data
        while keys:
            n = [i for i in nodes if i['value'] == keys[0]]
            if not n:
                return
            else:
                n = n[0]
                nodes = n['children']
                _k = keys[0]
                keys = keys[1:]
                if keys:
                    keys[0] = f'{_k}-{keys[0]}'

        n['children'] = [{'value': f'{key}-{i+1}', 'title': f'{key}-{i+1}-Expand to load', 'children': None} for i in range(2)]

    def on_load_simple_value(self, node):
        _id = int(node['id'])
        _id1 = 100 * _id + 1
        if [i for i in self.simple_data if i['id'] == _id1]:
            return
        self.simple_data.extend(
            [dict(id=i, pId=_id, value=f'key-{i}', title=f'key{i}-Expand to load') for i in range(_id1, _id1+2)]
        )


@helper.stateful
def antd_tree_select() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.heading('基本树选择'),
            rx.hstack(
                entry.tree_select(
                    tree_data=[
                        {'value': 'parent 1', 'title': 'parent 1',
                         'children': [{'value': f'leaf{i}', 'title': f'leaf{i}'} for i in range(1, 3)]},
                        {'value': 'parent 2', 'title': 'parent 2',
                         'children': [{'value': f'leaf{i}', 'title': f'leaf{i}'} for i in range(4, 8)]}
                    ],
                    show_search=True,
                    dropdown_style=dict(
                        maxHeight=400,
                        overflow='auto'
                    ),
                    placeholder="Please select",
                    allow_clear=True,
                    tree_default_expand_all=True,
                    style=dict(
                        width='500px',
                    ),
                    on_change=TreeState.change_value

                ),
            )
        ),
        rx.box(
            rx.heading('多选树选择'),
            rx.hstack(
                entry.tree_select(
                    tree_data=[
                        {'value': 'parent 1', 'title': 'parent 1',
                         'children': [{'value': f'leaf{i}', 'title': f'leaf{i}'} for i in range(1, 3)]},
                        {'value': 'parent 2', 'title': 'parent 2',
                         'children': [{'value': f'leaf{i}', 'title': f'leaf{i}'} for i in range(4, 8)]}
                    ],
                    show_search=True,
                    dropdown_style=dict(
                        maxHeight=400,
                        overflow='auto'
                    ),
                    placeholder="Please select",
                    allow_clear=True,
                    tree_default_expand_all=True,
                    style=dict(
                        width='500px',
                    ),
                    multiple=True,
                    on_change=TreeState.change_value

                ),
            )
        ),
        layout.divider(),
        rx.box(
            rx.heading('async load data'),
            rx.hstack(
                entry.tree_select(
                    tree_data=TreeState.init_data,
                    show_search=True,
                    dropdown_style=dict(
                        maxHeight=400,
                        overflow='auto'
                    ),
                    placeholder="Please select",
                    # allow_clear=True,
                    # tree_default_expand_all=True,
                    style=dict(
                        width='500px',
                    ),
                    multiple=True,
                    # on_change=TreeState.change_value,
                    load_data=js_event(TreeState.on_load_value, js="""(node) => {
    return new Promise((resolve) => {
          if (node.children) {
            resolve();
            return;
          }
          %(name)s(node);
          setTimeout(() => { resolve(); }, 500);
    }); 
    }""", fmt=True),
                ),
            ),
        ),
        layout.divider(),
        rx.box(
            rx.heading('async load simple data'),
            rx.hstack(
                entry.tree_select(
                    tree_data=TreeState.simple_data,
                    tree_data_simple_mode=True,
                    show_search=True,
                    dropdown_style=dict(
                        maxHeight=400,
                        overflow='auto'
                    ),
                    placeholder="Please select",
                    allow_clear=True,
                    # tree_default_expand_all=True,
                    style=dict(
                        width='500px',
                    ),
                    multiple=True,
                    # on_change=TreeState.change_value,
                    load_data=js_event(TreeState.on_load_simple_value, js="""(node) => {
    return new Promise((resolve) => {
          if (node.children) {
            resolve();
            return;
          }
          %(name)s(node);
          setTimeout(() => { resolve(); }, 500);
    }); 
    }""", fmt=True),
                ),
            ),
        ),

    )


@helper.stateful
def antd_upload() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.heading('base upload'),
            rx.hstack(
                entry.upload(
                    general.button(
                        'Click to Upload',
                        icon=general.icon('UploadOutlined')
                    ),
                    name='file',
                    action='https://660d2bd96ddfa2943b33731c.mockapi.io/api/upload',
                    headers=dict(authorization='authorization-text'),
                    # children=helper.js_value(
                    #     lambda record:
                    #     general.button(
                    #         'Click to Upload',
                    #         icon=general.icon('UploadOutlined')
                    #     ),
                    # )
                ),
            ),
        ),
        rx.box(
            rx.heading('file dir upload'),
            rx.hstack(
                entry.upload(
                    general.button(
                        'Click to Upload',
                        icon=general.icon('UploadOutlined')
                    ),
                    name='avatar',
                    action='https://660d2bd96ddfa2943b33731c.mockapi.io/api/upload',
                    class_name="avatar-uploader",
                    headers=dict(authorization='authorization-text'),
                    directory=True
                ),
            ),
        ),
    )


class TabsState(State):
    active_key: str = 'tree_select'


@page('/entry/dataload', 'entry')
def display_page() -> rx.Component:
    return rx.box(
        display.tabs(
            # active_key=TabsState.active_key,
            default_active_key='tree_select',
            items=helper.contain([
                display.tab_item(key='my_transfer', label='my_transfer', children=antd_transfer()),
                display.tab_item(key='tree_select', label='tree_select', children=antd_tree_select()),
                display.tab_item(key='upload', label='upload', children=antd_upload()),
            ]),
            on_change=DataLoadState.set_active_key,
            style=dict(
                width='100%',

            ),
        ),
    )
