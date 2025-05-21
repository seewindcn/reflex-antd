from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent
from ..constant import OrientationType, DirectionType


class Flex(AntdComponent):
    tag = 'Flex'

    vertical: Var[bool]
    wrap: Var[str | bool]
    justify: Var[str]
    align: Var[str]
    flex: Var[str]
    gap: Var[str | int]
    component: Var[str]


flex = Flex.create

