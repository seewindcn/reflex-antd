from typing import Optional, Union, Dict, Any

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Avatar(AntdComponent):
    tag = 'Avatar'

    alt: Var[str]
    gap: Var[int]
    icon: Var[ReactNode]
    shape: Var[str]
    size: Var[Union[str, int, Dict]]
    src: Var[ReactNode]
    src_set: Var[str]
    draggable: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_error": lambda: [],
        })
        return _triggers


class AvatarGroup(AntdComponent):
    tag = 'Avatar.Group'

    max_count: Var[int]
    max_popover_placement: Var[str]
    max_popover_trigger: Var[str]
    max_style: Var[Dict]
    size: Var[Union[str, int, Dict]]
    shape: Var[str]


avatar = Avatar.create
avatar_group = AvatarGroup.create
