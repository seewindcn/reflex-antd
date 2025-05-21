from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsNode
from ..constant import OrientationType, DirectionType


class Anchor(AntdComponent):
    tag = 'Anchor'

    affix: Var[bool]
    bounds: Var[int]
    get_container: Var[JsNode]
    get_current_anchor: Var[JsNode]
    offset_top: Var[int]
    show_ink_in_fixed: Var[bool]
    target_offset: Var[int]
    items: Var[Union[List, ContainVar]]
    direction: Var[DirectionType]
    replace: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda link: [link],
            EventTriggers.ON_CLICK: lambda ev, link: [ev, link],
        })
        return _triggers


anchor = Anchor.create
