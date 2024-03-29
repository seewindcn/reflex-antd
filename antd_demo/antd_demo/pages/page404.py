import reflex as rx

from antd_demo.layout import page


contents = f"""
# Page Not Found

The page at `{rx.State.router.page.raw_path}` doesn't exist.
"""


@page('/404', '', title='Page Not Found')
def page404_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.markdown(contents),
            rx.spacer(),
            height="80vh",
            width="100%",
        )
    )

