from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import TimelineModeType


class Timeline(AntdComponent):
    tag = 'Timeline'

    mode: Optional[Var[TimelineModeType]]
    pending: Optional[Var[Component]]
    pending_dot: Optional[Var[Component]]
    reverse: Optional[Var[bool]]
    items: Optional[Var[Union[List, ContainVar]]]


timeline = Timeline.create

