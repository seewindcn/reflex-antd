from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, ReactNode
from ..constant import AlignType, DirectionType, SizeType


class Splitter(AntdComponent):
    tag = 'Splitter'

    layout: Var[str]
    lazy: Var[bool]

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

    default_size: Var[Union[int, str]]
    min: Var[Union[int, str]]
    max: Var[Union[int, str]]
    size: Var[Union[int, str]]
    collapsible: Var[Union[bool, dict]]
    resizable: Var[bool]


splitter = Splitter.create
splitter_panel = SplitterPanel.create
