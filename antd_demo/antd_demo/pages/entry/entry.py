import time
from typing import List, Any, Dict, Optional
import asyncio

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout, feedback, navigation

from antd_demo.layout import page


class AntdEntryPage(State):
    active_key: str = "autoComplete"


class EntryAutoComplateState(State):
    options: list[dict] = []

    def on_select(self, value, option):
        print(value, option)

    def on_search(self, value):
        if value:
            self.options = [
                {"value": "{value}".format(value=value)},
                {"value": "{value}{value}".format(value=value)},
                {"value": "{value}{value}{value}".format(value=value)},
            ]


@rx.memo
def antd_entry_auto_complete() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "基本使用，通过 options 设置自动完成的数据源。",
            ),
            entry.auto_complete(
                placeholder="Enter your",
                style={"width": 200},
                options=EntryAutoComplateState.options,
                on_search=EntryAutoComplateState.on_search,
                on_select=EntryAutoComplateState.on_select
            )
        ),
        width="100%",
    )


class EntryCascaderState(State):
    default_value: list[str] = ['zhejiang', 'hangzhou', 'xihu']
    options: list[dict] = [
        {
            "value": 'zhejiang',
            "label": 'Zhejiang',
            "children": [
                {
                    "value": 'hangzhou',
                    "label": 'Hangzhou',
                    "children": [
                        {
                            "value": 'xihu',
                            "label": 'West Lake',
                        },
                    ],
                },
            ],
        },
        {
            "value": 'jiangsu',
            "label": 'Jiangsu',
            "children": [
                {
                    "value": 'nanjing',
                    "label": 'Nanjing',
                    "children": [
                        {
                            "value": 'zhonghuamen',
                            "label": 'Zhong Hua Men',
                        },
                    ],
                },
            ],
        },
    ]


@rx.memo
def antd_entry_cascader() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "省市区级联。",
            ),
            entry.cascader(
                options=EntryCascaderState.options,
                placeholder="Please select"
            ),
            rx.text(
                "默认值通过数组的方式指定。",
            ),
            entry.cascader(
                default_value=EntryCascaderState.default_value,
                options=EntryCascaderState.options,
                placeholder="Please select"
            ),

        ),
        width="100%",
    )


class EntryCheckboxState(State):
    plainOptions: list = ['Apple', 'Pear', 'Orange']
    defaultCheckedList: list = ['Apple', 'Orange']
    options: list[dict] = [
        {"label": 'Apple', "value": 'Apple'},
        {"label": 'Pear', "value": 'Pear'},
        {"label": 'Orange', "value": 'Orange'},
    ]

    def onCheckAllChange(self, checked_value):
        if checked_value['target']['checked']:
            self.defaultCheckedList = ['Apple', 'Pear', 'Orange']
        else:
            self.defaultCheckedList = []


@rx.memo
def antd_entry_checkbox() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "简单的 checkbox。",
            ),
            entry.checkbox(),
            rx.text(
                "checkbox 不可用。",
            ),
            entry.checkbox(disabled=True, default_checked=False),
            entry.checkbox(indeterminate=True, disabled=True),
            entry.checkbox(default_checked=True, disabled=True),
            rx.text(
                "方便的从数组生成 Checkbox 组。",
            ),
            entry.checkbox_group(
                options=EntryCheckboxState.plainOptions,
                default_value=["Apple"]
            ),
            rx.text(
                "实现全选效果。",
            ),
            entry.checkbox(
                "Check all",
                on_change=EntryCheckboxState.onCheckAllChange
            ),
            entry.checkbox_group(
                options=EntryCheckboxState.plainOptions,
                value=EntryCheckboxState.defaultCheckedList
            ),

        ),
        width="100%",
    )


class EntryColorPickerState(State):
    default_value: str = '#1677ff'


@rx.memo
def antd_entry_color_picker() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "最简单的使用方法。",
            ),
            entry.color_picker()
        ),
        width="100%",
    )


@rx.memo
def antd_entry_date_picker() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("最简单的用法，在浮层中可以选择或者输入日期。"),
            entry.date_picker(),
            entry.date_picker(picker="week"),
            entry.date_picker(picker="month"),
            entry.date_picker(picker="quarter"),
            entry.date_picker(picker="year"),
            rx.text("通过设置 picker 属性，指定范围选择器类型。"),
            entry.range_picker(),
            entry.range_picker(picker="year")
        ),
        width="100%",
    )


class EntryFormState(State):
    formLayout: str = 'horizontal'
    componentDisabled: bool = False

    def on_values_change(self, changed, all):
        self.formLayout = changed['layout']

    def on_change(self, checked_value):
        self.componentDisabled = checked_value['target']['checked']


@rx.memo
def antd_entry_form() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("基本的表单数据域控制展示，包含布局、初始化、验证、提交。"),
            entry.form(
                entry.form_item(
                    entry.input(),
                    name="username",
                    label="username",
                    rules=[{"required": True, "message": 'Please input your username!'}]
                ),
                entry.form_item(
                    entry.password(),
                    name="password",
                    label="password",
                    rules=[{"required": True, "message": 'Please input your password!'}]
                ),
                entry.form_item(
                    entry.checkbox(
                        "Remember me"
                    ),
                    name="remember",
                    value_prop_name="checked",
                    wrapper_col={"offset": 8, "span": 16},
                ),
                entry.form_item(
                    general.button("Submit", html_type="submit"),
                    wrapper_col={"offset": 8, "span": 16},
                ),
                name="basic",
                label_col={"span": 8},
                style={"maxWidth": "600"},
                initial_values={"remember": True},

            ),
            rx.text("表单有三种布局。"),
            entry.form(
                entry.form_item(
                    entry.radio_group(
                        entry.radio_button("Horizontal", value="horizontal"),
                        entry.radio_button("Vertical", value="vertical"),
                        entry.radio_button("Inline", value="inline"),
                        value=EntryFormState.formLayout
                    ),
                    label="Form Layout",
                    name="layout"
                ),
                entry.form_item(
                    entry.input(placeholder="input placeholder"),
                    label="Field A"
                ),
                entry.form_item(
                    entry.input(placeholder="input placeholder"),
                    label="Field B"
                ),
                entry.form_item(
                    rx.button("Submit")
                ),
                on_values_change=EntryFormState.on_values_change,
                initial_values={"layout": EntryFormState.formLayout},
                layout=EntryFormState.formLayout
            ),
            rx.text("设置表单组件禁用，仅对 antd 组件有效。"),
            entry.checkbox(
                "Form disabled",
                checked=EntryFormState.componentDisabled,
                on_change=EntryFormState.on_change
            ),
            entry.form(
                entry.form_item(
                    entry.checkbox("Checkbox"),
                    label="Checkbox",
                    name="disabled",
                    valuePropName="checked",
                ),
                entry.form_item(
                    entry.radio_group(
                        entry.radio("Apple", value="apple"),
                        entry.radio("Pear", value="pear"),
                    ),
                    label="Radio"
                ),
                entry.form_item(
                    entry.input(),
                    label="Input"
                ),
                entry.form_item(
                    entry.select(
                        options=[
                            {"value": "http://", "label": "http://"},
                            {"value": "https://", "label": "https://"}
                        ]
                    ),
                    label="Select"
                ),
                entry.form_item(
                    entry.tree_select(
                        tree_data=[
                            {"title": "Light", "value": "Light", "children": [{"value": "Bamboo", "label": "Bamboo"}]},
                        ]
                    ),
                    label="TreeSelect"
                ),
                entry.form_item(
                    entry.cascader(
                        options=[
                            {"value": "zhejiang", "label": "Zhejiang",
                             "children": [{"value": "hangzhou", "label": "hangzhou"}]}
                        ]
                    ),
                    label="Cascader"
                ),
                entry.form_item(
                    entry.date_picker(),
                    label="DatePicker"
                ),
                entry.form_item(
                    entry.range_picker(),
                    label="RangePicker"
                ),
                entry.form_item(
                    entry.input_number(),
                    label="InputNumber"
                ),
                entry.form_item(
                    entry.text_area(),
                    label="TextArea"
                ),
                entry.form_item(
                    entry.switch(),
                    label="Switch",
                    value_prop_name="checked"
                ),
                entry.form_item(
                    entry.upload(
                        general.button(
                            general.icon("PlusOutlined"),
                            rx.text("upload"),
                        ),
                        action="/upload.do",
                        list_type="picture-card",
                    ),
                    label="Upload",
                    value_prop_name="fileList"
                ),
                entry.form_item(
                    general.button("Button"),
                    label="Button",
                ),
                entry.form_item(
                    entry.slider(),
                    label="Slider",
                ),
                entry.form_item(
                    entry.color_picker(),
                    label="color_picker",
                ),

                layout="horizontal",
                disabled=EntryFormState.componentDisabled,
                style={"maxWidth": 600}
            )

        ),
        width="100%",
    )


@rx.memo
def antd_entry_input() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("基本使用。"),
            entry.input(placeholder="Basic usage"),
            entry.input(
                placeholder="large size",
                size="large",
                prefix=general.icon("UserOutlined")
            ),
            entry.input(
                placeholder="default size",
                prefix=general.icon("UserOutlined")
            ),
            entry.input(
                placeholder="default size",
                size="small",
                prefix=general.icon("UserOutlined")
            ),
            rx.text("用于配置一些固定组合。"),
            entry.input(
                addon_before=rx.text("http://"),
                addon_after=rx.text(".com"),
                default_value="mysite",
            ),
            entry.input(
                addon_before=entry.select(
                    default_value="http://",
                    options=[
                        {"value": "http://", "label": "http://"},
                        {"value": "https://", "label": "https://"}
                    ]
                ),
                addon_after=entry.select(
                    default_value=".com",
                    options=[
                        {"value": ".com", "label": ".com"},
                        {"value": ".cn", "label": ".cn"}
                    ]
                ),
                default_value="mysite",
            ),
            layout.space_compact(
                entry.input(
                    default_value="111",
                ),
                general.button(
                    "Submit"
                )
            ),
            rx.text("密码框。"),
            entry.password(
                placeholder="input password"
            )

        ),
        width="100%",
    )


@rx.memo
def antd_entry_inputnumber() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("基本的表单数据域控制展示，包含布局、初始化、验证、提交。"),
            entry.input_number(
                min=1,
                max=10,
                default_value=3
            ),
            rx.text("在输入框上添加前缀图标。"),
            entry.input_number(
                addon_before=general.icon("UserOutlined"),
                prefix=rx.text("￥"),
            ),

        ),
        width="100%",
    )


@page('/entry/entry', 'entry')
def entry_page() -> rx.Component:
    return rx.box(
        display.tabs(
            active_key=AntdEntryPage.active_key,
            default_active_key='autoComplete',
            items=helper.contain([
                display.tab_item(key='autoComplete', label='autoComplete', children=antd_entry_auto_complete()),
                display.tab_item(key='cascader', label='cascader', children=antd_entry_cascader()),
                display.tab_item(key='checkbox', label='checkbox', children=antd_entry_checkbox()),
                display.tab_item(key='color_picker', label='color_picker', children=antd_entry_color_picker()),
                display.tab_item(key='date_picker', label='date_picker', children=antd_entry_date_picker()),
                display.tab_item(key='form', label='form', children=antd_entry_form()),
                display.tab_item(key='input', label='input', children=antd_entry_input()),
                display.tab_item(key='inputnumber', label='inputnumber', children=antd_entry_inputnumber()),
            ]),
            on_change=AntdEntryPage.set_active_key,
        ),
    )
