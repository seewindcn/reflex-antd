from typing import Optional, Union, Dict, Any, List

import reflex as rx
from reflex import State, Var

from reflex_antd import general, entry, display, helper

from antd_demo.layout import page
from ..state import GlobalState


_data: list[dict[str, Any]] = [
    dict(key='1', name='Fike', age=32, gender='male', address='11 Downing Street', ),
    dict(key='2', name='John', age=42, gender='female', address='12 Downing Street', ),
    dict(key='3', name='Aim', age=22, gender='male', address='13 Downing Street', ),
    dict(key='4', name='Expandable', age=52, gender='female', address='14 Downing Street', ),
    dict(key='5', name='Black', age=62, gender='male', address='15 Downing Street', ),
]

_gender_filter = [
    dict(text="Male", value="male"),
    dict(text="Female", value="female"),
]


class TableState(State):
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

    def on_table_change(self, pagination, filters, sorter):
        print("on_table_change:", pagination, filters, sorter)
        self.data_source = _data
        if 'gender' in filters and filters['gender'] is not None:
            # test table_gender_filter
            self.data_source = [d for d in _data if d['gender'] in filters['gender']]
            if len(filters['gender']) >= 2 and self.table_gender_filter[-1]['text'] != 'Test':
                self.table_gender_filter.append(dict(text="Test", value="test"))
            elif self.table_gender_filter[-1]['text'] == 'Test':
                self.table_gender_filter.pop(-1)

        if sorter and sorter['column'] is not None:
            field, order = sorter['field'], sorter['order']
            self.data_source = sorted(self.data_source, key=lambda d: d[field], reverse=bool(order == 'descend'))

    @classmethod
    def get_columns(cls):
        ex_columns = helper.contains([
            dict(
                title='Id',
                dataIndex='key',
                key='key',
                sorter='true',
                defaultSortOrder='descend',
                # render=lambda text=None: '<a>{text}</a>',
            ),
            dict(
                title='Name',
                dataIndex='name',
                key='name',
                sorter='true',
                # render=lambda text=None: rx.code(Var.create_safe('{text}')),
            ),
            dict(
                title='Age',
                dataIndex='age',
                key='age',
            ),
            dict(
                title='Gender',
                dataIndex='gender',
                key='gender',
                # filters=cls.table_gender_filter,
                filters=_gender_filter,
            ),
            dict(
                title='Address',
                dataIndex='address',
                key='address',
                ellipsis='true',
                copyable='true',
            ),
        ])
        return ex_columns


@page('/display/table1')
def table1_page() -> rx.Component:
    return rx.center(
        display.table(
            data_source=TableState.data_source,
            columns=TableState.columns,
        ),
    )


@page('/display/table2')
def table2_page() -> rx.Component:
    return rx.center(
        display.table(
            data_source=TableState.data_source,
            columns=TableState.get_columns(),
            on_change=TableState.on_table_change,
        ),
    )
