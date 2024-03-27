from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType

from .pagination import Pagination


class Table(AntdComponent):
    tag = 'Table'

    data_source: Optional[Var[List[Dict[str, Any]]]]
    columns: Optional[Var[Union[ContainVar, list]]]
    pagination: Optional[Var[Union[bool, ContainVar]]]
    row_selection: Optional[Var[ContainVar]]
    check_strictly: Optional[Var[bool]]
    expandable: Optional[Var[ContainVar]]
    scroll: Optional[Var[Union[ContainVar, Dict]]]
    footer: Optional[Var[Union[JsValue]]]
    loading: Optional[Var[bool]]
    row_key: Optional[Var[str]]
    show_header: Optional[Var[bool]]


    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda pagination, filters, sorter: [pagination, filters, sorter],
            'row_selection.on_change': lambda keys, rows: [keys],
            'row_selection.on_select': lambda record, selected, selected_rows: [record, selected, selected_rows],
            'row_selection.on_select_all':
                lambda selected, selected_rows, change_rows: [selected, selected_rows, change_rows],
            'pagination.on_change': lambda page, size: [page, size],
        })
        return _triggers

    def get_imports(self) -> imports.ImportDict:
        _imports = super().get_imports()
        return _imports


table = Table.create
