from typing import Optional, Union, Dict

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar
from ..constant import OrientationType, DirectionType


class Row(AntdComponent):
    tag = 'Row'

    align: Var[str]
    gutter: Var[Union[int, ContainVar, dict, list]]
    justify: Var[str]
    wrap: Var[str]


class Col(AntdComponent):
    tag = 'Col'

    flex: Var[Union[str, int]]
    offset: Var[int]
    order: Var[int]
    pull: Var[int]
    push: Var[int]
    span: Var[int]

    xs: Var[Union[int, Dict]]
    sm: Var[Union[int, Dict]]
    md: Var[Union[int, Dict]]
    lg: Var[Union[int, Dict]]
    xl: Var[Union[int, Dict]]
    xxl: Var[Union[int, Dict]]


row = Row.create
col = Col.create
