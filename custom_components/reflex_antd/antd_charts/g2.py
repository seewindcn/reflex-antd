from typing import Any, Optional
from abc import ABC

from ..base import Var, ContainVar, ReactNode, Base, ExTypes
from . import constant as C

""" 
https://g2.antv.antgroup.com/api/overview 
 """


class AxisComponent(Base, ABC):
    title: Optional[ReactNode | ContainVar]
    tick_count: Optional[Var[int]]
    label_formatter: Optional[ContainVar]
    state: Optional[C.stateType]


class BaseMark(Base, ABC):
    x: Optional[Var[int]]
    y: Optional[Var[int]]
    encode: Optional[Var[ExTypes]]
    scale: Optional[Var[ExTypes]]
    coordinate: Optional[Var[ExTypes]]

    animate: Optional[Var[ExTypes]]
    labels: Optional[Var[ExTypes]]
    # tooltip: Optional[Var[ExTypes | ReactNode]]
    axis: Optional[Var[ExTypes | dict]]
    legend: Optional[Var[ExTypes]]
    slider: Optional[Var[ExTypes]]
    scrollbar: Optional[Var[ExTypes]]
    title: Optional[Var[ExTypes | ReactNode]]
    interaction: Optional[Var[ExTypes]]

