import reflex as rx

from reflex_antd import general as antd_g

from antd_demo.layout import page


@page('/general')
def general_page() -> rx.Component:
    return rx.center(
        rx.text('general page'),
        antd_g.button('ok'),
    )


