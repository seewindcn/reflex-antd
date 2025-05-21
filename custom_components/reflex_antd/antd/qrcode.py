from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType, QRCodeType, QRCodeErrorLevelType, QRCodeStatusType


class QRCode(AntdComponent):
    tag = 'QRCode'

    value: Var[str]
    type: Var[QRCodeType]
    icon: Var[str]
    size: Var[int]
    icon_size: Var[int]
    color: Var[str]
    bg_color: Var[str]
    bordered: Var[bool]
    error_level: Var[QRCodeErrorLevelType]
    status: Var[QRCodeStatusType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_refresh": lambda: [],
        })
        return _triggers


qrcode = QRCode.create

