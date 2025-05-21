from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import OrientationType, DirectionType


class Watermark(AntdComponent):
    tag = 'Watermark'

    width: Var[int]
    height: Var[int]
    inherit: Var[bool]
    rotate: Var[int]
    z_index: Var[int]
    image: Var[str]
    content: Var[Union[str, List[str]]]
    font: Var[Union[Dict, ContainVar]]
    gap: Var[Tuple[int, int]]
    offset: Var[Tuple[int, int]]


watermark = Watermark.create


