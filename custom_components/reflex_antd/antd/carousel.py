from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue


class Carousel(AntdComponent):
    tag = 'Carousel'

    autoplay: Optional[Var[bool]]
    autoplay_speed: Optional[Var[int]]
    dot_position: Optional[Var[str]]
    dots: Optional[Var[Union[bool, dict]]]
    fade: Optional[Var[bool]]
    infinite: Optional[Var[bool]]
    speed: Optional[Var[int]]
    easing: Optional[Var[str]]
    wait_for_animate: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'after_change': lambda current: [],
            'before_change': lambda current, next: [],
        })
        return _triggers


carousel = Carousel.create
