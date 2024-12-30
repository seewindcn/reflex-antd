from typing import Optional, Union, Dict, Any
from reflex import Var,Component

from ..base import AntdComponent, NodeVar
from ..constant import PlacementType, SizeType, BadgeStatusType


class Badge(AntdComponent):
    tag = "Badge"

    color: Optional[Var[str]]
    count: Optional[Var[Union[int, NodeVar]]]
    dot: Optional[Var[bool]]
    offset: Optional[Var[NodeVar]]
    overflow_count: Optional[Var[int]]
    show_zero: Optional[Var[bool]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[BadgeStatusType]]
    text: Optional[Var[Union[str, Component]]]


class BadgeRibbon(AntdComponent):
    tag = 'Badge.Ribbon'

    color: Optional[Var[str]]
    placement: Optional[Var[PlacementType]]
    text: Optional[Var[Union[str, NodeVar]]]


badge = Badge.create
badge_ribbon = BadgeRibbon.create
