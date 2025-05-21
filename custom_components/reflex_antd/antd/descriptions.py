from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import VariantType, SizeType, DirectionType


class Descriptions(AntdComponent):
    tag = 'Descriptions'

    bordered: Var[bool]
    colon: Var[bool]
    column: Var[Union[int, dict]]
    content_style: Var[Union[dict, ContainVar]]
    extra: Var[ReactNode]
    items: Var[Union[JsValue, ContainVar, list]]
    label_style: Var[dict]
    layout: Var[DirectionType]
    size: Var[SizeType]
    title: Var[ReactNode]


class DescriptionItem(AntdComponent):
    """ for <5.8.0; >=5.8.0 use items """
    tag = 'Descriptions.Item'

    label: Var[str]
    span: Var[int]


descriptions = Descriptions.create
description_item = DescriptionItem.create
