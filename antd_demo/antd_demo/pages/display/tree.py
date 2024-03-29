import reflex as rx

from reflex_antd import display, general, helper

from antd_demo.layout import page


class TreeState(rx.State):
    data = [
        dict(title='parent-1', key='0', children=[
            dict(title='child-1', key='0-1', children=[

            ]),
            dict(title='child-2', key='0-2', children=[
                dict(title='node-1', key='0-2-1', )
            ]),
        ]),
    ]

    def on_load(self):
        pass


@page('/display/tree1', 'display',
      on_load=TreeState.on_load)
def tree1_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            display.tree(
                tree_data=TreeState.data,
                checkable=True,
            ),
        ),
    )

