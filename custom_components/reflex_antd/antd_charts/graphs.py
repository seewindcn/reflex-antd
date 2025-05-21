"""
https://ant-design-charts.antgroup.com/options/graphs/overview
"""
from typing import Any, Optional, Union, Self, List
from types import SimpleNamespace
from abc import ABC
import dataclasses

from . import g2, base
from ..base import Var, BaseModel, Base, ExTypes, ContainVar, ReactNode, PropBase
from . import g6


class FlowGraph(base.GraphBase):
    tag = 'FlowGraph'

    data: Optional[Var[ExTypes | dict]]
    label_field: Optional[Var[str | ExTypes]]
    # Dagre layout: https://github.com/dagrejs/dagre/wiki
    layout: Optional[g6.DagreLayout]


flow_graph = FlowGraph.create
