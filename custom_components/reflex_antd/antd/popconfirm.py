from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TypeType

class Popconfirm(AntdComponent):
    tag = 'Popconfirm'

    cancel_button_orops: Var[dict]
    cancel_text: Var[str]
    disabled: Var[bool]
    icon: Var[ReactNode]
    ok_button_props: Var[dict]
    ok_text: Var[str]
    ok_type: Var[TypeType]
    open: Var[bool]
    show_cancel: Var[bool]
    title: Var[ReactNode]
    description: Var[ReactNode]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_cancel": lambda e: [e],
            "on_confirm": lambda e: [e],
            "on_popup_click": lambda e: [e],
        })
        return _triggers


popconfirm = Popconfirm.create
