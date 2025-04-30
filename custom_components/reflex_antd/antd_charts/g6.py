from typing import Any, Optional
from abc import ABC

import reflex as rx

from ..base import Var, ContainVar, ReactNode, Base, ExTypes, PropBase, AntdBaseComponent, AntdNoSSRComponent

""" 
https://g6.antv.antgroup.com/api/data
 """


class DagreLayout(PropBase):
    type: str = 'dagre'
    node_size: list[int] = None
    nodesep: int
    ranksep: int


class G6Node(PropBase):
    style: ExTypes = None


class G6Edge(PropBase):
    style: ExTypes = None
    state: ExTypes = None


class G6BaseComponent(AntdBaseComponent):
    animation: Optional[Var[bool]]
    auto_fit: Optional[Var[str]]  # view | center
    auto_resize: Optional[Var[bool]]
    background: Optional[Var[str]]
    cursor: Optional[Var[str]]
    device_pixel_ratio: Optional[Var[int]]
    width: Optional[Var[int]]
    height: Optional[Var[int]]
    zoom: Optional[Var[int | float]]
    zoom_range: Optional[Var[tuple[int | float, int | float]]]
    padding: Optional[Var[int | list[int]]]
    renderer: Optional[Var[ExTypes]]
    rotation: Optional[Var[int | float]]

