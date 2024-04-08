from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType, PlacementType, TabsType


class Segmented(AntdComponent):
    tag = 'Segmented'

    block: Optional[Var[bool]]
    default_value: Optional[Var[Union[str, int]]]
    disabled: Optional[Var[bool]]
    options: Optional[Union[List[str], List[int], List[Dict]]]
    size: Optional[Var[SizeType]]
    value: Optional[Var[Union[str, int]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value: [value],
        })
        return _triggers


segmented = Segmented.create

