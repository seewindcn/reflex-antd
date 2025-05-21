from typing import Optional, Union, Dict, Any

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from .base import Locale
from .date_picker import DayJS


class Calendar(AntdComponent):
    tag = 'Calendar'

    cell_render: Var[JsValue]
    full_cell_render: Var[JsValue]
    default_value: Var[JsValue]
    disabled_date: Var[JsValue]
    fullscreen: Var[bool]
    header_render: Var[JsValue]
    locale: Var[Locale]
    mode: Var[str]
    value: Var[JsValue]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_select': lambda value, mode: [value, mode],
            'on_panel_change': lambda value, mode: [value, mode],
        })
        return _triggers

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("dayjs", []).append(
            imports.ImportVar(tag="dayjs", is_default=True, install=False),
        )
        return _imports


dayjs = DayJS
calendar = Calendar.create
