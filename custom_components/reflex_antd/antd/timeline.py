from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TimelineModeType


class Timeline(AntdComponent):
    tag = 'Timeline'

    mode: Var[TimelineModeType]
    pending: Var[ReactNode]
    pending_dot: Var[ReactNode]
    reverse: Var[bool]
    items: Var[Union[List, ContainVar]]


timeline = Timeline.create

