import reflex as rx

from reflex_antd import general, entry, helper

from antd_demo.layout import page
from ..state import GlobalState


@page('/entry/form1', 'entry')
def form1_page() -> rx.Component:
    return rx.center(
        entry.form(
            entry.form_item(
                entry.input(),
                label='Username',
                name='Username',
                rules=[dict(required=True, message='Please input your username!')]
            ),
            entry.form_item(
                entry.password(),
                label='Password',
                name='Password',
                rules=[dict(required=True, message='Please input your password!')]
            ),
            entry.form_item(
                entry.checkbox(),
                name='remember',
                value_prop_name='checked',
                wrapper_col=dict(offset=8, span=16),
            ),
            entry.form_item(
                entry.date_picker(
                    default_value=helper.contain([
                        entry.dayjs('2000-01-01'),
                        entry.dayjs('2000-01-03'),
                    ]),
                    multiple=True,
                ),
                name='date_picker',
            ),
            entry.form_item(
                entry.range_picker(
                    default_value=helper.contain([
                        entry.dayjs('2000-01-01'),
                        entry.dayjs('2000-01-03'),
                    ]),
                ),
                name='range_picker',
            ),
            entry.form_item(
                general.button(
                    'Submit',
                    type='primary',
                    html_type='submit',
                ),
            ),

            name='basic',
            label_col=dict(span=8),
            wrapper_col=dict(span=16),
            max_width=600,
            auto_complete='off',
            on_finish=GlobalState.on_event1,
        ),
    )

