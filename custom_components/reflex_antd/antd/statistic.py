from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType, PlacementType, TabsType


class StatisticBase(AntdComponent):
    prefix: Optional[Var[ReactNode]]
    suffix: Optional[Var[ReactNode]]
    title: Optional[Var[ReactNode]]
    value: Optional[Var[Union[str, int]]]
    value_style: Optional[Var[Dict]]


class Statistic(StatisticBase):
    tag = 'Statistic'

    decimal_separator: Optional[Var[str]]
    formatter: Optional[Var[JsValue]]
    group_separator: Optional[Var[str]]
    loading: Optional[Var[bool]]
    precision: Optional[Var[int]]


class StatisticCountdown(StatisticBase):
    tag = 'Statistic.Countdown'

    format: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_finish": lambda: [],
            EventTriggers.ON_CHANGE: lambda value: [value],
        })
        return _triggers


statistic = Statistic.create
statistic_countdown = StatisticCountdown.create

