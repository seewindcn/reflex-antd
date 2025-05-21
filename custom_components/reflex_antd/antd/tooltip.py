from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, PlacementType, TriggerType


class Tooltip(AntdComponent):
    tag = "Tooltip"

    title: Var[Union[ReactNode, JsValue]]
    align: Var[str]
    arrow: Var[Union[bool, Dict]]
    auto_adjust_overflow: Var[bool]
    color: Var[str]
    default_open: Var[bool]
    destroy_tooltip_on_hide: Var[bool]
    fresh: Var[bool]
    get_popup_container: Var[JsValue]
    mouse_enter_delay: Var[int]
    mouse_leave_delay: Var[int]
    overlay_class_name: Var[str]
    overlay_style: Var[Dict]
    overlay_inner_style: Var[Dict]
    placement: Var[PlacementType]
    trigger: Var[Union[TriggerType, List[TriggerType]]]
    open: Var[bool]
    z_index: Var[int]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
        })
        return _triggers


tooltip = Tooltip.create

