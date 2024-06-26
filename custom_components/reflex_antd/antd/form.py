import uuid
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component

from ..base import (AntdComponent, ContainVar, JsValue, ReactNode, js_value,
                    memo_never_no_recursive, memo_always_no_recursive)
from ..constant import AlignType, DirectionType, SizeType, VariantType


class Form(AntdComponent):
    tag = 'Form'

    colon: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    fields: Optional[Var[ContainVar]]
    form: Optional[Var[str]]
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

    # form and form.item can not split, if split some components like select don't work;
    _memoization_mode = memo_never_no_recursive

    @classmethod
    def create(cls, *children, **props) -> Component:
        if 'form' in props and isinstance(props['form'], str):
            props['form'] = Var.create_safe(f'{props["form"]}', _var_is_local=False, _var_is_string=False)
        comp = super().create(*children, **props)
        if comp._get_all_hooks() or comp._get_all_hooks_internal():
            comp._memoization_mode = memo_always_no_recursive
        return comp

    def _get_hooks(self) -> str | None:
        if hasattr(self, 'form') and self.form is not None:
            return f"const [{str(self.form).strip('{}')}] = Form.useForm();"

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
    tooltip: Optional[Var[Union[ReactNode, ContainVar]]]
    trigger: Optional[Var[str]]
    validate_debounce: Optional[Var[float]]
    validate_first: Optional[Var[Union[bool, str]]]
    validate_status: Optional[Var[str]]
    validate_trigger: Optional[Var[Union[str, List[str]]]]
    value_prop_name: Optional[Var[str]]
    wrapper_col: Optional[Var[Dict]]


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


def _modal_form(modal_type: str, *children, modal_config=None, form_id: str = None, **props) -> JsValue | Component:
    from . import modal
    if form_id is None:
        form_id = f'form_{uuid.uuid4().hex}'
    props.update(
        form=form_id,
        preserve=False,
    )
    f = form(*children, **props)
    f._memoization_mode = memo_never_no_recursive

    modal_config = modal_config or {}
    modal_config.update(destroy_on_close=True)
    modal_config['on_ok'] = js_value(f"""() => {{
        return new Promise((resolve, reject) => {{
    {form_id}
      .validateFields({{
        validateOnly: false,
      }})
      .then(() => {{
        {form_id}.submit();
      resolve()}})
      .catch((err) => {{
      console.log('{form_id}.validateFields error:', err)
      reject()}});
      }});//if catch, modal will close the form //.catch(() => console.log('Oops errors!'));
      }}
    """)
    op = getattr(modal, modal_type)
    if modal_type == 'confirm':
        modal_config['content'] = f
        return op(config=modal_config)
    else:
        modal_config['after_open_change'] = js_value(f"""(open) => {{{form_id}.resetFields()}}""")
        modal = op(
            f,
            # on_open=JsValue(f'{form_id}.resetFields()'),
            **modal_config)
        return modal


def modal_form(*children, modal_config=None, form_id: str = None, **props) -> Component:
    return _modal_form('modal',
                       *children, modal_config=modal_config, form_id=form_id, **props)


def confirm_form(*children, confirm_config=None, form_id: str = None, **props) -> JsValue:
    return _modal_form('confirm',
                       *children, modal_config=confirm_config, form_id=form_id, **props)
