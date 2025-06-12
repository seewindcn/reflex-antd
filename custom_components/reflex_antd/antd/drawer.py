from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExTypes
from ..constant import OrientationType, SizeType


class Drawer(AntdComponent):
    tag = 'Drawer'

    auto_focus: Var[bool]
    class_names: Var[ContainVar]
    close_icon: Var[Union[ReactNode, bool]]
    destroy_on_close: Var[bool]
    extra: Var[ReactNode]
    footer: Var[ReactNode]
    force_render: Var[bool]
    get_container: Var[Union[ContainVar, bool]]
    height: Var[Union[str, int]]
    keyboard: Var[bool]
    mask: Var[bool]
    mask_closable: Var[bool]
    placement: Var[OrientationType]
    push: Var[Union[bool, dict]]
    root_style: Var[dict]
    size: Var[SizeType]
    styles: Var[ContainVar]
    title: Var[ReactNode]
    loading: Var[bool]
    open: Var[bool]
    width: Var[Union[str, int]]
    z_index: Var[int]
    drawer_render: Var[ExTypes]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "after_open_change": lambda open: [open],
            "on_close": lambda: [],
        })
        return _triggers


drawer = Drawer.create
