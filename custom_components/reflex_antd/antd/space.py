from typing import Optional, Union, Dict

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import AlignType, DirectionType, SizeType


class Space(AntdComponent):
    tag = 'Space'

    align: Optional[Var[AlignType]]
    class_names: Optional[Var[Dict]]
    direction: Optional[Var[DirectionType]]
    size: Optional[Var[SizeType]]
    split: Optional[Var[ReactNode]]
    styles: Optional[Var[Dict]]
    wrap: Optional[Var[bool]]


class SpaceCompact(AntdComponent):
    tag = 'Space.Compact'

    block: Optional[Var[bool]]
    direction: Optional[Var[DirectionType]]
    size: Optional[Var[SizeType]]


space = Space.create
space_compact = SpaceCompact.create

