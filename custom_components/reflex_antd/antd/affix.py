from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import OrientationType, DirectionType


class Affix(AntdComponent):
    tag = 'Affix'

    offset_bottom: Var[int]
    offset_top: Var[int]
    target: Var[JsValue]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            EventTriggers.ON_CHANGE: lambda affixed: [affixed],
        })
        return _triggers


affix = Affix.create



