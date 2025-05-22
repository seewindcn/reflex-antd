from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import DatePickerModeType, DatePickerType, SizeType, PlacementType, StatusType, VariantType

from .base import Locale, DayJS


class BaseDatePicker(AntdComponent):
    allow_clear: Var[bool]
    auto_focus: Var[bool]
    date_render: Var[JsValue]
    cell_render: Var[JsValue]
    components: Var[Union[ReactNode, list, dict, ContainVar]]
    disabled: Var[bool]
    disabled_date: Var[JsValue]
    format: Var[ContainVar]
    order: Var[bool]
    popup_class_name: Var[str]
    preserve_invalidOn_blur: Var[bool]
    get_popup_container: Var[JsValue]
    input_readOnly: Var[bool]
    locale: Var[Locale]
    min_date: Var[JsValue]
    max_date: Var[JsValue]
    mode: Var[DatePickerModeType]
    need_confirm: Var[bool]
    next_icon: Var[ReactNode]
    open: Var[bool]
    panel_render: Var[JsValue]
    picker: Var[DatePickerType]
    placeholder: Var[Union[str, List[str]]]
    placement: Var[PlacementType]
    popup_style: Var[ContainVar]
    presets: Var[ContainVar]
    prev_icon: Var[ReactNode]
    size: Var[SizeType]
    status: Var[StatusType]
    suffix_icon: Var[ReactNode]
    super_next_icon: Var[ReactNode]
    super_prev_icon: Var[ReactNode]
    variant: Var[VariantType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
            'on_panel_change': lambda value, mode: [value, mode],
        })
        return _triggers

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("dayjs", []).append(
            imports.ImportVar(tag="dayjs", is_default=True, install=False),
        )
        return _imports


class DatePicker(BaseDatePicker):
    tag = 'DatePicker'

    default_picker_value: Var[JsValue]
    default_value: Var[ContainVar]
    disabled_time: Var[JsValue]
    format: Var[ContainVar]
    multiple: Var[bool]
    picker_value: Var[ContainVar]
    render_extra_footer: Var[JsValue]
    show_now: Var[bool]
    show_time: Var[Union[bool, ContainVar]]
    # showTime.defaultValue
    show_week: Var[bool]
    value: Var[ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda date, sdate: [date, sdate],
            "on_ok": lambda: [],
            "on_panel_change": lambda value, mode: [value, mode],
        })
        return _triggers


class RangePicker(BaseDatePicker):
    tag = 'RangePicker'

    allow_empty: Var[Tuple[bool, bool]]
    cell_render: Var[JsValue]
    date_render: Var[JsValue]
    default_picker_value: Var[ContainVar]
    default_value: Var[ContainVar]
    disabled: Var[Tuple[bool, bool]]
    disabled_time: Var[JsValue]
    format: Var[ContainVar]
    picker_value: Var[ContainVar]
    presets: Var[ContainVar]
    render_extra_footer: Var[JsValue]
    separator: Var[ReactNode]
    show_time: Var[Union[bool, ContainVar]]
    # showTime.defaultValue
    value: Var[ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_calendar_change": lambda dates, sdates, info: [dates, sdates, info],
            EventTriggers.ON_CHANGE: lambda dates, sdates: [dates, sdates],
            EventTriggers.ON_FOCUS: lambda ev, range: [ev, range],
            EventTriggers.ON_BLUR: lambda ev, range: [ev, range],
        })
        return _triggers

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _vars: List = [v for v in _imports[self.library] if v.tag != "RangePicker"]
        _vars.append(
            imports.ImportVar(tag="DatePicker"),
        )
        _imports[self.library] = _vars

        return _imports

    def _get_hooks(self) -> str | None:
        return "const { RangePicker } = DatePicker;"


date_picker = DatePicker.create
range_picker = RangePicker.create
