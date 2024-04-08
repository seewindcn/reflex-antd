from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import SizeType, QRCodeType, QRCodeErrorLevelType, QRCodeStatusType


class QRCode(AntdComponent):
    tag = 'QRCode'

    value: Optional[Var[str]]
    type: Optional[Var[QRCodeType]]
    icon: Optional[Var[str]]
    size: Optional[Var[int]]
    icon_size: Optional[Var[int]]
    color: Optional[Var[str]]
    bg_color: Optional[Var[str]]
    bordered: Optional[Var[bool]]
    error_level: Optional[Var[QRCodeErrorLevelType]]
    status: Optional[Var[QRCodeStatusType]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_refresh": lambda: [],
        })
        return _triggers


qrcode = QRCode.create

