from typing import Optional, Union, Dict, Any, List, Set

from reflex import Component, Var
from reflex.utils import imports

from ..base import (
    AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, FakeComponentMixin, memo_never_no_recursive,
    get_unique_variable_name,
)
from ..constant import TypeType

from . import helper


class Modal(AntdComponent):
    tag = 'Modal'

    class_names: Var[ContainVar]
    styles: Var[ContainVar]
    cancel_button_props: Var[ContainVar]
    cancel_text: Var[ReactNode]
    centered: Var[bool]
    close_icon: Var[Union[ReactNode, bool]]
    confirm_loading: Var[bool]
    destroy_on_close: Var[bool]
    focus_trigger_after_close: Var[bool]
    footer: Var[ContainVar]
    force_render: Var[bool]
    get_container: Var[Union[bool, ContainVar]]
    keyboard: Var[bool]
    mask: Var[bool]
    closable: Var[bool]
    mask_closable: Var[bool]
    modal_render: Var[ReactNode]
    ok_button_props: Var[ContainVar]
    ok_text: Var[ReactNode]
    ok_type: Var[TypeType]
    title: Var[ReactNode]
    open: Var[bool]
    width: Var[Union[str, int]]
    wrapClassName: Var[str]
    z_index: Var[int]

    _memoization_mode = memo_never_no_recursive

    def _get_hooks(self) -> str | None:
        _hooks = []
        # if self.open is not None and 'on_open' in self.event_triggers:
        #     _hooks.append(helper.hook_state(
        #         state_field=self.open,
        #         on_update=f'{str(self.event_triggers["on_open"])}()',
        #     ))
        return '\n'.join(_hooks) if _hooks else None

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "after_close": lambda: [],
            "on_cancel": lambda e: [],
            "on_ok": lambda e: [],
            "after_open_change": lambda open: [open],
        })
        return _triggers


class Confirm(FakeComponentMixin, JsValue):
    """ confirm模式, 使用 useContext(EventLoopContext); 会报错, """
    config: Var[dict]
    # sample: before_open=helper.js_value(f""" {form_id}.setFieldsValue({str(ws.form_params).strip('{}')}) """)
    before_open: JsValue = None

    @property
    def config_item(self) -> Optional[ExStateItem]:
        if not hasattr(self, 'config') or self.config is None:
            return None
        try:
            return self._config_item
        except AttributeError:
            if isinstance(self.config, Var):
                self._config_item = ExStateItem(self.config, self)
            else:
                self._config_item = ContainVar.create(self.config).init(self, 'config')
            return self._config_item

    @property
    def uid(self) -> str:
        try:
            return self._uid
        except AttributeError:
            self._uid = get_unique_variable_name()
            return self._uid

    def get_name(self) -> str:
        return f'confirm_{self.uid}'

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='App')],
        }
        return imports.merge_imports(
            _imports,
            self.config_item.get_imports(),
        )

    def get_hooks(self) -> Dict[str, None]:
        before_open = self.before_open
        # if isinstance(self.config_item, ContainVar):
        #     before_open = self.config_item._var_fmt.get_ex_item('config.before_open')
        s_before_open = before_open.serialize() \
            if before_open is not None else ''
        confirm_func = """
        const %(name)s = () => {
            %(s_before_open)s
            modal.confirm(%(cfg)s);
        };""" % dict(
            name=self.get_name(),
            s_before_open=s_before_open,
            cfg=self.config_item.serialize() if hasattr(self.config_item, 'serialize') else str(self.config_item),
        )
        return {
            **self.config_item.get_hooks(),
            'const { modal } = App.useApp();': None,
            confirm_func: None,
        }

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = {}
        _triggers.update({
            "config.after_close": lambda: [],
            "config.on_cancel": lambda e: [],
            "config.on_ok": lambda e: [],
            "config.before_open": lambda e: [],
            # not support: "config.after_open_change": lambda open: [open],
        })
        return _triggers

    def serialize(self) -> str:
        return self.get_name()


modal = Modal.create
confirm = Confirm
