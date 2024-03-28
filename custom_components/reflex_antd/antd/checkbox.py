from typing import Optional, Union, Dict, Any, List
from reflex import Var
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar
from ..constant import StatusType, SizeType


class Checkbox(AntdComponent):
    tag = "Checkbox"

    auto_focus: Optional[Var[bool]]
    checked: Optional[Var[bool]]
    default_checked: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    indeterminate: Optional[Var[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda e: [e],
        })
        return _triggers


class CheckboxGroup(AntdComponent):
    tag = 'Checkbox.Group'

    default_value: Optional[Var[List[Union[int, str]]]]
    disabled: Optional[Var[bool]]
    name: Optional[Var[str]]
    options: Optional[Var[List[Union[str, int, Dict]]]]
    value: Optional[Var[List[Union[int, str, bool]]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda checked_value: [checked_value],
        })
        return _triggers


checkbox = Checkbox.create
checkbox_group = CheckboxGroup.create



