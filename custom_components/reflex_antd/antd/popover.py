from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType

from .tooltip import Tooltip


class Popover(Tooltip):
    tag = 'Popover'

    content: Var[Union[ReactNode, ContainVar]]
    title: Var[Union[ReactNode, ContainVar]]


popover = Popover.create
