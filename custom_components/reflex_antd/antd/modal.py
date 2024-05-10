from typing import Optional, Union, Dict, Any, List, Set
import uuid

from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, FakeComponentMixin
from ..constant import TypeType

from . import helper


class Modal(AntdComponent):
    tag = 'Modal'

    class_names: Optional[Var[ContainVar]]
    styles: Optional[Var[ContainVar]]
    cancel_button_props: Optional[Var[ContainVar]]
    cancel_text: Optional[Var[ReactNode]]
    centered: Optional[Var[bool]]
    close_icon: Optional[Var[Union[ReactNode, bool]]]
    confirm_loading: Optional[Var[bool]]
    destroy_on_close: Optional[Var[bool]]
    focus_trigger_after_close: Optional[Var[bool]]
    footer: Optional[Var[ContainVar]]
    force_render: Optional[Var[bool]]
    get_container: Optional[Var[Union[bool, ContainVar]]]
    keyboard: Optional[Var[bool]]
    mask: Optional[Var[bool]]
    mask_closable: Optional[Var[bool]]
    modal_render: Optional[Var[ReactNode]]
    ok_button_props: Optional[Var[ContainVar]]
    ok_text: Optional[Var[ReactNode]]
    ok_type: Optional[Var[TypeType]]
    title: Optional[Var[ReactNode]]
    open: Optional[Var[bool]]
    width: Optional[Var[Union[str, int]]]
    wrapClassName: Optional[Var[str]]
    zIndex: Optional[Var[int]]

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
    config: Optional[Var[dict]]

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
            self._uid = uuid.uuid4().hex
            return self._uid

    def get_name(self) -> str:
        return f'confirm_{self.uid}'

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='Modal')],
        }
        return imports.merge_imports(
            _imports,
            self.config_item.get_imports(),
        )

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        before_open = None
        if isinstance(self.config_item, ContainVar):
            before_open = self.config_item._var_fmt.get_ex_item('config.before_open')
        call_before_open = f'({before_open.serialize()})();' \
            if before_open is not None else ''
        confirm_func = """const %(name)s = () => {
                                %(call_before_open)s
                               Modal.confirm(%(cfg)s);
                               };""" % dict(
            name=self.get_name(),
            call_before_open=call_before_open,
            cfg=self.config_item.serialize() if hasattr(self.config_item, 'serialize') else str(self.config_item),
        )
        return {
            **self.config_item.get_hooks(),
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
