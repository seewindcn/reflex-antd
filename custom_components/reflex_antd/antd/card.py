from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue


class Card(AntdComponent):
    tag = 'Card'

    actions: Optional[Var[ContainVar]]
    active_tab_key: Optional[Var[str]]
    bordered: Optional[Var[bool]]
    cover: Optional[Var[Component]]
    default_active_tab_key: Optional[Var[str]]
    extra: Optional[Var[Component]]
    hoverable: Optional[Var[bool]]
    loading: Optional[Var[bool]]
    size: Optional[Var[str]]
    tab_bar_extra_content: Optional[Var[Component]]
    tab_list: Optional[Var[list[ContainVar]]]
    title: Optional[Var[Component]]
    type: Optional[Var[str]]
    tab_props: Optional[Var[Union[ContainVar,dict]]]
    class_names: Optional[Var[dict]]
    styles: Optional[Var[dict]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_tab_change': lambda key: [key],
        })
        return _triggers


class CardGrid(AntdComponent):
    tag = 'Card.Grid'

    hoverable: Optional[Var[bool]]


class CardMeta(AntdComponent):
    tag = 'Card.Meta'

    avatar: Optional[Var[Component]]
    className: Optional[Var[str]]
    description: Optional[Var[Component]]
    style: Optional[Var[Dict]]
    title: Optional[Var[Component]]


card = Card.create
card_grid = CardGrid.create
card_meta = CardMeta.create
