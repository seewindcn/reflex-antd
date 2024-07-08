from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import OrientationType, SizeType


class Drawer(AntdComponent):
    tag = 'Drawer'

    auto_focus: Optional[Var[bool]]
    class_name: Optional[Var[str]]
    class_names: Optional[Var[ContainVar]]
    close_icon: Optional[Var[Union[ReactNode, bool]]]
    destroy_on_close: Optional[Var[bool]]
    extra: Optional[Var[ReactNode]]
    footer: Optional[Var[ReactNode]]
    force_render: Optional[Var[bool]]
    get_container: Optional[Var[Union[ContainVar, bool]]]
    height: Optional[Var[Union[str, int]]]
    keyboard: Optional[Var[bool]]
    mask: Optional[Var[bool]]
    mask_closable: Optional[Var[bool]]
    placement: Optional[Var[OrientationType]]
    push: Optional[Var[Union[bool, dict]]]
    root_style: Optional[Var[dict]]
    size: Optional[Var[SizeType]]
    styles: Optional[Var[ContainVar]]
    title: Optional[Var[ReactNode]]
    open: Optional[Var[bool]]
    width: Optional[Var[Union[str, int]]]
    z_index: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "after_open_change": lambda open: [open],
            "on_close": lambda: [],
        })
        return _triggers


drawer = Drawer.create
