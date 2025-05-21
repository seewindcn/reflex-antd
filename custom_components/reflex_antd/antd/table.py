from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, JsValue, ExTypes, PropBase, ReactNode
from ..constant import StatusType, SizeType


class Column(PropBase):
    align: str = None
    class_name: str = None
    col_span: int = None
    data_index: str | list[str] = None
    default_filtered_value: list[str] = None
    filter_reset_to_default_filtered_value: bool = None
    default_sort_order: str = None
    ellipsis: bool | dict = None
    filter_dropdown: ReactNode | ExTypes = None
    filtered: bool = None
    filtered_value: list[str] = None
    filter_icon: ReactNode | ExTypes = None
    filter_on_close: bool = None
    filter_multiple: bool = None
    filter_mode: str = None
    filter_search: bool | ExTypes = None
    filters: bool | list[dict] | ExTypes = None
    filter_dropdown_props: dict | ExTypes = None
    fixed: bool | str = None
    key: str = None
    render: ExTypes = None
    responsive: dict | ExTypes = None
    row_scope: dict | ExTypes = None
    should_cell_update: ExTypes = None
    show_sorter_tooltip: bool | ExTypes = None
    sort_directions: list[str] = None
    sorter: bool | ExTypes = None
    sort_order: str = None
    sort_icon: ReactNode | ExTypes = None
    title: ReactNode | ExTypes = None
    width: str | int = None
    min_width: str | int = None
    hidden: bool = None

    on_cell: ExTypes = None
    on_filter: ExTypes = None
    on_header_cell: ExTypes = None


class Table(AntdComponent):
    tag = 'Table'

    bordered: Var[bool]
    columns: Var[list[dict] | list[Column] | ContainVar]
    components: Var[Union[ContainVar, dict]]
    data_source: Var[List[Dict[str, Any]]]
    expandable: Var[ContainVar]
    footer: Var[JsValue]
    get_popup_container: Var[JsValue]
    loading: Var[bool]
    locale: Var[ContainVar]
    pagination: Var[Union[bool, ContainVar]]
    row_class_name: Var[Union[str, JsValue]]
    row_key: Var[Union[str, JsValue]]
    row_selection: Var[ContainVar]
    scroll: Var[Union[ContainVar, Dict]]
    show_header: Var[bool]
    show_sorter_tooltip: Var[Union[bool, ContainVar]]
    size: Var[SizeType]
    sort_directions: Var[ContainVar]
    sticky: Var[Union[bool, JsValue]]
    summary: Var[JsValue]
    table_layout: Var[str]
    title: Var[JsValue]
    virtual: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda pagination, filters, sorter: [pagination, filters, sorter],
            'on_header_row': lambda columns, index: [columns, index],
            'on_row': lambda record, index: [record, index],
            'on_scroll': lambda ev: [ev],

            'columns.*.on_header_cell': lambda column: [column],
            'columns.*.on_cell': lambda record, row_index: [record, row_index],
            'columns.*.on_filter': lambda: [],
            'columns.*.on_filter_dropdown_open_change': lambda visible: [visible],

            'pagination.on_change': lambda page, size: [page, size],
            'pagination.on_show_size_change': lambda current, size: [current, size],

            'expandable.on_expand': lambda record, event: [record, event],
            'expandable.on_expanded_rows_change': lambda rows: [rows],

            'row_selection.on_cell': lambda record, index: [record, index],
            'row_selection.on_change': lambda keys, rows, info: [keys, info],
            'row_selection.on_select': lambda record, selected, selected_rows: [record, selected, selected_rows],
            'row_selection.on_select_all':
                lambda selected, selected_rows, change_rows: [selected, selected_rows, change_rows],
        })
        return _triggers


table = Table.create
