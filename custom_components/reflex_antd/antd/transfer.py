from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, js_value, ReactNode
from ..constant import StatusType


class Transfer(AntdComponent):
    tag = 'Transfer'
    _rename_props: Dict[str, str] = {"itemRender": "render"}

    data_source: Var[List]
    disabled: Var[bool]
    selections_icon: Var[ReactNode]
    filter_option: Var[JsValue]
    footer: Var[JsValue]
    list_style: Var[Union[Dict, JsValue]]
    locale: Var[Union[Dict, ContainVar]]
    one_way: Var[bool]
    operations: Var[List[str]]
    operation_style: Var[Dict]
    pagination: Var[Union[bool, ContainVar]]
    item_render: Var[Union[JsValue, ContainVar]]
    row_key: Var[JsValue]
    select_all_labels: Var[JsValue]
    selected_keys: Var[List[str]]
    show_search: Var[bool]
    showSelect_all: Var[bool]
    status: Var[StatusType]
    target_keys: Var[List[str]]
    titles: Var[ContainVar]

    @classmethod
    def create(cls, *children, **props) -> Component:
        if 'item_render' not in props:
            props['item_render'] = js_value(lambda record: 'return record.title;')
        com = super().create(*children, **props)
        return com

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda target_keys, direction, move_keys: [target_keys, direction, move_keys],
            EventTriggers.ON_SCROLL: lambda direction, ev: [direction, ev],
            "on_search": lambda direction, value: [direction, value],
            "on_select_change": lambda s_keys, t_keys: [s_keys, t_keys],
        })
        return _triggers


transfer = Transfer.create




