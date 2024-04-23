from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue, ReactNode
from ..constant import AlignType, DirectionType, SizeType, VariantType


class Form(AntdComponent):
    tag = 'Form'

    colon: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    fields: Optional[Var[ContainVar]]
    initial_values: Optional[Var[Dict]]
    label_align: Optional[Var[AlignType]]
    label_wrap: Optional[Var[bool]]
    label_col: Optional[Var[Dict]]
    layout: Optional[Var[DirectionType]]
    name: Optional[Var[str]]
    preserve: Optional[Var[bool]]
    required_mark: Optional[Var[Union[bool, JsValue]]]
    scrollTo_first_error: Optional[Var[Union[bool, Dict]]]
    size: Optional[Var[SizeType]]
    validate_messages: Optional[Var[Dict]]
    validate_trigger: Optional[Var[Union[str, List[str]]]]
    variant: Optional[Var[VariantType]]
    wrapper_col: Optional[Var[Dict]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_fields_change": lambda changed, all: [changed],
            'on_finish': lambda values: [values],
            "on_finish_failed": lambda ev: [ev.values, ev.errorFields, ev.outOfDate],
            "on_values_change": lambda changed, all: [changed, all],
        })
        return _triggers


class FormItem(AntdComponent):
    tag = 'Form.Item'

    colon: Optional[Var[bool]]
    dependencies: Optional[Var[List[Union[str, int, List[Union[str, int]]]]]]
    extra: Optional[Var[ReactNode]]
    getValue_from_event: Optional[Var[JsValue]]
    get_value_props: Optional[Var[JsValue]]
    has_feedback: Optional[Var[Union[bool, ContainVar]]]
    help: Optional[Var[ReactNode]]
    hidden: Optional[Var[bool]]
    html_for: Optional[Var[str]]
    initial_value: Optional[Var[str]]
    label: Optional[Var[str]]
    label_align: Optional[Var[AlignType]]
    label_col: Optional[Var[Dict]]
    message_variables: Optional[Var[JsValue]]
    name: Optional[Var[Union[str, int, List[Union[str, int]]]]]
    normalize: Optional[Var[JsValue]]
    no_style: Optional[Var[bool]]
    preserve: Optional[Var[bool]]
    required: Optional[Var[bool]]
    rules: Optional[Var[Union[List[Dict], ContainVar]]]
    should_update: Optional[Var[bool]]
    tooltip: Optional[Var[Union[Component, ContainVar]]]
    trigger: Optional[Var[str]]
    validate_debounce: Optional[Var[float]]
    validate_first: Optional[Var[Union[bool, str]]]
    validate_status: Optional[Var[str]]
    validate_trigger: Optional[Var[Union[str, List[str]]]]
    value_prop_name: Optional[Var[str]]
    wrapper_col: Optional[Var[Dict]]

    rules: Optional[Var[List[Dict]]]


class FormList(AntdComponent):
    tag = 'Form.List'

    # children: Optional[Var[JsValue]]
    initial_value: Optional[Var[List]]
    name: Optional[Var[Union[str, int, List[Union[str, int]]]]]
    rules: Optional[Var[ContainVar]]


class FormProvider(AntdComponent):
    tag = 'Form.Provider'

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_form_change": lambda form_name, info: [form_name, info],
            'on_form_finish': lambda form_name, info: [form_name, info],
        })
        return _triggers


form = Form.create
form_item = FormItem.create
form_list = FormList.create
form_provider = FormProvider.create
