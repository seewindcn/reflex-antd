from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, PlacementType, TypeType


class Tour(AntdComponent):
    tag = 'Tour'

    arrow: Optional[Var[bool]]
    close_icon: Optional[Var[ReactNode]]
    disabled_interaction: Optional[Var[bool]]
    placement: Optional[Var[PlacementType]]
    mask: Optional[Var[Union[bool, Dict]]]
    type: Optional[Var[TypeType]]
    open: Optional[Var[bool]]
    current: Optional[Var[int]]
    scroll_into_view_options: Optional[Var[Union[bool, Dict]]]
    steps: Optional[Var[ContainVar]]
    indicators_render: Optional[Var[JsValue]]
    z_index: Optional[Var[int]]
    get_popup_container: Optional[Var[JsValue]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_close': lambda: [],
            'on_finish': lambda: [],
            EventTriggers.ON_CHANGE: lambda current: [current],
            'steps.*.on_close': lambda: [],
        })
        return _triggers


tour = Tour.create

