from typing import Optional, Union, Dict, Any, List
from reflex import Var
from reflex.constants import EventTriggers
from reflex.utils import imports

from ..base import AntdComponent, ContainVar
from ..constant import StatusType, SizeType

from .pagination import Pagination


class Table(AntdComponent):
    tag = 'Table'

    data_source: Optional[Var[List[Dict[str, Any]]]]
    columns: Optional[Var[Union[ContainVar, list]]]
    pagination: Optional[Var[Union[bool, ContainVar]]]
    row_selection: Optional[Var[Union[ContainVar, Dict]]]
    expandable: Optional[Var[Union[ContainVar, Dict]]]
    scroll: Optional[Var[Union[ContainVar, Dict]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda pagination, filters, sorter: [pagination, filters, sorter],
            'row_selection.on_change': lambda keys, rows: [keys],
            'pagination.on_change': lambda page, size: [page, size],
        })
        return _triggers

    def get_imports(self) -> imports.ImportDict:
        _imports = super().get_imports()
        return _imports


table = Table.create


