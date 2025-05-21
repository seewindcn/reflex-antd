from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType


class Skeleton(AntdComponent):
    tag = 'Skeleton'

    active: Var[bool]
    avatar: Var[Union[bool, Dict]]
    loading: Var[bool]
    paragraph: Var[Union[bool, Dict]]
    round: Var[bool]
    title: Var[Union[bool, Dict]]


skeleton = Skeleton.create

