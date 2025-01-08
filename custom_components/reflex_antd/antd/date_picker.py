from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import DatePickerModeType, DatePickerType, SizeType, PlacementType, StatusType, VariantType

from .base import Locale, DayJS


class BaseDatePicker(AntdComponent):
    allow_clear: Optional[Var[bool]]
    auto_focus: Optional[Var[bool]]
    date_render: Optional[Var[JsValue]]
    cell_render: Optional[Var[JsValue]]
    components: Optional[Var[Union[ReactNode, list, dict, ContainVar]]]
    disabled: Optional[Var[bool]]
    disabled_date: Optional[Var[JsValue]]
    format: Optional[Var[ContainVar]]
    order: Optional[Var[bool]]
    popup_class_name: Optional[Var[str]]
    preserve_invalidOn_blur: Optional[Var[bool]]
    get_popup_container: Optional[Var[JsValue]]
    input_readOnly: Optional[Var[bool]]
    locale: Optional[Var[Locale]]
    min_date: Optional[Var[JsValue]]
    max_date: Optional[Var[JsValue]]
    mode: Optional[Var[DatePickerModeType]]
    need_confirm: Optional[Var[bool]]
    next_icon: Optional[Var[ReactNode]]
    open: Optional[Var[bool]]
    panel_render: Optional[Var[JsValue]]
    picker: Optional[Var[DatePickerType]]
    placeholder: Optional[Var[Union[str, List[str]]]]
    placement: Optional[Var[PlacementType]]
    popup_style: Optional[Var[ContainVar]]
    presets: Optional[Var[ContainVar]]
    prev_icon: Optional[Var[ReactNode]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[StatusType]]
    suffix_icon: Optional[Var[ReactNode]]
    super_next_icon: Optional[Var[ReactNode]]
    super_prev_icon: Optional[Var[ReactNode]]
    variant: Optional[Var[VariantType]]

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

    default_picker_value: Optional[Var[JsValue]]
    default_value: Optional[Var[ContainVar]]
    disabled_time: Optional[Var[JsValue]]
    format: Optional[Var[ContainVar]]
    multiple: Optional[Var[bool]]
    picker_value: Optional[Var[ContainVar]]
    render_extra_footer: Optional[Var[JsValue]]
    show_now: Optional[Var[bool]]
    show_time: Optional[Var[Union[bool, ContainVar]]]
    # showTime.defaultValue
    show_week: Optional[Var[bool]]
    value: Optional[Var[ContainVar]]

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

    allow_empty: Optional[Var[Tuple[bool, bool]]]
    cell_render: Optional[Var[JsValue]]
    date_render: Optional[Var[JsValue]]
    default_picker_value: Optional[Var[ContainVar]]
    default_value: Optional[Var[ContainVar]]
    disabled: Optional[Var[Tuple[bool, bool]]]
    disabled_time: Optional[Var[JsValue]]
    format: Optional[Var[ContainVar]]
    id: Optional[Var[Dict[str, str]]]
    picker_value: Optional[Var[ContainVar]]
    presets: Optional[Var[ContainVar]]
    render_extra_footer: Optional[Var[JsValue]]
    separator: Optional[Var[ReactNode]]
    show_time: Optional[Var[Union[bool, ContainVar]]]
    # showTime.defaultValue
    value: Optional[Var[ContainVar]]

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
