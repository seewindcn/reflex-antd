from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import VariantType, SizeType, DirectionType


class Descriptions(AntdComponent):
    tag = 'Descriptions'

    bordered: Optional[Var[bool]]
    colon: Optional[Var[bool]]
    column: Optional[Var[Union[int, dict]]]
    content_style: Optional[Var[Union[dict, ContainVar]]]
    extra: Optional[Var[ReactNode]]
    items: Optional[Var[Union[JsValue, ContainVar, list]]]
    label_style: Optional[Var[dict]]
    layout: Optional[Var[DirectionType]]
    size: Optional[Var[SizeType]]
    title: Optional[Var[ReactNode]]


descriptions = Descriptions.create
