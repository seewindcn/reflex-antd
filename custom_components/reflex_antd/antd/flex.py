from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent
from ..constant import OrientationType, DirectionType


class Flex(AntdComponent):
    tag = 'Flex'

    vertical: Optional[Var[bool]]
    wrap: Optional[Var[str | bool]]
    justify: Optional[Var[str]]
    align: Optional[Var[str]]
    flex: Optional[Var[str]]
    gap: Optional[Var[str | int]]
    component: Optional[Var[str]]


flex = Flex.create

