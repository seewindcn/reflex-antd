from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType


class Spin(AntdComponent):
    tag = 'Spin'

    delay: Var[int]
    indicator: Var[ReactNode]
    size: Var[SizeType]
    spinning: Var[bool]
    tip: Var[ReactNode]
    wrapper_class_name: Var[str]
    fullscreen: Var[bool]


spin = Spin.create

