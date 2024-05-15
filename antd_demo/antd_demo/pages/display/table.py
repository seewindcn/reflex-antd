from typing import Optional, Union, Dict, Any, List
import random
import uuid
import reflex as rx
from reflex import State, Var

from reflex_antd import general, entry, display, helper, navigation

from antd_demo.layout import page
from antd_demo.state import GlobalState, MyBaseState


def random_data(i) -> Dict[str, Any]:
    return dict(key=i, name=str(uuid.uuid4().hex), age=random.randint(1, 100),
                gender=random.choice(['male', 'female']), address=str(random.randbytes(n=20)),
                )


def render_children(pi: int) -> List[Dict[str, Any]]:
    return [random_data(pi * 100 + i) for i in range(random.randint(1, 10))]


_data = [
    dict(children=render_children(i) if int(i / 10) % 2 == 0 and i % 2 == 0 else None,
         **random_data(i))
    for i in range(100)
]

_gender_filter = [
    dict(text="Male", value="male"),
    dict(text="Female", value="female"),
]


class TableState(MyBaseState):
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

    async def on_page_load(self):
        g = await self.get_global_state()
        g.update_subnav([('display', table2_page.path if '1' in self.current_path else table1_page.path),
                         ('table', self.current_path)])
        self.on_table_change(
            pagination={}, filters={},
            sorter=dict(column='key', field='key', order='descend'),
        )

    @classmethod
    def get_columns(cls):
        ex_columns = helper.contain([
            dict(
                title='Id',
                dataIndex='key',
                key='key',
                width=100,
                sorter=True,
                defaultSortOrder='descend',
                # render=helper.js_value(
                #     '(text) => <a>{text}</a>',
                # ),
            ),
            dict(
                title='Name',
                dataIndex='name',
                key='name',
                sorter=True,
                render=helper.js_value(
                    lambda text: ' <a>{text}</a>',
                    is_component=True,
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
                # filters=_gender_filter,
                defaultFilteredValue=cls.filters['gender'],
                on_header_cell=helper.js_event(GlobalState.on_event1, js="""
                    console.log("on_header_cell: ", column);
                    var column = column.key;
                    return;
                """)
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
                                         on_select=lambda _: GlobalState.on_event1(
                                             Var.create_safe('("Duplicate:" + record.key)'))
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

    def on_row_select_change(self, keys, info):
        print("on_row_select_change:", keys, info)
        self.selected_row_keys = list(set(self.selected_row_keys + keys))

    def on_row_select(self, record, selected, selected_rows):
        print("on_row_select:", record, selected, selected_rows)
        if not selected:
            self.selected_row_keys = [i for i in self.selected_row_keys if i not in [record, *selected_rows]]

    def on_row_select_all(self, selected, selected_rows, change_rows):
        print("on_row_select_all:", selected, selected_rows, change_rows)
        if not selected:
            self.selected_row_keys = [i for i in self.selected_row_keys if i not in change_rows]

    def on_clean_selected(self):
        self.selected_row_keys = []

    def on_page_change(self, page, size):
        print("on_page_change:", page, size)


@page('/display/table1', 'display', state=TableState)
def table1_page() -> rx.Component:
    return rx.center(
        display.table(
            data_source=TableState.data_source,
            columns=TableState.columns,
        ),
    )


@page('/display/table2', 'display', state=TableState)
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
                # on_header_row=helper.js_value(
                #     lambda columns, index: 'console.log(columns, index);'
                # ),
                row_selection=helper.contain(
                    type=TableState.row_select_type,
                    check_strictly=False,
                    selected_row_keys=TableState.selected_row_keys,
                    on_change=TableState.on_row_select_change,
                    on_select=helper.js_event(TableState.on_row_select, js="""(record, selected, selected_rows) => {
                        if (selected_rows.length > 0) {
                            var selected_rows = selected_rows.map(item => { return item.key });
                        } else if (record.children) {
                            var selected_rows = record.children.map(item => { return item.key });
                        }
                        %(name)s(record.key, selected, selected_rows);
                    }
                    """, fmt=True),
                    on_select_all=helper.js_event(TableState.on_row_select_all, js="""
                    var selected_rows = selected_rows.map(item => { return item.key });
                    var change_rows = change_rows.map(item => { return item.key });
                    """),
                ),
                expandable=helper.contain(
                    children_column_name='children',
                    #    expandedRowRender=helper.js_value(
                    #        lambda record: '<p style={{ margin: 0 }}>{record.address}</p>'
                    #    ),
                    #    rowExpandable=helper.js_value(
                    #        lambda record: "record.age >= 50",
                    #    ),
                ),
                pagination=helper.contain(
                    current=TableState.page_current,
                    total=TableState.total,
                    page_size=TableState.page_size,
                    page_size_options=[5, 10, 20, 50, 100, 150, 200],
                    on_change=TableState.on_page_change,
                    showTotal=helper.js_value('((total, range) => `${range[0]}-${range[1]} of ${total} items`) '),
                    showSizeChanger=True,
                    showQuickJumper=True,
                ),
                scroll=dict(y=500, x=900),
                footer=helper.js_value(lambda: rx.badge('footer-test')),
                on_change=TableState.on_table_change,
                style=dict(
                    width='99%',
                ),
            ),
        ),
        width='100%',
    )
