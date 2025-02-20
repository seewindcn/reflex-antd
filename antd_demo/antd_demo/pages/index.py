import reflex as rx
import pydantic

from reflex_antd.base import get_dynamic_ctx
from reflex_antd import (
    helper, display, entry, feedback, general, layout,
    navigation,
    charts,
)

from antd_demo.layout import page

from ..state import GlobalState, MyBaseState


class AntdEditorState(MyBaseState):
    component_str: str = ""
    _com: rx.Component | None = pydantic.PrivateAttr(default=None)

    @rx.var
    def examples(self) -> list[dict[str, str]]:
        return [dict(label=k, value=k) for k in get_examples().keys()]

    async def on_page_load(self):
        self.component_str = ''
        self._com = None

    @rx.event(background=True)
    async def editor_on_change(self, val):
        async with self:
            self.component_str = val

    @rx.event(background=True)
    async def editor_on_example_select(self, v, option):
        examples = get_examples()
        codes = examples.get(v, None)
        if not codes:
            return
        async with self:
            self.component_str = codes
            self.on_refresh()

    def on_refresh(self):
        self._com = None
        self._mark_dirty()


@rx.dynamic
def _dynamic(state: AntdEditorState):
    if isinstance(state._com, rx.Component):
        return state._com

    try:
        if state.component_str == "":
            com = rx.flex()
        else:
            _ctx = get_dynamic_ctx(
                State=AntdEditorState, state=state,
            )
            if 'def ' not in state.component_str:
                com = eval(
                    state.component_str,
                    _ctx,
                )
            else:
                lg = dict()
                exec(state.component_str, _ctx, lg)
                com = lg['component']()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return rx.text(f"Error: {e}")
    if not isinstance(com, rx.Component):
        return rx.text("Invalid component")
    state._com = com
    return com


def _ui_editor() -> rx.Component:
    from ..component.codemirror import python_edit
    _com = python_edit(
        width='500px',
        height='800px',
        value=AntdEditorState.component_str,
        read_only=False,
        theme=helper.casual_var('okaidia'),
        on_change=AntdEditorState.editor_on_change,
    )
    return rx.vstack(
        layout.space(
            rx.text('examples:'),
            entry.select(
                options=AntdEditorState.examples,
                show_search=True,
                on_select=AntdEditorState.editor_on_example_select,
                width='230px',
            ),
            rx.button(
                'dynamic->gen',
                on_click=AntdEditorState.on_refresh,
            ),
        ),
        _com,
    )


def _ui_view() -> rx.Component:
    return rx.vstack(
        rx.card(
            _dynamic(),
            height="100%",
            width='100%',
            flex="1",
        ),
    )


def editor_page() -> rx.Component:
    return rx.hstack(
        _ui_editor(),
        _ui_view(),
    )


_examples = {}


def get_examples() -> dict:
    global _examples
    if _examples:
        return _examples

    import inspect
    pre = '_code_'
    lk = len(pre)
    for k, v in globals().items():
        if not k.startswith(pre):
            continue
        codes = inspect.getsource(v)
        _examples[k[lk:]] = codes.replace(f'def {k}', 'def component')
    return _examples


def _code_card_with_tailwind() -> rx.Component:
    result = rx.card(
        rx.el.div(
            rx.link(
                rx.flex(
                    rx.avatar(src="/reflex_banner.png"),
                    rx.box(
                        rx.heading("Quick Start"),
                        rx.text(
                            "Get started with Reflex in 5 minutes.",
                        ),
                    ),
                    spacing="2",
                ),
            ),
            rx.flex(
                rx.avatar(src="/reflex_banner.png"),
                rx.el.div(
                    rx.heading("Quick Start"),
                    rx.text(
                        "Get started with Reflex in 5 minutes.",
                        height='50px',
                    ),
                    rx.el.div(
                        rx.text("Absolute child"),
                        class_name='absolute bottom-0 left-0 hover:bg-indigo-50',
                    ),
                    class_name='static',
                ),
                spacing="2",
            ),
            class_name='hover:shadow-lg',
        ),
        as_child=True,
    )
    return result


def _code_transfer1() -> rx.Component:
    result = rx.vstack(
        rx.text(
            '测试用',
            class_name='text-1xl hover:underline hover:bg-red-100',
        ),
        rx.box(
            rx.heading("自定义题目样式"),
            entry.transfer(
                data_source=[
                    {'key': str(i), 'title': f'content {i}', 'description': f'description {i}'}
                    for i in range(1, 15)
                ],
                titles=helper.contain(['Source', 'Target']),
                item_render=helper.js_value(
                    lambda record: (record.key + '-' + record.title)
                ),
            ),
        ),
    )
    return result


def _code_checkbox1() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                "简单的 checkbox。",
            ),
            entry.checkbox(),
            rx.text(
                "checkbox 不可用。",
            ),
            entry.checkbox(disabled=True, default_checked=False),
            entry.checkbox(indeterminate=True, disabled=True),
            entry.checkbox(default_checked=True, disabled=True),
            rx.text(
                "方便的从数组生成 Checkbox 组。",
            ),
            entry.checkbox_group(
                options=['Apple', 'Pear', 'Orange'],
                default_value=["Apple"]
            ),
            rx.text(
                "实现全选效果。",
            ),
            entry.checkbox(
                "Check all",
                # on_change=EntryCheckboxState.onCheckAllChange
            ),
            entry.checkbox_group(
                options=['Apple', 'Pear', 'Orange'],
                value=['Apple', 'Orange'],
            ),
        ),
        width="100%",
    )


def _code_form1() -> rx.Component:
    def form1_items(submit) -> list:
        return [
            entry.form_item(
                entry.input(),
                name="username",
                label="username",
                rules=[{"required": True, "message": 'Please input your username!'}]
            ),
            entry.form_item(
                entry.input(),
                name="password",
                label="password",
                rules=[{"required": True, "message": 'Please input your password!'}]
            ),
            entry.form_item(
                general.button("Submit", html_type="submit"),
                wrapper_col={"offset": 8, "span": 16},
            ) if submit else "",
        ]

    return entry.form(
        *form1_items(submit=True),
        # form="myForm",
        name="basic",
        label_col={"span": 8},
        style={"maxWidth": "600"},
        initial_values={"remember": True},
    )


@page('/', '', state=AntdEditorState)
def index_page() -> rx.Component:
    return editor_page()
