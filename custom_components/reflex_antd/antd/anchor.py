from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsNode
from ..constant import OrientationType, DirectionType


class Anchor(AntdComponent):
    tag = 'Anchor'

    affix: Optional[Var[bool]]
    bounds: Optional[Var[int]]
    get_container: Optional[Var[JsNode]]
    get_current_anchor: Optional[Var[JsNode]]
    offset_top: Optional[Var[int]]
    show_ink_in_fixed: Optional[Var[bool]]
    target_offset: Optional[Var[int]]
    items: Optional[Var[Union[List, ContainVar]]]
    direction: Optional[Var[DirectionType]]
    replace: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda link: [link],
            EventTriggers.ON_CLICK: lambda ev, link: [ev, link],
        })
        return _triggers


anchor = Anchor.create
