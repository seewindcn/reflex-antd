from typing import Optional, Union, Dict, Any, List
from reflex import Var

from ..base import AntdComponent, ContainVar
from ..constant import StatusType, SizeType


class Form(AntdComponent):
    tag = 'Form'

    colon: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    name: Optional[Var[str]]
    label_col: Optional[Var[Dict]]
    wrapper_col: Optional[Var[Dict]]
    initial_values: Optional[Var[Dict]]
    auto_complete: Optional[Var[str]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            'onFinish': lambda values: [values],
        })
        return _triggers


class FormItem(AntdComponent):
    tag = 'Form.Item'

    label: Optional[Var[str]]
    name: Optional[Var[str]]
    value_prop_name: Optional[Var[str]]
    wrapper_col: Optional[Var[Dict]]

    rules: Optional[Var[List[Dict]]]


form = Form.create
form_item = FormItem.create
