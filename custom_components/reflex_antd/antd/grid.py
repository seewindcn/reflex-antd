from typing import Optional, Union

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar
from ..constant import OrientationType, DirectionType


class Row(AntdComponent):
    tag = 'Row'
    align: Optional[Var[str]]
    gutter: Optional[Var[Union[int, ContainVar]]]
    justify: Optional[Var[str]]
    wrap: Optional[Var[str]]


class Col(AntdComponent):
    tag = 'Col'
    flex: Optional[Var[Union[str, int]]]
    offset: Optional[Var[int]]
    order: Optional[Var[int]]
    pull: Optional[Var[int]]
    push: Optional[Var[int]]
    span: Optional[Var[int]]

    xs: Optional[Var[Union[int, ContainVar]]]
    sm: Optional[Var[Union[int, ContainVar]]]
    md: Optional[Var[Union[int, ContainVar]]]
    lg: Optional[Var[Union[int, ContainVar]]]
    xl: Optional[Var[Union[int, ContainVar]]]
    xxl: Optional[Var[Union[int, ContainVar]]]


row = Row.create
col = Col.create
