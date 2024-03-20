import reflex as rx

from antd_demo.layout import page


@page('/')
def index_page() -> rx.Component:
    return rx.center(
        rx.button('ok'),
    )


