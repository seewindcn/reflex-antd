"""
https://ant-design-charts.antgroup.com/en/options/plots/overview
"""
from typing import Any, Optional, Union, Self, List
from types import SimpleNamespace
from abc import ABC
import dataclasses

from . import g2, base
from ..base import Var, BaseModel, Base, ExTypes, ContainVar, ReactNode, PropBase


# class Spec(g2.AxisComponent, g2.BaseMark, ABC):
#     depth: Optional[Var[int]]


# class BaseOptions(Base, ABC):
#
#
# class Options(Spec, BaseOptions):
#     type: Optional[Var[str]]
#     annotations: Optional[Var[ExTypes]]
#     line: Optional[Var[ExTypes]]
#     children: Optional[Var[ExTypes]]


# class AttachConfig(Base, ABC):
#     tooltip: Optional[Var[ExTypes | bool]]
#     on_ready: Optional[Var[ExTypes]]
#     on_event: Optional[Var[ExTypes]]


# class Common(AttachConfig, ContainerConfig, ABC):
#     data: Optional[Var[ExTypes]]


class ContainerConfig(Base, ABC):
    width: Optional[Var[int]]
    height: Optional[Var[int]]
    auto_fit: Optional[Var[bool]]
    renderer: Optional[Var[ExTypes]]


class DataConfig(Base, ABC):
    data: Optional[Var[ExTypes | list[dict]]]
    x_field: Optional[Var[ExTypes | str]]
    y_field: Optional[Var[ExTypes | str]]
    series_field: Optional[Var[ExTypes | str]]


class ShapeConfig(Base, ABC):
    shape_field: Optional[Var[ExTypes | str]]
    color_field: Optional[Var[ExTypes | str]]
    size_field: Optional[Var[ExTypes | str]]
    key_field: Optional[Var[ExTypes | str]]
    stack: Optional[Var[ExTypes | bool]]
    normalize: Optional[Var[ExTypes | bool]]
    sort: Optional[Var[ExTypes | bool]]
    group: Optional[Var[ExTypes | bool]]
    percent: Optional[Var[bool]]
    line: Optional[Var[ExTypes]]
    area: Optional[Var[ExTypes]]
    point: Optional[Var[ExTypes]]
    # label: Optional[Var[ExTypes | bool]]


class LabelProp(PropBase):
    text: str | ExTypes = ''
    font_size: int | ExTypes = None
    font_family: str | ExTypes = None
    font_weight: str | ExTypes = None
    line_height: int | ExTypes = None
    text_align: str | ExTypes = None
    text_baseline: str | ExTypes = None
    fill: str | ExTypes = None
    fill_opacity: int | ExTypes = None
    stroke: str | ExTypes = None
    stroke_opacity: str | ExTypes = None
    line_width: int | ExTypes = None
    line_dash: list[int] | ExTypes = None
    opacity: int | ExTypes = None
    shadow_color: str | ExTypes = None
    shadow_blur: int | ExTypes = None
    shadow_offset_x: int | ExTypes = None
    shadow_offset_y: int | ExTypes = None
    cursor: str | ExTypes = None
    position: str | ExTypes = None
    selector: str | ExTypes = None
    connector: bool = None
    background: bool = None
    transform: list | ExTypes = None
    formatter: ExTypes = None


class PoltProp(SimpleNamespace):
    label = LabelProp


class PoltBase(base.ChartBase, ContainerConfig, DataConfig, ShapeConfig, g2.BaseMark):
    title: Optional[ReactNode | ContainVar]
    state: Optional[Var[str | ExTypes]]
    label: Optional[LabelProp]
    tooltip: Optional[Var[ExTypes]]


class Line(PoltBase):
    tag = 'Line'


class Area(PoltBase):
    tag = 'Area'


class Bar(PoltBase):
    tag = 'Bar'


class Column(PoltBase):
    tag = 'Column'


class Heatmap(PoltBase):
    tag = 'Heatmap'


class Pie(PoltBase):
    tag = 'Pie'
    angle_field: Optional[Var[ExTypes | str]]
    color_field: Optional[Var[ExTypes | str]]


class Scatter(PoltBase):
    tag = 'Scatter'


class Stock(PoltBase):
    tag = 'Stock'


class DualAxes(PoltBase):
    tag = 'DualAxes'


class Histogram(PoltBase):
    tag = 'Histogram'


class Box(PoltBase):
    tag = 'Box'


class Gauge(PoltBase):
    tag = 'Gauge'


polt_prop = PoltProp()
line = Line.create
area = Area.create
bar = Bar.create
column = Column.create
heatmap = Heatmap.create
pie = Pie.create
scatter = Scatter.create
stock = Stock.create
dualAxes = DualAxes.create
histogram = Histogram.create
box = Box.create

gauge = Gauge.create
