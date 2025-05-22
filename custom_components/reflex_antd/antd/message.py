from typing import Optional, Union, Dict, Any, List, Set, Iterator

from reflex import Component, Var, vars
from reflex.utils import imports, format
from reflex.components.component import ComponentNamespace
from reflex.components.base.bare import Bare
from reflex.event import EventSpec, call_script

from ..base import (
    AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, version, compose_react_imports,
    get_unique_variable_name,
)
from ..constant import MessageType
from . import helper

_ref = Var(_js_expr="refs['__antd_message']")


class Message(JsValue):
    is_global: bool = True
    class_name: Optional[Var[str | list]]
    content: Optional[Var[ReactNode]]
    duration: Optional[Var[Union[int, float]]]
    icon: Optional[Var[ReactNode]]
    key: Optional[Var[Union[str, int]]]
    style: Optional[Var[dict]]
    type: Optional[MessageType] = 'info'
    config: Optional[Var[dict]]

    top: Optional[Var[int]]
    rtl: Optional[Var[bool]]
    prefix_cls: Optional[Var[str]]
    max_count: Optional[Var[int]]

    @property
    def config_item(self) -> Optional[ExStateItem]:
        if not hasattr(self, 'config') or self.config is None:
            return None
        try:
            return self._config_item
        except AttributeError:
            self._config_item = ExStateItem(self.config, self)
            return self._config_item

    @property
    def uid(self) -> str:
        try:
            return self._uid
        except AttributeError:
            self._uid = get_unique_variable_name()
            return self._uid

    def get_open_message(self) -> str:
        return f'openMessage_{self.uid}'

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='App'), imports.ImportVar(tag='message', alias='message_md')],
            "react": compose_react_imports(['useEffect']),
            "/utils/state": [imports.ImportVar(tag="refs")],
        }
        return _imports

    def get_hooks(self) -> Set[str] | Dict[str, None]:

        if self.config_item is not None:
            open_func = """
            const %(name)s = () => {
                %(mn)s.open(%(cfg)s);
            };""" % dict(
                name=self.get_open_message(),
                mn='messageApi' if not self.is_global else 'message',
                cfg=self.config_item.serialize(),
            )
        else:
            key_s = f'{self.key},' if hasattr(self, 'key') else ''
            duration_s = f'duration: {self.duration},' if hasattr(self, 'duration') else ''
            top_s = f'top: {self.top},' if hasattr(self, 'top') else ''

            open_func = """
            const %(name)s = () => {
                %(mn)s.open({
                  %(key)s
                  type: '%(type)s',
                  content: '%(content)s',
                  %(duration)s %(top)s
                });
            };
            """ % dict(
                name=self.get_open_message(),
                mn='messageApi' if not self.is_global else 'message',
                key=key_s, type=self.type, content=self.content,
                duration=duration_s,
                top=top_s,
            )
        others = []
        if self.config_item:
            state = self.config_item.serialize()
            others.extend([
                *self.config_item.get_hooks(),
                helper.hook_state(
                    state_field=state,
                    on_update='%(name)s(%(state)s)' % dict(name=self.get_open_message(), state=state),
                    on_null='messageApi.destroy()',
                ),
            ])

        _hooks = [
            'const { message } = App.useApp();',
            str(f"{str(_ref)} = message"),
        ]
        if self.is_global:
            _hooks.extend([
                open_func
            ])
        else:
            _hooks.extend([
                """const [messageApi, contextHolder] = message_md.useMessage();""",
                open_func,
                *others,
            ])
        if version <= '000.004.006':
            return set(_hooks)
        return dict((h, None) for h in _hooks)

    def serialize(self) -> str:
        # if self.config_item is not None:
        #     return '{contextHolder}'
        return self.get_open_message()


class MessageHolder(Bare):
    """
    Message.hook:
        const [messageApi, contextHolder] = message.useMessage();

    MessageHolder:
        <>
            {contextHolder}
        </>
     """
    msg: Optional[Message]

    @classmethod
    def create(cls, msg: Message) -> Component:
        cs = ['<>']
        if not msg.is_global:
            cs.append('{contextHolder}')
        cs.append('</>')
        data = '\n'.join(cs)
        rs = cls(
            msg=msg,
            contents=Var(
                _js_expr=data,
                _var_type=str,
            ),
        )
        return rs

    def _get_vars(self, **kwargs) -> Iterator[Var]:
        yield self.contents
        yield Var(
            _js_expr='',
            _var_data=self.msg.get_var_data(),
        )


class Messages(ComponentNamespace):
    @staticmethod
    def send(content: ReactNode, type: str | None = None, **props) -> EventSpec:
        """Send a message. """
        if type is None:
            type = 'info'
        cmd = f"{str(_ref)}.{type}"
        config = dict(
            content=content,
            **props
        )

        send_cmd = f"{cmd}({format.json_dumps(config)})"
        send_action = Var(_js_expr=send_cmd)
        return call_script(send_action)  # type: ignore

    @staticmethod
    def info(content: ReactNode, **kwargs):
        return Messages.send(content, type="info", **kwargs)

    @staticmethod
    def warning(content: ReactNode, **kwargs):
        return Messages.send(content, type="warning", **kwargs)

    @staticmethod
    def error(content: ReactNode, **kwargs):
        return Messages.send(content, type="error", **kwargs)

    @staticmethod
    def success(content: ReactNode, **kwargs):
        return Messages.send(content, type="success", **kwargs)

    @staticmethod
    def loading(content: ReactNode, **kwargs):
        return Messages.send(content, type="loading", **kwargs)


message = Message
message_holder = MessageHolder.create
messages = Messages()

# def message_holder():
#     return Var.create_safe('{contextHolder}')
