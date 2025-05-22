from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import DatePickerModeType, DatePickerType, SizeType, PlacementType, StatusType, VariantType

from .base import Locale, DayJS
from .date_picker import RangePicker as DateRangePicker


class TimePicker(AntdComponent):
    tag = 'TimePicker'

    allow_clear: Var[Union[bool, ContainVar]]
    auto_focus: Var[bool]
    cell_render: Var[JsValue]
    change_on_scroll: Var[bool]
    default_value: Var[DayJS]
    disabled: Var[bool]
    disabled_time: Var[JsValue]
    format: Var[str]
    get_popup_container: Var[JsValue]
    hide_disabled_options: Var[bool]
    hour_step: Var[int]
    input_read_only: Var[bool]
    minute_step: Var[int]
    need_confirm: Var[bool]
    open: Var[bool]
    placeholder: Var[Union[str, List[str]]]
    placement: Var[PlacementType]
    popup_class_name: Var[str]
    popup_style: Var[ContainVar]
    prefix: Var[ReactNode]
    render_extra_footer: Var[JsValue]
    second_step: Var[int]
    show_now: Var[bool]
    size: Var[SizeType]
    status: Var[StatusType]
    suffix_icon: Var[ReactNode]
    use12_hours: Var[bool]
    value: Var[DayJS]
    variant: Var[VariantType]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_OPEN_CHANGE: lambda open: [open],
            'on_calendar_change': lambda dates, date_strs, info: [dates, date_strs, info],
        })
        return _triggers

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("dayjs", []).append(
            imports.ImportVar(tag="dayjs", is_default=True, install=False),
        )
        return _imports


class RangePicker(DateRangePicker):
    tag = 'TimePicker.RangePicker'

    order: Var[bool]

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        # _vars: List = [v for v in _imports[self.library] if v.tag != "RangePicker"]
        # _vars.append(
        #     imports.ImportVar(tag="TimePicker"),
        # )
        # _imports[self.library] = _vars

        return _imports

    def _get_hooks(self) -> str | None:
        ...
        # return "const { RangePicker } = TimePicker;"


time_picker = TimePicker.create
range_picker = RangePicker.create
