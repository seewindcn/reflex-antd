from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import StatusType, SizeType, VariantType, PlacementType


class Mention(AntdComponent):
    tag = 'Mention'

    allow_clear: Optional[Var[Union[bool, ContainVar]]]
    auto_focus: Optional[Var[bool]]
    auto_size: Optional[Var[Union[bool, Dict]]]
    default_value: Optional[Var[str]]
    filter_option: Optional[Var[Union[bool, JsValue]]]
    get_popup_container: Optional[Var[JsValue]]
    not_found_content: Optional[Var[ReactNode]]
    placement: Optional[Var[PlacementType]]
    prefix: Optional[Var[Union[str, List[str]]]]
    split: Optional[Var[str]]
    status: Optional[Var[StatusType]]
    validate_search: Optional[Var[JsValue]]
    value: Optional[Var[str]]
    variant: Optional[Var[VariantType]]
    options: Optional[Var[ContainVar]]

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
