from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType, SizeType


# TODO

class TreeSelect(AntdComponent):
    tag = 'TreeSelect'


tree_select = TreeSelect.create

