from typing import Optional, Union, Dict, Any

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExTypes
from ..constant import SizeType


class AList(AntdComponent):
    tag = 'List'

    bordered: Var[bool]
    data_source: Var[Any]
    footer: Var[ReactNode]
    grid: Var[dict]
    header: Var[ReactNode]
    item_layout: Var[str]
    loading: Var[Union[bool, dict]]
    load_more: Var[ReactNode]
    locale: Var[dict]
    pagination: Var[Union[bool, dict, ContainVar]]
    render_item: Var[JsValue]
    size: Var[SizeType]
    split: Var[bool]


class ListItem(AntdComponent):
    tag = 'List.Item'

    actions: Var[ExTypes]
    extra: Var[ExTypes]


class ListItemMeta(AntdComponent):
    tag = 'List.Item.Meta'

    avatar: Var[ReactNode]
    description: Var[ReactNode]
    title: Var[ReactNode]


alist = AList.create
list_item = ListItem.create
list_item_meta = ListItemMeta.create
