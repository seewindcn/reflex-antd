from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType


class Result(AntdComponent):
    tag = 'Result'

    extra: Optional[Var[ReactNode]]
    icon: Optional[Var[ReactNode]]
    status: Optional[Var[Union[StatusType, str]]]
    sub_title: Optional[Var[ReactNode]]
    title: Optional[Var[ReactNode]]


result = Result.create


