from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, ProgressType, SizeType, OrientationType


class Progress(AntdComponent):
    tag = 'Progress'

    format: Optional[Var[JsValue]]
    percent: Optional[Var[int]]
    show_info: Optional[Var[bool]]
    status: Optional[Var[StatusType]]
    stroke_color: Optional[Var[str]]
    stroke_linecap: Optional[Var[str]]
    success: Optional[Var[Dict]]
    trail_color: Optional[Var[str]]
    type: Optional[Var[ProgressType]]
    size: Optional[Var[Union[int, SizeType, List[Union[int, SizeType]]]]]
    # type=...
    steps: Optional[Var[Union[int, Dict]]]
    stroke_color: Optional[Var[Union[str, List[str], Dict]]]
    stroke_width: Optional[Var[int]]
    # dashboard
    gap_degree: Optional[Var[int]]
    gap_position: Optional[Var[OrientationType]]


progress = Progress.create


