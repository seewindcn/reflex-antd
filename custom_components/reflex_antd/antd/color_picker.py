from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue,ReactNode
from ..constant import ColorFormatType, SizeType, PlacementType, TriggerType


class ColorPicker(AntdComponent):
    tag = 'ColorPicker'

    allow_clear: Optional[Var[bool]]
    arrow: Optional[Var[bool]]
    default_value: Optional[Var[str]]
    default_format: Optional[Var[str]]
    disabled: Optional[Var[bool]]
    disabled_alpha: Optional[Var[bool]]
    destroy_tooltip_on_hide: Optional[Var[bool]]
    format: Optional[Var[ColorFormatType]]
    open: Optional[Var[bool]]
    presets: Optional[Var[ContainVar]]
    placement: Optional[Var[PlacementType]]
    panel_render: Optional[Var[JsValue]]
    show_text: Optional[Var[Union[bool, JsValue]]]
    size: Optional[Var[SizeType]]
    trigger: Optional[Var[TriggerType]]
    value: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda value, hex: [value, hex],
            'on_change_complete': lambda value: [value],
            'on_format_change': lambda format: [format],
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
            'on_clear': lambda: [],
        })
        return _triggers


color_picker = ColorPicker.create



