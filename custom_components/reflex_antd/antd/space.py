from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, Component
from ..constant import AlignType, DirectionType, SizeType


class Space(AntdComponent):
    tag = 'Space'

    align: Optional[Var[AlignType]]
    direction: Optional[Var[DirectionType]]
    size: Optional[Var[SizeType]]
    wrap: Optional[Var[bool]]
    split: Optional[Var[Component]]


class SpaceCompact(AntdComponent):
    tag = 'Space.Compact'

    block: Optional[Var[bool]]
    direction: Optional[Var[DirectionType]]
    size: Optional[Var[SizeType]]


space = Space.create
space_compact = SpaceCompact.create

