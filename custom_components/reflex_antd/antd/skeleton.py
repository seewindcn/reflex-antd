from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType


class Skeleton(AntdComponent):
    tag = 'Skeleton'

    active: Optional[Var[bool]]
    avatar: Optional[Var[Union[bool, Dict]]]
    loading: Optional[Var[bool]]
    paragraph: Optional[Var[Union[bool, Dict]]]
    round: Optional[Var[bool]]
    title: Optional[Var[Union[bool, Dict]]]


skeleton = Skeleton.create

