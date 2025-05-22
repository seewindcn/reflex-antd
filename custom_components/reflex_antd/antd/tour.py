from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, PlacementType, TypeType


class Tour(AntdComponent):
    tag = 'Tour'

    arrow: Var[bool]
    close_icon: Var[ReactNode]
    disabled_interaction: Var[bool]
    placement: Var[PlacementType]
    mask: Var[Union[bool, Dict]]
    type: Var[TypeType]
    open: Var[bool]
    current: Var[int]
    scroll_into_view_options: Var[Union[bool, Dict]]
    steps: Var[ContainVar]
    indicators_render: Var[JsValue]
    z_index: Var[int]
    get_popup_container: Var[JsValue]

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

