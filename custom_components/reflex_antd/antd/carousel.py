from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue


class Carousel(AntdComponent):
    tag = 'Carousel'

    autoplay: Var[bool]
    autoplay_speed: Var[int]
    dot_position: Var[str]
    dots: Var[Union[bool, dict]]
    fade: Var[bool]
    infinite: Var[bool]
    speed: Var[int]
    easing: Var[str]
    wait_for_animate: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'after_change': lambda current: [],
            'before_change': lambda current, next: [],
        })
        return _triggers


carousel = Carousel.create
