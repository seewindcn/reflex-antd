from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Card(AntdComponent):
    tag = 'Card'

    actions: Var[ContainVar]
    active_tab_key: Var[str]
    bordered: Var[bool]
    cover: Var[ReactNode]
    default_active_tab_key: Var[str]
    extra: Var[ReactNode]
    hoverable: Var[bool]
    loading: Var[bool]
    size: Var[str]
    tab_bar_extra_content: Var[ReactNode]
    tab_list: Var[list[ContainVar]]
    title: Var[ReactNode]
    type: Var[str]
    tab_props: Var[Union[ContainVar, dict]]
    class_names: Var[dict]
    styles: Var[dict]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_tab_change': lambda key: [key],
        })
        return _triggers


class CardGrid(AntdComponent):
    tag = 'Card.Grid'

    hoverable: Var[bool]


class CardMeta(AntdComponent):
    tag = 'Card.Meta'

    avatar: Var[ReactNode]
    description: Var[ReactNode]
    title: Var[ReactNode]


card = Card.create
card_grid = CardGrid.create
card_meta = CardMeta.create
