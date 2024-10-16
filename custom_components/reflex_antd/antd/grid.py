from typing import Optional, Union, Dict

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar
from ..constant import OrientationType, DirectionType


class Row(AntdComponent):
    tag = 'Row'

    align: Optional[Var[str]]
    gutter: Optional[Var[Union[int, ContainVar, list]]]
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

    xs: Optional[Var[Union[int, Dict]]]
    sm: Optional[Var[Union[int, Dict]]]
    md: Optional[Var[Union[int, Dict]]]
    lg: Optional[Var[Union[int, Dict]]]
    xl: Optional[Var[Union[int, Dict]]]
    xxl: Optional[Var[Union[int, Dict]]]


row = Row.create
col = Col.create
