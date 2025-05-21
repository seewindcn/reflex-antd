import logging
from typing import List, Any, Dict, Set
import asyncio
import random
import math
from datetime import datetime, timedelta

import requests
import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout, feedback, pro

from antd_demo.layout import page


value_enum = dict(
    all=dict(text='全部', status='Default'),
    open=dict(text='未解决', status='Error'),
    closed=dict(text='已解决', status='Success', disabled=True),
    processing=dict(text='进行中', status='Processing'),
)

schema_columns_datas = {
    0: [
        dict(title='创建时间', key='showTime', dataIndex='createName', valueType='date'),
        dict(title='分组', valueType='group', columns=[
            dict(title='状态', dataIndex='groupState', valueType='select', valueEnum=value_enum, width='xs'),
            dict(title='标题', dataIndex='groupTitle', width='md',
                 formItemProps=dict(rules=[dict(required=True, message='必填项')])),
        ])
    ],
    1: [
        dict(title='列表', valueType='formList', dataIndex='datas',
             initialValue=[{'state': 'all', 'title': '标题'}], col_props=dict(xs=24, sm=12),
             columns=[
                 dict(valueType='group', columns=[
                     dict(title='状态', dataIndex='state', valueType='select', valueEnum=value_enum, width='xs'),
                     dict(title='标题', dataIndex='title', width='md',
                          formItemProps=dict(rules=[dict(required=True, message='必填项')])),
                 ]),
                 dict(valueType='dateTime', dataIndex='currentTime', width='md'),
             ])
    ],
}


class AntdProState(State):
    range_5: list[int] = list(range(5))
    form_grid: bool = False
    schema_id: int = 0
    schema_columns: list[dict] = []

    def update_schema_columns(self, v):
        logging.info('update_schema_columns: %s', v)
        self.schema_id = int(v)
        # if self.schema_id >= len(schema_columns_datas):
        #     self.schema_id = 0
        self.schema_columns = schema_columns_datas[self.schema_id]
        self.schema_id += 1

    def on_form_finish(self, data: dict):
        logging.info('on_form_finish: %s', data)


def _ui_pro_card() -> rx.Component:
    comp = pro.pro_card(
        pro.pro_card(
            pro.pro_card(
                pro.pro_card(
                    pro.pro_card('123', title='昨日全部流量'),
                    pro.pro_card('234', title='本月累计流量'),
                    pro.pro_card('345', title='今年累计流量'),
                    split='vertical',
                ),
                pro.pro_card(
                    pro.pro_card('12/56', title='运行中试验'),
                    pro.pro_card('134', title='历史试验总数'),
                    split='vertical',
                ),
                pro.pro_card(
                    layout.flex(
                        rx.foreach(
                            AntdProState.range_5,
                            lambda i: rx.heading(f'图表-{i}'),
                        ),
                        vertical=True,
                    ),
                    title='流量趋势',
                ),
                split='horizontal',
            ),
            pro.pro_card(
                '右侧内容',
                title='流量占用情况',
            ),
            title='复杂切分',
            sub_title='sub_title',
            bordered=True,
            header_bordered=True,
            box_shadow=True,
            tooltip='This is tooltip!',
            extra=layout.space('2019年9月28日 -', rx.switch('extra-switch')),
            split='vertical',
        ),
    )
    return comp


def _ui_pro_form() -> rx.Component:
    _form1 = pro.pro_form(
        pro.pro_form_text(name='name', label='标题', tooltip='最长为 24 位', placeholder='请输入名称'),
        pro.pro_form_group(
            pro.pro_form_text(name='company', label='公司', width='md', col_props=dict(md=12, xl=8)),
            pro.pro_form_text(name='phone', label='电话', width='sm', col_props=dict(md=12, xl=8)),
            pro.pro_form_text(name='email', label='邮箱', width='xs', col_props=dict(md=12, xl=8)),
        ),
        pro.pro_form_textarea(name='address', label='详细的工作地址或家庭住址', col_props=dict(span=24)),
        pro.pro_form_date_picker(name='date', label='入职日期', col_props=dict(md=12, xl=8)),
        pro.pro_form_list(
            pro.pro_form_group(
                pro.pro_form_text(name='value', label='值', col_props=dict(md=12, xl=8)),
                pro.pro_form_text(name='label', label='标签', col_props=dict(md=12, xl=8)),
                key='group',
            ),
            col_props=dict(span=24),
            name='labels', label='用户标签',
            initial_value=[dict(value='lb1', label='标签1')],
            copy_icon_props=helper.contain(dict(icon=general.icon('SmileOutlined'), tooltip_text='复制此项到末尾')),
            delete_icon_props=helper.contain(dict(icon=general.icon('CloseCircleOutlined'), tooltip_text='不需要这行了')),
        ),
        layout.space_compact(
            general.typography_title('Embed SchemaForm', level=3),
            entry.select(options=[
                dict(label=i, value=i) for i in schema_columns_datas
            ], on_select=lambda v, option: AntdProState.update_schema_columns(v))
        ),
        pro.schema_form(
            layout_type='Embed',
            columns=AntdProState.schema_columns,
        ),
        layout='horizontal',
        grid=AntdProState.form_grid,
        row_props=dict(gutter=[16, 0],),
        on_finish=AntdProState.on_form_finish,
    )
    return layout.flex(
        pro.pro_card(
            _form1,
            extra=layout.space('grid', rx.switch(
                checked=AntdProState.form_grid,
                on_change=AntdProState.set_form_grid)),
        ),
    )


@page('/demo/antd_pro')
def antd_pro_page() -> rx.Component:
    return rx.box(
        display.tabs(
            # active_key=TabsState.active_key,
            default_active_key='pro_card',
            items=helper.contain(
                [
                    display.tab_item(key='pro_card', label='proCard', children=_ui_pro_card()),
                    display.tab_item(key='pro_form', label='proForm', children=_ui_pro_form()),
                ]
            ),
            width='100%',
            tab_position='left',
        ),
    )
