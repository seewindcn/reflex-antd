from typing import Optional, Union, Dict, Any

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import SizeType


class AList(AntdComponent):
    tag = 'List'

    bordered: Optional[Var[bool]]
    data_source: Optional[Var[Any]]
    footer: Optional[Var[ReactNode]]
    grid: Optional[Var[dict]]
    header: Optional[Var[ReactNode]]
    item_layout: Optional[Var[str]]
    loading: Optional[Var[Union[bool, dict]]]
    load_more: Optional[Var[ReactNode]]
    locale: Optional[Var[dict]]
    pagination: Optional[Var[Union[bool, dict]]]
    render_item: Optional[Var[JsValue]]
    size: Optional[Var[SizeType]]
    split: Optional[Var[bool]]


class ListItem(AntdComponent):
    tag = 'List.Item'

    actions: Optional[Var[list[ContainVar]]]
    extra: Optional[Var[ReactNode]]


class ListItemMeta(AntdComponent):
    tag = 'List.Item.Meta'

    avatar: Optional[Var[ReactNode]]
    description: Optional[Var[ReactNode]]
    title: Optional[Var[ReactNode]]


alist = AList.create
list_item = ListItem.create
list_item_meta = ListItemMeta.create
