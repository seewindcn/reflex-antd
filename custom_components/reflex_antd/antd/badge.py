from typing import Optional, Union, Dict, Any
from reflex import Var, Component

from ..base import AntdComponent, NodeVar
from ..constant import PlacementType, SizeType, BadgeStatusType


class Badge(AntdComponent):
    tag = "Badge"

    color: Var[str]
    count: Var[Union[int, NodeVar]]
    dot: Var[bool]
    offset: Var[NodeVar]
    overflow_count: Var[int]
    show_zero: Var[bool]
    size: Var[SizeType]
    status: Var[BadgeStatusType]
    text: Var[Union[str, Component]]
    styles: Var[Dict]


class BadgeRibbon(AntdComponent):
    tag = 'Badge.Ribbon'

    color: Var[str]
    placement: Var[PlacementType]
    text: Var[Union[str, NodeVar]]


badge = Badge.create
badge_ribbon = BadgeRibbon.create
