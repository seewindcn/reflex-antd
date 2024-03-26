from typing import Optional, Union, Dict, Any, List
import random
import uuid
import reflex as rx
from reflex import State, Var

from reflex_antd import general, entry, display, helper, navigation

from antd_demo.layout import page
from ..state import GlobalState

_data: list[dict[str, Any]] = [
    dict(key='1', name='Fike', age=32, gender='male', address='11 Downing Street', ),
    dict(key='2', name='John', age=42, gender='female', address='12 Downing Street', ),
    dict(key='3', name='Aim', age=22, gender='male', address='13 Downing Street', ),
    dict(key='4', name='Expandable', age=52, gender='female', address='14 Downing Street', ),
    dict(key='5', name='Black', age=62, gender='male', address='15 Downing Street', ),
]
_data = [
    dict(key=i, name=str(uuid.uuid4().hex), age=random.randint(1, 100),
         gender=random.choice(['male', 'female']), address=str(random.randbytes(n=20)))
    for i in range(100)
]

_gender_filter = [
    dict(text="Male", value="male"),
    dict(text="Female", value="female"),
]


class TableState(State):
    row_select_type = 'checkbox'  # checkbox | radio
    selected_row_keys: List[int] = []
    table_gender_filter = [
        dict(text="Male", value="male"),
        dict(text="Female", value="female"),
    ]
    data_source: list[dict[str, Any]] = _data[:]

    columns = [
        dict(title='Id', dataIndex='key', key='key', ),
        dict(title='Name', dataIndex='name', key='name', ),
        dict(title='Age', dataIndex='age', key='age', ),
        dict(title='Address', dataIndex='address', key='address', ),
    ]

    page_current: int = 1
    page_size: int = 10
    total: int = len(_data)
    filters: Dict[str, List[str]] = {}

    @rx.var
    def selected_row_count(self) -> str:
        return str(len(self.selected_row_keys))

    @classmethod
    def get_columns(cls):
        ex_columns = helper.contains([
            dict(
                title='Id',
                dataIndex='key',
                key='key',
                width=50,
                sorter=True,
                defaultSortOrder='descend',
                render=helper.js_value(
                    '(text) => <a>{text}</a>',
                ),
            ),
            dict(
                title='Name',
                dataIndex='name',
                key='name',
                sorter=True,
                render=helper.js_value(
                    lambda text: ' <a>{text}</a>',
                ),
            ),
            dict(
                title='Age',
                dataIndex='age',
                key='age',
                sorter=True,
                render=helper.js_value(
                    lambda text: rx.badge(Var.create_safe('{text}'))
                ),
            ),
            dict(
                title='Gender',
                dataIndex='gender',
                key='gender',
                filters=cls.table_gender_filter,
                defaultFilteredValue=cls.filters['gender'],
                # filters=_gender_filter,
            ),
            dict(
                title='Address',
                dataIndex='address',
                key='address',
                hidden=False,
                ellipsis='true',
                copyable='true',
            ),
            dict(
                title='Action',
                key='action',
                fixed='right',
                render=helper.js_value(
                    lambda _, record: rx.menu.root(
                        rx.menu.trigger(
                            rx.button("Options", variant="soft"),
                        ),
                        rx.menu.content(
                            rx.menu.item("Edit", shortcut="⌘ E"),
                            rx.menu.item("Duplicate", shortcut="⌘ D",
                                         on_select=lambda _: GlobalState.on_event1(Var.create_safe('("Duplicate:" + record.key)'))
                                         ),
                            rx.menu.separator(),
                            rx.menu.item("Archive", shortcut="⌘ N"),
                            rx.menu.sub(
                                rx.menu.sub_trigger("More"),
                                rx.menu.sub_content(
                                    rx.menu.item("Move to project…"),
                                    rx.menu.item("Move to folder…"),
                                    rx.menu.separator(),
                                    rx.menu.item("Advanced options…"),
                                ),
                            ),
                            rx.menu.separator(),
                            rx.menu.item("Share"),
                            rx.menu.item("Add to favorites"),
                            rx.menu.separator(),
                            rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                        ),
                    )
                ),
            ),
        ])
        return ex_columns

    def on_load(self):
        self.on_table_change(
            pagination={}, filters={},
            sorter=dict(column='key', field='key', order='descend'),
        )

    def on_table_change(self, pagination, filters, sorter):
        print("on_table_change:", pagination, filters, sorter)
        self.page_current = int(pagination.get('current', self.page_current))
        self.page_size = int(pagination.get('pageSize', self.page_size))
        my_data = _data[:]

        _filters = filters if filters else self.filters
        if _filters:
            _filters = dict((k, v) for k, v in _filters.items() if v is not None)
            self.filters = _filters
            if 'gender' in _filters:
                my_data = [d for d in _data if d['gender'] in _filters['gender']]
                # test filter items change
                # if len(_filters['gender']) >= 2 and self.table_gender_filter[-1]['text'] != 'Test':
                #     self.table_gender_filter.append(dict(text="Test", value="test"))
                # elif self.table_gender_filter[-1]['text'] == 'Test':
                #     self.table_gender_filter.pop(-1)
        self.total = len(my_data)

        if sorter and sorter['column'] is not None:
            field, order = sorter['field'], sorter['order']
            my_data = sorted(my_data, key=lambda d: d[field], reverse=bool(order == 'descend'))

        # page
        idx = (self.page_current - 1) * self.page_size
        self.data_source = my_data[idx: idx + self.page_size]

    def on_row_select_change(self, selected_row_keys):
        print("on_row_select_change:", selected_row_keys)
        self.selected_row_keys = list(set(self.selected_row_keys + selected_row_keys))

    def on_clean_selected(self):
        self.selected_row_keys = []

    def on_page_change(self, page, size):
        print("on_page_change:", page, size)


@page('/display/table1')
def table1_page() -> rx.Component:
    return rx.center(
        display.table(
            data_source=TableState.data_source,
            columns=TableState.columns,
        ),
    )


@page('/display/table2',
      on_load=TableState.on_load,
      )
def table2_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.button('clear Select', on_click=TableState.on_clean_selected),
                rx.text('selected_row_count: ' + TableState.selected_row_count)
            ),
            display.table(
                data_source=TableState.data_source,
                columns=TableState.get_columns(),
                row_selection=helper.contains(
                    _name_='row_selection',
                    type=TableState.row_select_type,
                    selected_row_keys=TableState.selected_row_keys,
                    onChange=helper.js_event(TableState.on_row_select_change, 'keys', 'rows'),
                ),
                expandable=helper.contains(
                    expandedRowRender=helper.js_value(
                        lambda record: '<p style={{ margin: 0 }}>{record.address}</p>'
                    ),
                    rowExpandable=helper.js_value(
                        lambda record: "record.age >= 50",
                    ),
                ),
                pagination=helper.contains(
                    current=TableState.page_current,
                    total=TableState.total,
                    page_size=TableState.page_size,
                    page_size_options=[5, 10, 20, 50, 100, 150, 200],
                    on_change=helper.js_event(TableState.on_page_change, 'page', 'size'),
                    showTotal=helper.js_value('((total, range) => `${range[0]}-${range[1]} of ${total} items`)'),
                    showSizeChanger=True,
                    showQuickJumper=True,
                ),
                scroll=dict(y=500),
                on_change=TableState.on_table_change,
            ),
        ),
    )
