import reflex as rx

from reflex_antd import general

from antd_demo.layout import page
from antd_demo.state import GlobalState


@page('/general', 'general')
def general_page() -> rx.Component:
    return rx.center(
        rx.text('general-page aa'),
        rx.hstack(
            general.button(
                'ok',
                icon=general.icon(
                    'QuestionCircleOutlined',
                    spin=True,
                    two_tone_color="#52c41a",
                ),
            ),
            general.float_button(
                GlobalState.tooltip,
                icon=general.icon('InsertRowAboveOutlined'),
                tooltip=GlobalState.tooltip,
                right=94,
                on_click=GlobalState.tooltip_click,
            ),
        ),
    )
