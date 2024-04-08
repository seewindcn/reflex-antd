from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType


class Result(AntdComponent):
    tag = 'Result'

    extra: Optional[Var[Component]]
    icon: Optional[Var[Component]]
    status: Optional[Var[Union[StatusType, str]]]
    sub_title: Optional[Var[Component]]
    title: Optional[Var[Component]]


result = Result.create


