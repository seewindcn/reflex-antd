from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import StatusType


class Transfer(AntdComponent):
    tag = 'Transfer'

    data_source: Optional[Var[List]]
    disabled: Optional[Var[bool]]
    selections_icon: Optional[Var[Component]]
    filter_option: Optional[Var[JsValue]]
    footer: Optional[Var[JsValue]]
    list_style: Optional[Var[Union[Dict, JsValue]]]
    locale: Optional[Var[Union[Dict, ContainVar]]]
    one_way: Optional[Var[bool]]
    operations: Optional[Var[List[str]]]
    operation_style: Optional[Var[Dict]]
    pagination: Optional[Var[Union[bool, ContainVar]]]
    render: Optional[Var[Union[JsValue, ContainVar]]]
    row_key: Optional[Var[JsValue]]
    select_all_labels: Optional[Var[JsValue]]
    selected_keys: Optional[Var[List[str]]]
    show_search: Optional[Var[bool]]
    showSelect_all: Optional[Var[bool]]
    status: Optional[Var[StatusType]]
    target_keys: Optional[Var[List[str]]]
    titles: Optional[Var[ContainVar]]

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




