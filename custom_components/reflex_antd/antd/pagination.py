from typing import Optional, List, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent


class Pagination(AntdComponent):
    tag = 'Pagination'

    current: Optional[Var[int]]
    default_current: Optional[Var[int]]
    default_page_size: Optional[Var[int]]
    disabled: Optional[Var[bool]]
    hide_on_single_page: Optional[Var[bool]]
    page_size: Optional[Var[int]]
    page_size_options: Optional[Var[List[int]]]
    responsive: Optional[Var[bool]]
    show_less_items: Optional[Var[bool]]
    show_quick_jumper: Optional[Var[bool]]
    show_size_changer: Optional[Var[bool]]
    show_title: Optional[Var[bool]]
    # showTotal
    simple: Optional[Var[bool]]
    size: Optional[Var[int]]
    total: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda page, page_size: [page, page_size],
            "show_total": lambda total,range: [total,range],
        })
        return _triggers


pagination = Pagination.create
