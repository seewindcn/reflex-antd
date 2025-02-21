import time
from typing import List, Any, Dict, Optional
import asyncio

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout, feedback

from antd_demo.layout import page


class FeedbackBaseState(State):
    active_key: str = 'alert'


class FeedbackDrawerState(State):
    open: bool = False

    def on_close(self):
        self.open = False

    def change_open(self):
        self.open = not self.open


class FeedbackModalState(State):
    open: bool = False
    count: int = 0
    initial_values: Dict[str, Any] = dict(
        username='user-0',
    )

    def change_open(self):
        self.open = True

    def on_ok(self):
        self.before_open('on_ok')
        self.open = not self.open

    def on_cancel(self):
        self.open = False

    def on_finish(self, values):
        print('on_finish:', values)
        self.on_cancel()

    def after_open_change(self, open):
        print('after_open_change:', open)

    def before_open(self, key):
        self.count += 1
        print('before_open:', key, self.count)
        self.initial_values['username'] = f'user-{self.count}'


class FeedbackSyncModalState(State):
    open: bool = False
    confirm_loading: bool = False

    def change_open(self):
        self.open = True

    @rx.event(background=True)
    async def on_ok(self):
        async with self:
            self.confirm_loading = not self.confirm_loading
        time.sleep(2)
        async with self:
            self.open = not self.open
            self.confirm_loading = not self.confirm_loading

    def on_cancel(self):
        self.open = not self.open


class FeedbackMessageState(State):
    cfg: Optional[dict] = None
    cfg1: dict = dict(
        key=2,
        type='success',
        content='cfg1 loading ok',
        duration=5,
    )
    type1: str = 'success'
    ctx1: str = 'message from state'

    @rx.event(background=True)
    async def on_click(self):
        async with self:
            self.exchange_cfg()
        # yield
        await asyncio.sleep(5)
        async with self:
            self.exchange_cfg()
        await asyncio.sleep(3)
        async with self:
            self.cfg = None

    def exchange_cfg(self):
        if self.cfg and self.cfg['type'] == 'loading':
            self.cfg = dict(
                key=0,
                type='success',
                content='cfg loading ok',
            )
        else:
            self.cfg = dict(
                key=0,
                type='loading',
                content='cfg loading....',
                duration=0,
            )


class FeedbackNotificationState(State):
    def on_notify(self, playment: str):
        return feedback.notifications.info(
            'title',
            "Notification Title",
            placement=playment,
            duration=2,
        )


@rx.memo
def antd_feedback_alert() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("最简单的用法，适用于简短的警告提示。"),
            feedback.alert(message=rx.text('Success Text.'), type="success", width=200),
            feedback.alert(message=rx.text('Info  Text.'), type="info", width=200),
            feedback.alert(message=rx.text('Warning  Text.'), type="warning", width=200),
            feedback.alert(message=rx.text('Error  Text.'), type="error", width=200),
            rx.text("显示关闭按钮，点击可关闭警告提示。"),
            feedback.alert(
                message=rx.text('Warning Text '),
                description=rx.text('Warning Text Warning TextW arning Text Warning Text Warning TextWarning Text.'),
                type="warning",
                closable=True),
            feedback.alert(
                message=rx.text('Error Description'),
                description=rx.text(
                    'Error Description Error Description Error Description Error Description Error Description.'),
                type="error", closable=True),
            rx.text("可口的图标让信息类型更加醒目。"),
            feedback.alert(message=rx.text('Success Tips'), type="error", show_icon=True, width=200),
            feedback.alert(message=rx.text('Informational Notes'), type="info", show_icon=True, width=200),
        ),
        width="100%",
    )


@rx.memo
def antd_feedback_drawer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("基础抽屉，点击触发按钮抽屉从右滑出，点击遮罩区关闭。"),
            rx.button(
                "Open",
                on_click=FeedbackDrawerState.change_open
            ),
            feedback.drawer(
                rx.text("content"),
                title=rx.text("Basic Drawer"),
                open=FeedbackDrawerState.open,
                mask_closable=True,
                keyboard=False,
                size="large",
                on_close=FeedbackDrawerState.on_close,
                # helper.js_event(
                #     FeedbackDrawerState.on_close,
                #     js=""" e.preventDefault(); var e = ''; """,
                #     event_trigger=lambda: [],
                # ),
                extra=rx.spacer(
                    general.button(
                        "Cancel",
                        on_click=FeedbackDrawerState.change_open
                    ),
                    general.button(
                        "OK",
                        on_click=FeedbackDrawerState.change_open
                    ),
                ),
            ),

        ),
        width="100%",
    )


@helper.stateful
def antd_feedback_message() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("基础抽屉，点击触发按钮抽屉从右滑出，点击遮罩区关闭。"),
            general.button(
                f"Display normal {FeedbackMessageState.ctx1} use global api",
                on_click=feedback.message(
                    is_global=True,
                    type="success",
                    content='Hello, Ant Design!',
                ),
            ),
            layout.divider(),
            general.button(
                "Display normal message use global api and config",
                on_click=feedback.message(
                    is_global=True,
                    config=FeedbackMessageState.cfg1,
                ),
            ),
            layout.divider(),
            rx.hstack(
                general.button(
                    'Display message by change state.cfg from back ground task',
                    on_click=FeedbackMessageState.on_click,
                ),
                feedback.message_holder(
                    msg=feedback.message(
                        is_global=False,
                        config=FeedbackMessageState.cfg,
                    ),
                ),
            ),
            layout.divider(),
        ),
        width="100%",
    )


@rx.memo
def antd_feedback_notification() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("使用 placement 可以配置通知从上面、下面、左上角、右上角、左下角、右下角弹出。"),
            general.button(
                "top",
                on_click=lambda: FeedbackNotificationState.on_notify('top'),
            ),
            general.button(
                "topLeft",
                on_click=lambda: FeedbackNotificationState.on_notify('topLeft'),
            ),
            general.button(
                "topRight",
                on_click=lambda: FeedbackNotificationState.on_notify('topRight'),
            ),
            general.button(
                "bottomLeft",
                on_click=lambda: FeedbackNotificationState.on_notify('bottomLeft'),
            ),

        ),
        width="100%",
    )


@helper.stateful
def stateful_test() -> rx.Component:
    return rx.button('okkkkkkkkkk', id='ccccccc')


def _modal_form1() -> rx.Component:
    from .entry import entry as antd_entry
    return rx.flex(
        general.button(
            'modal +form',
            on_click=entry.confirm_form(
                *antd_entry.form1_items(submit=False),
                confirm_config=dict(
                    title='modal + form',
                    icon=general.icon('ExclamationCircleFilled'),
                    # before_open=helper.js_event(
                    #     FeedbackModalState.before_open,
                    #     js="""(e) => {
                    #     let key= 1;
                    #     %(name)s(key);
                    #     }""",
                    #     fmt=True,
                    #     event_trigger=lambda v: [v],
                    # ),
                ),
                form_id='myForm',
                on_finish=helper.js_event(FeedbackModalState.on_finish),
                initial_values=FeedbackModalState.initial_values,
            ),
        )
    )


def _modal_form2() -> rx.Component:
    from .entry import entry as antd_entry
    return rx.flex(
        entry.modal_form(
            *antd_entry.form1_items(submit=False),
            modal_config=dict(
                open=FeedbackModalState.open,
                on_cancel=FeedbackModalState.on_cancel,
                mask_closable=False,
                title='modal + form2',
                icon=general.icon('ExclamationCircleFilled'),
                before_open=helper.js_event(
                    FeedbackModalState.before_open,
                    js="""(e) => {
                let key= 1;
                %(name)s(key);
                }""",
                    fmt=True,
                    event_trigger=lambda v: [v],
                ),
            ),
            form_id='myForm2',
            on_finish=helper.js_event(FeedbackModalState.on_finish),
            initial_values=FeedbackModalState.initial_values,
        ),
        rx.button('open-modal2', on_click=FeedbackModalState.on_ok)
    )


@rx.memo
def antd_feedback_modal() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("基础弹框。"),
            # general.button(
            #     "Open Modal",
            #     on_click=FeedbackModalState.change_open
            # ),
            feedback.modal(
                rx.box(
                    rx.el.p('Data disk type: MongoDB'),
                    rx.el.p('Database version: 3.4'),
                ),
                title=rx.text("Basic Modal"),
                # open=FeedbackModalState.open,
                ok_type="default",
                on_ok=FeedbackModalState.on_ok,
                on_cancel=FeedbackModalState.on_cancel
            ),
            rx.text("点击确定后异步关闭对话框，例如提交表单。"),
            rx.button(
                "Open Modal with async logic",
                on_click=FeedbackSyncModalState.change_open
            ),
            feedback.modal(
                rx.text("The modal will be closed after two seconds"),
                title=rx.text("Basic Modal"),
                open=FeedbackSyncModalState.open,
                ok_type="default",
                confirm_loading=FeedbackSyncModalState.confirm_loading,
                on_ok=FeedbackSyncModalState.on_ok,
                on_cancel=FeedbackSyncModalState.on_cancel
            ),
            layout.divider(),
            general.button(
                "Open Modal by confirm",
                on_click=feedback.confirm(
                    config=dict(
                        title='Do you want to delete these items?',
                        icon=general.icon('ExclamationCircleFilled'),
                        content='Some descriptions',
                        on_ok=helper.js_event(FeedbackModalState.on_ok),
                    ),
                ),
            ),
            layout.divider(),
            _modal_form1(),
            layout.divider(),
            _modal_form2(),
        ),
        width="100%",
    )


@page('/demo/feedback', 'feedback')
def feedback_page() -> rx.Component:
    return rx.box(
        display.tabs(
            active_key=FeedbackBaseState.active_key,
            default_active_key='alert',
            items=helper.contain([
                display.tab_item(key='alert', label='alert', children=antd_feedback_alert()),
                display.tab_item(key='drawer', label='drawer', children=antd_feedback_drawer()),
                display.tab_item(key='message', label='message', children=antd_feedback_message()),
                display.tab_item(key='modal', label='modal', children=antd_feedback_modal()),
                display.tab_item(key='notification', label='notification', children=antd_feedback_notification()),
            ]),
            on_change=FeedbackBaseState.set_active_key,
        ),
        id='abcde',
    )
