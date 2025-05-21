from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, SelectModeType, PlacementType, VariantType


class Switch(AntdComponent):
    tag = 'Switch'

    auto_focus: Var[bool]
    checked: Var[bool]
    checked_children: Var[ReactNode]
    default_checked: Var[bool]
    default_value: Var[bool]
    disabled: Var[bool]
    loading: Var[bool]
    size: Var[SizeType]
    un_checked_children: Var[ReactNode]
    value: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda checked, e: [checked, e],
            EventTriggers.ON_CLICK: lambda checked, e: [checked, e],
        })
        return _triggers


switch = Switch.create

