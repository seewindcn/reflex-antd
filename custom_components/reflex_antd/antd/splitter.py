from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import AlignType, DirectionType, SizeType


class Splitter(AntdComponent):
    tag = 'Splitter'

    layout: Optional[Var[str]]
    lazy: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_resize_start": lambda v: [v],
            "on_resize": lambda v: [v],
            "on_resize_end": lambda v: [v],
        })
        return _triggers


class SplitterPanel(AntdComponent):
    tag = 'Splitter.Panel'

    default_size: Optional[Var[Union[int, str]]]
    min: Optional[Var[Union[int, str]]]
    max: Optional[Var[Union[int, str]]]
    size: Optional[Var[Union[int, str]]]
    collapsible: Optional[Var[Union[bool, dict]]]
    resizable: Optional[Var[bool]]


splitter = Splitter.create
splitter_panel = SplitterPanel.create
