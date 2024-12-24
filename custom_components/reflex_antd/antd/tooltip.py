from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, PlacementType, TriggerType


class Tooltip(AntdComponent):
    tag = "Tooltip"

    title: Optional[Var[Union[ReactNode, JsValue]]]
    align: Optional[Var[str]]
    arrow: Optional[Var[Union[bool, Dict]]]
    auto_adjust_overflow: Optional[Var[bool]]
    color: Optional[Var[str]]
    default_open: Optional[Var[bool]]
    destroy_tooltip_on_hide: Optional[Var[bool]]
    fresh: Optional[Var[bool]]
    get_popup_container: Optional[Var[JsValue]]
    mouse_enter_delay: Optional[Var[int]]
    mouse_leave_delay: Optional[Var[int]]
    overlay_class_name: Optional[Var[str]]
    overlay_style: Optional[Var[Dict]]
    overlay_inner_style: Optional[Var[Dict]]
    placement: Optional[Var[PlacementType]]
    trigger: Optional[Var[Union[TriggerType, List[TriggerType]]]]
    open: Optional[Var[bool]]
    z_index: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
        })
        return _triggers


tooltip = Tooltip.create

