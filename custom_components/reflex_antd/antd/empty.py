from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Empty(AntdComponent):
    tag = 'Empty'

    description: Optional[Var[ReactNode]]
    image: Optional[Var[ReactNode]]
    image_style: Optional[Var[dict]]


empty = Empty.create
