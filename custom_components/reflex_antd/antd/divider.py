from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ReactNode
from ..constant import OrientationType, DirectionType


class Divider(AntdComponent):
    tag = 'Divider'

    dashed: Var[bool]
    variant: Var[str]
    orientation: Var[OrientationType]
    orientation_margin: Var[Union[int, str]]
    plain: Var[bool]
    type: Var[DirectionType]


divider = Divider.create

