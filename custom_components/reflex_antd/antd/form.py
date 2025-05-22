from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component

from ..base import (
    AntdComponent, ContainVar, CasualVar, ReactNode,
    JsValue, js_value, JsUseEffect,
    memo_never_no_recursive, memo_always_no_recursive,
    get_unique_variable_name,
)
from ..constant import AlignType, DirectionType, SizeType, VariantType


class Form(AntdComponent):
    tag = 'Form'

    colon: Var[bool]
    component: Var[Union[bool, ReactNode]]
    disabled: Var[bool]
    fields: Var[ContainVar]
    form: Var[Union[str, CasualVar]]
    initial_values: Var[Dict]
    label_align: Var[AlignType]
    label_wrap: Var[bool]
    label_col: Var[Dict]
    layout: Var[DirectionType]
    name: Var[str]
    preserve: Var[bool]
    required_mark: Var[Union[bool, JsValue]]
    scrollTo_first_error: Var[Union[bool, Dict]]
    size: Var[SizeType]
    validate_messages: Var[Dict]
    validate_trigger: Var[Union[str, List[str]]]
    variant: Var[VariantType]
    wrapper_col: Var[Dict]

    # form and form.item can not split, if split some components like select don't work;
    _memoization_mode = memo_never_no_recursive

    @classmethod
    def create(cls, *children, **props) -> Component:
        if 'form' in props:
            # no auto gen form id; sometimes form can not be set, like foreach make a lot of forms
            # if props['form'] is None:
            #     props['form'] = gen_form_id()
            if isinstance(props['form'], str):
                props['form'] = CasualVar.create(f'{props["form"]}')
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

    colon: Var[bool]
    dependencies: Var[List[Union[str, int, List[Union[str, int]]]]]
    extra: Var[ReactNode]
    get_value_from_event: Var[JsValue]
    get_value_props: Var[JsValue]
    has_feedback: Var[Union[bool, ContainVar]]
    help: Var[ReactNode]
    hidden: Var[bool]
    html_for: Var[str]
    initial_value: Var[str]
    label: Var[str]
    label_align: Var[AlignType]
    label_col: Var[Dict]
    message_variables: Var[JsValue]
    name: Var[Union[str, int, List[Union[str, int]]]]
    normalize: Var[JsValue]
    no_style: Var[bool]
    preserve: Var[bool]
    required: Var[bool]
    rules: Var[Union[List[Dict], ContainVar]]
    should_update: Var[bool]
    tooltip: Var[Union[ReactNode, ContainVar]]
    trigger: Var[str]
    validate_debounce: Var[float]
    validate_first: Var[Union[bool, str]]
    validate_status: Var[str]
    validate_trigger: Var[Union[str, List[str]]]
    value_prop_name: Var[str]
    wrapper_col: Var[Dict]


class FormList(AntdComponent):
    tag = 'Form.List'

    # children: Var[JsValue]
    initial_value: Var[List]
    name: Var[Union[str, int, List[Union[str, int]]]]
    rules: Var[ContainVar]


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


def gen_form_id():
    return f'form_{get_unique_variable_name()}'


def form_hook_reset_fields(form_id: str, state, dep_name: str = None) -> JsValue:
    _hook = JsUseEffect(
        state,
        f""" {str(form_id)}.resetFields(); """,
        dep_name=dep_name,
    )
    return _hook


def _modal_form(
        modal_type: str, *children: Component,
        others: list[Component] = None,
        modal_config=None, form_id: str = None,
        # form_params: dict[str, Any] = None,
        **props) -> JsValue | Component:
    from . import modal
    if form_id is None:
        form_id = gen_form_id()
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
      console.log('{form_id}.validateFields error:', err);
      err.stack = '{form_id}.validateFields error';
      reject(err)}});
      }});//if catch, modal will close the form //.catch(() => console.log('Oops errors!'));
      }}
    """)
    if others is None:
        others = []
    op = getattr(modal, modal_type)
    if modal_type == 'modal':
        modal_config.update(
            after_open_change=js_value(f"""(open) => {{{form_id}.resetFields()}}""", to_js=True),
        )
        modal = op(
            f,
            *others,
            # on_open=JsValue(f'{form_id}.resetFields()'),
            **modal_config)
        return modal
    else:
        # confirm
        modal_config['content'] = [f, *others]
        form_params = props.get('initial_values', None)
        if form_params is not None:
            # 初始化form表单字段值
            modal_config.update(
                before_open=js_value(f""" {form_id}.setFieldsValue({str(form_params).strip('{}')}) """),
            )
        before_open = modal_config.pop('before_open', None)
        return op(config=modal_config, before_open=before_open)


def modal_form(
        *children, others: list[Component] = None,
        modal_config=None, form_id: str = None, **props) -> Component:
    return _modal_form('modal', *children,
                       others=others, modal_config=modal_config, form_id=form_id, **props)


def confirm_form(
        *children, others: list[Component] = None,
        confirm_config=None, form_id: str = None, **props) -> JsValue:
    """ confirm模式, 使用 useContext(EventLoopContext); 会报错, """
    return _modal_form('confirm', *children,
                       others=others,
                       modal_config=confirm_config, form_id=form_id, **props)
