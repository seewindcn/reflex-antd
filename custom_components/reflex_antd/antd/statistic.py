from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType, PlacementType, TabsType


class StatisticBase(AntdComponent):
    prefix: Var[ReactNode]
    suffix: Var[ReactNode]
    title: Var[ReactNode]
    value: Var[Union[str, int]]
    value_style: Var[Dict]


class Statistic(StatisticBase):
    tag = 'Statistic'

    decimal_separator: Var[str]
    formatter: Var[JsValue]
    group_separator: Var[str]
    loading: Var[bool]
    precision: Var[int]


class StatisticCountdown(StatisticBase):
    tag = 'Statistic.Countdown'

    format: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_finish": lambda: [],
            EventTriggers.ON_CHANGE: lambda value: [value],
        })
        return _triggers


statistic = Statistic.create
statistic_countdown = StatisticCountdown.create

