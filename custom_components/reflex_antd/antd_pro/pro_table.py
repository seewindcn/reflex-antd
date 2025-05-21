from __future__ import annotations
from typing import Dict, Any, List, Optional, Union, Callable, Any

import reflex as rx
from reflex import Component, Var
from reflex.event import EventHandler, passthrough_event_spec, no_args_event_spec

from ..base import ReactNode, ExTypes, PropBase
from ..antd.table import Table, Column as _Column

from .base import AntdProBaseComponent
from .pro_form import FormProps


class SearchProps(PropBase):
    enter_button: ReactNode = None
    loading: bool = None
    label_width: str  # auto|
    on_search: ExTypes = None

    # input's props
    allow_clear: bool | ExTypes = None
    disabled: bool = None
    value: str = None

    on_change: ExTypes = None
    on_press_enter: ExTypes = None
    on_clear: ExTypes = None


class Setting(PropBase):
    icon: ReactNode = None
    tooltip: str = None
    key: str = None
    on_click: ExTypes = None


class ListToolBarMenu(PropBase):
    type: str = None
    active_key: str = None
    items: ExTypes = None

    on_change: ExTypes = None


class ListToolBarTabs(PropBase):
    active_key: str = None
    items: ExTypes = None

    on_change: ExTypes = None


class ListToolBarProps(PropBase):
    title: ReactNode = None
    sub_title: ReactNode = None
    tooltip: str = None
    search: dict | ReactNode | SearchProps = None
    actions: list[ReactNode] = None
    settings: list[ReactNode | Setting] = None
    filter: ReactNode = None
    multiple_line: bool = None
    menu: ListToolBarMenu = None
    tabs: ListToolBarTabs = None


class TableDropdown(PropBase):
    key: str = None
    name: ReactNode = None


class TableRowEditable(PropBase):
    type: str
    form: ExTypes = None
    form_props: FormProps = None
    editable_keys: list[str] = None
    save_text: ReactNode = None
    delete_text: ReactNode = None
    cancel_text: ReactNode = None

    action_render: ExTypes = None
    delete_popconfirm_message: ReactNode = None
    only_one_line_editor_alert_message: ReactNode = None
    only_add_one_line_alert_message: ReactNode = None

    on_change: ExTypes = None
    on_save: ExTypes = None
    on_delete: ExTypes = None
    on_cancel: ExTypes = None


class ColumnStateType(PropBase):
    default_value: ExTypes | dict = None
    value: ExTypes | dict = None
    persistence_key: str | int = None
    persistence_type: str = None

    on_change: ExTypes = None


class Column(_Column):
    copyable: bool = None
    value_enum: dict | ExTypes = None
    value_type: str | ExTypes = None
    order: int = None
    field_props: ExTypes = None
    form_item_props: dict | ExTypes = None
    search: bool | ExTypes | dict = None
    search_transform: ExTypes = None
    editable: bool | ExTypes = None
    col_size: int = None
    hide_in_search: bool = None
    hide_in_table: bool = None
    hide_in_form: bool = None
    hide_in_descriptions: bool = None
    request: ExTypes = None
    initial_value: Any = None
    disable: bool | dict | ExTypes = None
    tooltip: ReactNode = None

    render_text: ExTypes = None
    render_form_item: ExTypes = None


class SettingOptionType(PropBase):
    draggable: bool = None
    checkable: bool = None
    show_list_item_option: bool = None
    checked_reset: bool = None
    lists_height: int = None
    extra: ReactNode = None
    children: ReactNode = None
    setting_icon: ReactNode = None


class SearchConfig(PropBase):
    filter_type: str = None  # 'query' | 'light'
    search_text: str = None
    reset_text: str = None
    submit_text: str = None
    label_width: str = None  # 'number' | 'auto'
    span: str = None
    class_name: str = None
    collapse_render: ExTypes | bool = None
    default_collapsed: bool = None
    collapsed: bool = None
    on_collapse: ExTypes = None
    option_render: ExTypes | bool = None
    show_hidden_num: bool = None


class OptionConfig(PropBase):
    density: bool = True
    full_screen: bool | ExTypes = False
    reload: bool | ExTypes = True
    setting: bool | SettingOptionType = True
    search: bool | ExTypes = None
    reload_icon: ReactNode = None
    density_icon: ReactNode = None


class ProTable(AntdProBaseComponent, Table):
    tag = 'ProTable'
    _rename_props = {
        "searchTransform": "search.transform",
    }

    columns: Var[list[dict] | ExTypes]
    request: Var[ExTypes]
    params: Var[dict | ExTypes]
    post_data: Var[ExTypes]
    default_data: Var[list]
    data_source: Var[list]
    table_class_name: Var[str]
    table_style: Var[dict | ExTypes]
    options: Var[bool | OptionConfig]
    search: Var[bool | dict | ExTypes | SearchConfig]
    default_size: Var[str | int]
    date_formatter: Var[bool | str | ExTypes]
    before_search_submit: Var[ExTypes]
    type: Var[str]
    form: Var[dict | ExTypes]
    column_empty_text: Var[str | bool]
    toolbar: Var[dict | ExTypes]

    tool_bar_render: Var[ExTypes]
    table_render: Var[ExTypes]
    table_extra_render: Var[ExTypes]
    manual_request: Var[bool]
    editable: Var[dict | TableRowEditable]
    card_bordered: Var[bool | dict]
    ghost: Var[bool]
    debounce_time: Var[int]
    revalidate_on_focus: Var[bool]
    columns_state: Var[dict | ColumnStateType]
    Error_boundary: Var[bool | ReactNode]

    on_data_source_change: EventHandler[passthrough_event_spec(list)]
    on_load: EventHandler[passthrough_event_spec(list)]
    on_loading_change: EventHandler[passthrough_event_spec(bool)]
    on_request_error: EventHandler[passthrough_event_spec(Any)]
    on_size_change: EventHandler[passthrough_event_spec(str)]
    on_submit: EventHandler[passthrough_event_spec(dict)]
    on_reset: EventHandler[no_args_event_spec]


    action_ref: Var[ExTypes]
    form_ref: Var[ExTypes]


    tip: Var[ReactNode]
    icon: Var[ReactNode]
    status: Var[str]
    description: Var[ReactNode | ExTypes]
    layout: Var[str]
    trend: Var[str]


class RecordCreator(PropBase):
    record: str | int = None
    position: str = None


class EditableProTable(ProTable):
    tag = 'EditableProTable'

    value: Var[list | ExTypes]
    record_creator_props: Var[dict | RecordCreator | ExTypes]
    max_length: Var[int]
    editable: Var[dict | TableRowEditable]
    controlled: Var[bool]
    editable_form_ref: ExTypes

    on_change: EventHandler[passthrough_event_spec(list)]


pro_table = ProTable.create
edit_pro_table = EditableProTable.create
