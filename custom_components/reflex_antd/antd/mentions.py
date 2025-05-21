from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType, PlacementType


class Mention(AntdComponent):
    tag = 'Mention'

    allow_clear: Var[Union[bool, ContainVar]]
    auto_focus: Var[bool]
    auto_size: Var[Union[bool, Dict]]
    default_value: Var[str]
    filter_option: Var[Union[bool, JsValue]]
    get_popup_container: Var[JsValue]
    not_found_content: Var[ReactNode]
    placement: Var[PlacementType]
    prefix: Var[Union[str, List[str]]]
    split: Var[str]
    status: Var[StatusType]
    validate_search: Var[JsValue]
    value: Var[str]
    variant: Var[VariantType]
    options: Var[ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda text: [text],
            "on_resize": lambda ev: [ev],
            'on_search': lambda text, prefix: [text, prefix],
            "on_select": lambda option, prefix: [option, prefix],
        })
        return _triggers


mention = Mention.create
