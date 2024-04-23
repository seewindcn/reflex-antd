from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType


class Spin(AntdComponent):
    tag = 'Spin'

    delay: Optional[Var[int]]
    indicator: Optional[Var[ReactNode]]
    size: Optional[Var[SizeType]]
    spinning: Optional[Var[bool]]
    tip: Optional[Var[ReactNode]]
    wrapper_class_name: Optional[Var[str]]
    fullscreen: Optional[Var[bool]]


spin = Spin.create

