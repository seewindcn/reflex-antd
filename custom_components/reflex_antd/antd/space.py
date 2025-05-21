from typing import Optional, Union, Dict

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import AlignType, DirectionType, SizeType


class Space(AntdComponent):
    tag = 'Space'

    align: Var[AlignType]
    class_names: Var[Dict]
    direction: Var[DirectionType]
    size: Var[SizeType]
    split: Var[ReactNode]
    styles: Var[Dict]
    wrap: Var[bool]


class SpaceCompact(AntdComponent):
    tag = 'Space.Compact'

    block: Var[bool]
    direction: Var[DirectionType]
    size: Var[SizeType]


space = Space.create
space_compact = SpaceCompact.create

