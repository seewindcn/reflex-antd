from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TimelineModeType


class Tag(AntdComponent):
    tag = 'Tag'

    close_icon: Optional[Var[Union[bool, ReactNode]]]
    color: Optional[Var[str]]
    icon: Optional[Var[ReactNode]]
    bordered: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_close': lambda e: [e],
        })
        return _triggers


class CheckableTag(AntdComponent):
    tag = 'Tag.CheckableTag'

    checked: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda checked: [checked],
        })
        return _triggers


tag = Tag.create
checkable_tag = CheckableTag.create

