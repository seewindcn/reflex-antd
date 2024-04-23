from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import TypeType


class Modal(AntdComponent):
    tag = 'Modal'

    class_names: Optional[Var[ContainVar]]
    styles: Optional[Var[ContainVar]]
    cancel_button_props: Optional[Var[ContainVar]]
    cancel_text: Optional[Var[ReactNode]]
    centered: Optional[Var[bool]]
    close_icon: Optional[Var[Union[ReactNode, bool]]]
    confirm_loading: Optional[Var[bool]]
    destroy_on_close: Optional[Var[bool]]
    focus_trigger_after_close: Optional[Var[bool]]
    footer: Optional[Var[ContainVar]]
    force_render: Optional[Var[bool]]
    get_container: Optional[Var[Union[bool, ContainVar]]]
    keyboard: Optional[Var[bool]]
    mask: Optional[Var[bool]]
    mask_closable: Optional[Var[bool]]
    modal_render: Optional[Var[ReactNode]]
    ok_button_props: Optional[Var[ContainVar]]
    ok_text: Optional[Var[ReactNode]]
    ok_type: Optional[Var[TypeType]]
    title: Optional[Var[ReactNode]]
    open: Optional[Var[bool]]
    width: Optional[Var[Union[str, int]]]
    wrapClassName: Optional[Var[str]]
    zIndex: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "after_close": lambda: [],
            "on_cancel": lambda event: [],
            "on_ok": lambda event: [],
            "after_open_change": lambda open: [],
        })
        return _triggers


modal = Modal.create
