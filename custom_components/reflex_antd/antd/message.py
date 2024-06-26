from typing import Optional, Union, Dict, Any, List, Set, Iterator
import uuid

from reflex import Component, Var
from reflex.utils import imports
from reflex.components.component import ComponentNamespace
from reflex.components.base.bare import Bare
from reflex.vars import BaseVar
from reflex.event import EventSpec, call_script
from reflex.utils.serializers import serialize

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, version
from ..constant import MessageType
from . import helper

_ref = Var.create_safe("refs['__antd_message']", _var_is_string=False)


class Message(JsValue):
    is_global: bool = True
    class_name: Optional[Var[str]]
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
            self._uid = uuid.uuid4().hex
            return self._uid

    def get_open_message(self) -> str:
        return f'openMessage_{self.uid}'

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='message')],
            "react": [imports.ImportVar(tag="useEffect")],
            "/utils/state": [imports.ImportVar(tag="refs")],
        }
        return _imports

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        if self.config_item is not None:
            open_func = """const %(name)s = () => {
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
            str(f"{_ref} = message"),
        ]
        if self.is_global:
            _hooks.extend([
                open_func
            ])
        else:
            _hooks.extend([
                """const [messageApi, contextHolder] = message.useMessage();""",
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
        return cls(
            msg=msg,
            contents='\n'.join(cs),
        )

    def _get_vars(self, include_children: bool = False) -> Iterator[Var]:
        yield self.contents
        yield BaseVar(
            _var_name='',
            _var_is_local=True,
            _var_data=self.msg.get_var_data(),
        )


class Messages(ComponentNamespace):
    @staticmethod
    def send(content: ReactNode, type: str | None = None, **props) -> EventSpec:
        """Send a message. """
        if type is None:
            type = 'info'
        cmd = f"{_ref}.{type}"
        config = dict(
            content=content,
            **props
        )

        send_cmd = f"{cmd}({serialize(config)})"
        send_action = Var.create(send_cmd, _var_is_string=False, _var_is_local=True)
        return call_script(send_action)  # type: ignore

    @staticmethod
    def info(content: ReactNode, **kwargs):
        return MessageHolder.send(message, type="info", **kwargs)

    @staticmethod
    def warning(content: ReactNode, **kwargs):
        return MessageHolder.send(message, type="warning", **kwargs)

    @staticmethod
    def error(content: ReactNode, **kwargs):
        return MessageHolder.send(message, type="error", **kwargs)

    @staticmethod
    def success(content: ReactNode, **kwargs):
        return MessageHolder.send(message, type="success", **kwargs)

    @staticmethod
    def loading(content: ReactNode, **kwargs):
        return MessageHolder.send(message, type="success", **kwargs)


message = Message
message_holder = MessageHolder.create
messages = Messages()

# def message_holder():
#     return Var.create_safe('{contextHolder}')
