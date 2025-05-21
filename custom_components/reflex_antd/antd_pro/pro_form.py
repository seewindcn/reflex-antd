from __future__ import annotations

from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var
from reflex.event import EventHandler, passthrough_event_spec
from reflex_antd.antd import form, modal

from ..constant import AlignType, DirectionType, SizeType, VariantType
from ..base import ContainVar, JsValue, ReactNode, ExTypes, PropBase, CasualVar
from .base import AntdProBaseComponent


class FormProps(PropBase):
    grid: Var[bool]
    row_props: Var[dict | ExTypes]
    readonly: Var[bool]
    trigger: Var[ReactNode | ExTypes]
    submitter: Var[bool | ContainVar]

    # form
    colon: Optional[Var[bool]]
    component: Optional[Var[Union[bool, ReactNode]]]
    disabled: Optional[Var[bool]]
    fields: Optional[Var[ContainVar]]
    form: Optional[Var[Union[str, CasualVar]]]
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


class ProForm(AntdProBaseComponent, form.Form):
    tag = 'ProForm'

    form_ref: Var[CasualVar]
    grid: Var[bool]
    row_props: Var[dict | ExTypes]
    readonly: Var[bool]
    trigger: Var[ReactNode | ExTypes]
    submitter: Var[bool | ContainVar]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            'on_collapse': lambda collapsed: [collapsed],
        })
        return _triggers


class QueryFilter(ProForm):
    tag = 'QueryFilter'


class Column(PropBase):
    """ json定义 """
    key: str
    data_index: str | list[str]
    value_type: str  # select|group|formList|formSet|dateTime|dateRange
    value_enum: dict  # all: { text: '全部', status: 'Default', disabled: false},
    title: ReactNode
    tooltip: str
    field_props: dict | ExTypes  # {style: {width: '20px'},}
    form_item_props: dict | ExTypes
    form_item_props_rules: list
    pro_field_props: ExTypes
    render_text: ExTypes
    render: ExTypes
    render_form_item: ExTypes  # () => <DatePicker.RangePicker />
    request: ExTypes
    params: dict
    dependencies: str | int | list[str | int]
    hide_in_descriptions: bool
    hide_in_form: bool
    hide_in_table: bool
    hide_in_search: bool
    columns: list[Column] | ExTypes
    width: str
    initial_value: str | int | list | dict  # [dayjs().add(-1, 'm'), dayjs()]  [{ state: 'all', title: '标题' }]
    col_props: dict
    row_props: dict
    convert_value: ExTypes
    transform: ExTypes


class StepForm(ProForm):
    tag = 'StepsForm.StepForm'

    step_props: Var[dict | ExTypes]
    on_finish: EventHandler[passthrough_event_spec(Any)]


class StepsForm(ProForm):
    tag = 'StepsForm'

    current: Var[int]
    steps: Var[list | ExTypes]
    steps_props: Var[dict | ExTypes]
    step_form_render: Var[ExTypes]
    steps_form_render: Var[ExTypes]
    steps_render: Var[ExTypes]
    form_ref: Var[ExTypes]

    on_finish: EventHandler[passthrough_event_spec(Any)]


class ModalForm(ProForm):
    tag = 'ModalForm'

    open: Var[bool]
    modal_props: Var[dict | ExTypes]
    title: Var[ReactNode]
    width: Var[int | str]
    submit_timeout: Var[int]
    submitter: Var[bool | ContainVar]
    on_open_change: EventHandler[passthrough_event_spec(bool)]


class DrawerForm(ProForm):
    tag = 'DrawerForm'

    resize: Var[bool | ExTypes]
    drawer_props: Var[dict | ExTypes]
    title: Var[ReactNode]
    width: Var[int | str]
    submit_timeout: Var[int]

    on_open_change: EventHandler[passthrough_event_spec(bool)]


class SchemaForm(ProForm):
    tag = 'BetaSchemaForm'

    layout_type: Var[str]  # Form|ModalForm|DrawerForm|LightFilter|QueryFilter|StepsForm|StepForm|Embed
    steps: Var[list | ExTypes]  # StepFormProps[]
    columns: Var[list[dict] | list[Column] | ExTypes]
    should_update: Var[ExTypes]


class ProFormGroup(AntdProBaseComponent):
    tag = 'ProFormGroup'

    title: Var[str]
    collapsible: Var[bool]


class ProFormList(AntdProBaseComponent):
    tag = 'ProFormList'

    name: Var[str]
    label: Var[str]
    col_props: Var[dict | ExTypes]
    copy_icon_props: Var[ExTypes | bool]  # { Icon: SmileOutlined, tooltipText: '复制此项到末尾' }
    delete_icon_props: Var[ExTypes | bool]
    # {creatorButtonText: '新建', icon: false, type: 'link', style: { width: 'unset' }, }
    creator_button_props: Var[ExTypes]
    initial_value: Var[list[dict] | ExTypes]
    always_show_item_label: Var[bool]
    rules: Var[ExTypes | list]
    min: Var[int]
    item_container_render: Var[ExTypes]
    item_render: Var[ExTypes]  # ({ listDom, action }) => Component


class ProFormSet(AntdProBaseComponent):
    tag = 'ProFormSet'


class ProFormField(AntdProBaseComponent, form.FormItem):
    tag = 'ProForm.Item'

    col_props: Var[dict | ExTypes]
    field_props: Var[dict | ExTypes]
    placeholder: Var[str]
    width: Var[int | str]  # 'sm' | 'md' | 'xl' | 'xs' | 'lg'
    allow_clear: Var[bool]
    is_list_field: Var[bool]


class ProFormText(ProFormField):
    tag = 'ProFormText'


class ProFormTextPassword(ProFormField):
    tag = 'ProFormText.Password'


class ProFormDigit(ProFormField):
    tag = 'ProFormDigit'


class ProFormTextArea(ProFormField):
    tag = 'ProFormTextArea'


class ProFormDatePicker(ProFormField):
    tag = 'ProFormDatePicker'


class ProFormSelect(ProFormField):
    """
    field_props:
        labelInValue: true
        mode: 'multiple'
     """
    tag = 'ProFormSelect'

    value_enum: Var[dict | ExTypes]
    request: ExTypes
    show_search: Var[bool]
    debounce_time: Var[int]


class ProFormTreeSelect(ProFormSelect):
    tag = 'ProFormTreeSelect'


class ProFormCascader(ProFormField):
    """
    field_props:
        changeOnSelect: true,
     """
    tag = 'ProFormCascader'


class ProFormCheckbox(ProFormField):
    tag = 'ProFormCheckbox'


class ProFormRadioGroup(ProFormField):
    tag = 'ProFormRadio.Group'

    value_enum: Var[dict | ExTypes]
    request: ExTypes
    options: Var[list | ExTypes]  # {label:xx, value:xx} , ['xx','bb',...]
    layout: Var[str]  # vertical|horizontal
    radio_type: Var[str]  # button|


class ProFormColorPicker(ProFormField):
    tag = 'ProFormColorPicker'


class ProFormSlider(ProFormField):
    tag = 'ProFormSlider'

    marks: Var[dict]


class ProFormSwitch(ProFormField):
    tag = 'ProFormSwitch'


class ProFormUploadButton(ProFormField):
    tag = 'ProFormUploadButton'


class ProFormSegmented(ProFormField):
    tag = 'ProFormSegmented'


pro_form = ProForm.create
query_filter = QueryFilter.create
step_form = StepForm.create
steps_form = StepsForm.create
modal_form = ModalForm.create
drawer_form = DrawerForm.create

schema_form = SchemaForm.create

pro_form_group = ProFormGroup.create
pro_form_list = ProFormList.create
pro_form_set = ProFormSet.create

pro_form_item = ProFormField.create
pro_form_text = ProFormText.create
pro_form_digit = ProFormDigit.create
pro_form_textarea = ProFormTextArea.create
pro_form_date_picker = ProFormDatePicker.create
pro_form_select = ProFormSelect.create
pro_form_radio = ProFormRadioGroup.create
