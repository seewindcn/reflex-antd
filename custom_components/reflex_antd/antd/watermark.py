from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import OrientationType, DirectionType


class Watermark(AntdComponent):
    tag = 'Watermark'

    width: Optional[Var[int]]
    height: Optional[Var[int]]
    inherit: Optional[Var[bool]]
    rotate: Optional[Var[int]]
    z_index: Optional[Var[int]]
    image: Optional[Var[str]]
    content: Optional[Var[Union[str, List[str]]]]
    font: Optional[Var[Union[Dict, ContainVar]]]
    gap: Optional[Var[Tuple[int, int]]]
    offset: Optional[Var[Tuple[int, int]]]


watermark = Watermark.create


