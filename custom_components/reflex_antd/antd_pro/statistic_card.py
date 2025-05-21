from typing import Dict, Any, List, Optional, Union, Callable

import reflex as rx
from reflex import Component, Var

from ..base import ReactNode, ExTypes
from ..antd import statistic

from .base import AntdProBaseComponent
from .pro_card import ProCard


class Statistic(statistic.Statistic):
    tag = 'StatisticCard.Statistic'

    tip: Var[ReactNode]
    icon: Var[ReactNode]
    status: Var[str]
    description: Var[ReactNode | ExTypes]
    layout: Var[str]
    trend: Var[str]


class Divider(AntdProBaseComponent):
    tag = 'StatisticCard.Divider'

    type: Var[str]


class Operation(AntdProBaseComponent):
    tag = 'StatisticCard.Operation'


class StatisticCard(ProCard):
    """StatisticCard 统计数值卡片。
    一个简单的卡片，用于展示统计数值和相关信息。
    参考: https://procomponents.ant.design/components/statistic-card
    """

    tag = "StatisticCard"

    chart: Var[ReactNode]
    statistic: Var[ExTypes | ReactNode | Statistic]
    chart_placement: Var[str]
    footer: Var[ReactNode]


class StatisticCardGroup(StatisticCard):
    """StatisticCard.Group 统计数值卡片组。
    """
    tag = "StatisticCard.Group"


statistic_card = StatisticCard.create
statistic_card_group = StatisticCardGroup.create
statistic = Statistic.create
divider = Divider.create
operation = Operation.create

