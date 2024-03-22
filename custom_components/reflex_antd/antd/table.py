from typing import Optional, Union, Dict, Any, List
from reflex import Var
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar
from ..constant import StatusType, SizeType


class Table(AntdComponent):
    tag = 'Table'

    data_source: Optional[Var[List[Dict[str, Any]]]]
    columns: Optional[Var[Union[ContainVar, list]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda pagination, filters, sorter: [pagination, filters, sorter],
        })
        return _triggers


table = Table.create


