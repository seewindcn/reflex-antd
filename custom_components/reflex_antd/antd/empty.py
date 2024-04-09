from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue


class Empty(AntdComponent):
    tag = 'Empty'

    description: Optional[Var[Component]]
    image: Optional[Var[Component]]
    image_style: Optional[Var[dict]]


empty = Empty.create
