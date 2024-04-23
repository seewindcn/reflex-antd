from typing import Optional, Union, Dict, Any

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Avatar(AntdComponent):
    tag = 'Avatar'

    alt: Optional[Var[str]]
    gap: Optional[Var[int]]
    icon: Optional[Var[ReactNode]]
    shape: Optional[Var[str]]
    size: Optional[Var[Union[str, int, Dict]]]
    src: Optional[Var[ReactNode]]
    src_set: Optional[Var[str]]
    draggable: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_error": lambda: [],
        })
        return _triggers


class AvatarGroup(AntdComponent):
    tag = 'Avatar.Group'

    max_count: Optional[Var[int]]
    max_popover_placement: Optional[Var[str]]
    max_popover_trigger: Optional[Var[str]]
    max_style: Optional[Var[Dict]]
    size: Optional[Var[Union[str, int, Dict]]]
    shape: Optional[Var[str]]


avatar = Avatar.create
avatar_group = AvatarGroup.create
