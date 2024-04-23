from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TypeType

class Popconfirm(AntdComponent):
    tag = 'Popconfirm'

    cancel_button_orops: Optional[Var[dict]]
    cancel_text: Optional[Var[str]]
    disabled: Optional[Var[bool]]
    icon: Optional[Var[ReactNode]]
    ok_button_props: Optional[Var[dict]]
    ok_text: Optional[Var[str]]
    ok_type: Optional[Var[TypeType]]
    open: Optional[Var[bool]]
    show_cancel: Optional[Var[bool]]
    title: Optional[Var[ReactNode]]
    description: Optional[Var[ReactNode]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_cancel": lambda e: [e],
            "on_confirm": lambda e: [e],
            "on_popup_click": lambda e: [e],
        })
        return _triggers


popconfirm = Popconfirm.create
