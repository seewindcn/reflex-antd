import reflex as rx

from reflex_antd import general, entry

from antd_demo.layout import page

from ..state import GlobalState


@page('/')
def index_page() -> rx.Component:
    return rx.center(
        rx.button('ok'),
    )


