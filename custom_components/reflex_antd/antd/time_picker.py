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

    allow_clear: Optional[Var[Union[bool, ContainVar]]]
    auto_focus: Optional[Var[bool]]
    cell_render: Optional[Var[JsValue]]
    change_on_scroll: Optional[Var[bool]]
    default_value: Optional[Var[DayJS]]
    disabled: Optional[Var[bool]]
    disabled_time: Optional[Var[JsValue]]
    format: Optional[Var[str]]
    get_popup_container: Optional[Var[JsValue]]
    hide_disabled_options: Optional[Var[bool]]
    hour_step: Optional[Var[int]]
    input_read_only: Optional[Var[bool]]
    minute_step: Optional[Var[int]]
    need_confirm: Optional[Var[bool]]
    open: Optional[Var[bool]]
    placeholder: Optional[Var[Union[str, List[str]]]]
    placement: Optional[Var[PlacementType]]
    popup_class_name: Optional[Var[str]]
    popup_style: Optional[Var[ContainVar]]
    prefix: Optional[Var[ReactNode]]
    render_extra_footer: Optional[Var[JsValue]]
    second_step: Optional[Var[int]]
    show_now: Optional[Var[bool]]
    size: Optional[Var[SizeType]]
    status: Optional[Var[StatusType]]
    suffix_icon: Optional[Var[ReactNode]]
    use12_hours: Optional[Var[bool]]
    value: Optional[Var[DayJS]]
    variant: Optional[Var[VariantType]]

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

    order: Optional[Var[bool]]

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
