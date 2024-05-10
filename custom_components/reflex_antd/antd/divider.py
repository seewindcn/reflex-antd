from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ReactNode
from ..constant import OrientationType, DirectionType


class Divider(AntdComponent):
    tag = 'Divider'

    dashed: Optional[Var[bool]]
    orientation: Optional[Var[OrientationType]]
    orientation_margin: Optional[Var[Union[int, str]]]
    plain: Optional[Var[bool]]
    type: Optional[Var[DirectionType]]


divider = Divider.create

