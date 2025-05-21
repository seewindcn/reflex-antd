from typing import Optional, List, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent


class Pagination(AntdComponent):
    tag = 'Pagination'

    current: Var[int]
    default_current: Var[int]
    default_page_size: Var[int]
    disabled: Var[bool]
    hide_on_single_page: Var[bool]
    page_size: Var[int]
    page_size_options: Var[List[int]]
    responsive: Var[bool]
    show_less_items: Var[bool]
    show_quick_jumper: Var[bool]
    show_size_changer: Var[bool]
    show_title: Var[bool]
    # showTotal
    simple: Var[bool]
    size: Var[int]
    total: Var[int]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda page, page_size: [page, page_size],
            "show_total": lambda total,range: [total,range],
        })
        return _triggers


pagination = Pagination.create
