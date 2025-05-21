from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, ProgressType, SizeType, OrientationType


class Progress(AntdComponent):
    tag = 'Progress'

    format: Var[JsValue]
    percent: Var[int]
    show_info: Var[bool]
    status: Var[StatusType]
    stroke_color: Var[str]
    stroke_linecap: Var[str]
    success: Var[Dict]
    trail_color: Var[str]
    type: Var[ProgressType]
    size: Var[Union[int, SizeType, List[Union[int, SizeType]]]]
    # type=...
    steps: Var[Union[int, Dict]]
    stroke_color: Var[Union[str, List[str], Dict]]
    stroke_width: Var[int]
    # dashboard
    gap_degree: Var[int]
    gap_position: Var[OrientationType]


progress = Progress.create


