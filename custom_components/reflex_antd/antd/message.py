from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Message(AntdComponent):
    tag = 'Message'

    content: Optional[Var[Union[ReactNode, dict]]]
    duration: Optional[Var[int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_close": lambda: [],
        })
        return _triggers


message = Message.create
