from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Empty(AntdComponent):
    tag = 'Empty'

    description: Var[ReactNode]
    image: Var[ReactNode]
    image_style: Var[dict]


empty = Empty.create
