import reflex as rx

from reflex_antd import general as antd_g

from antd_demo.layout import page


@page('/')
def index_page() -> rx.Component:
    return rx.center(
        antd_g.button('ok'),
    )


