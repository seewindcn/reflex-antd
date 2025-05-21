from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue,ReactNode
from ..constant import ColorFormatType, SizeType, PlacementType, TriggerType


class ColorPicker(AntdComponent):
    tag = 'ColorPicker'

    allow_clear: Var[bool]
    arrow: Var[bool]
    default_value: Var[str]
    default_format: Var[str]
    disabled: Var[bool]
    disabled_alpha: Var[bool]
    destroy_tooltip_on_hide: Var[bool]
    format: Var[ColorFormatType]
    open: Var[bool]
    presets: Var[ContainVar]
    placement: Var[PlacementType]
    panel_render: Var[JsValue]
    show_text: Var[Union[bool, JsValue]]
    size: Var[SizeType]
    trigger: Var[TriggerType]
    value: Var[str]

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



