from typing import Optional, Union, Dict, Any, List, Set, Iterator
import uuid

from reflex import Component, Var
from reflex.utils import imports
from reflex.components.base.bare import Bare
from reflex.vars import BaseVar

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, version
from ..constant import MessageType


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
            others.extend([
                *self.config_item.get_hooks(),
                """useEffect(() => {
    if (%(state)s === null) {messageApi.destroy(); return;}
    %(name)s(%(state)s);
}, [%(state)s]); """ % dict(
                    state=self.config_item.serialize(),
                    name=self.get_open_message(),
                ),
            ])

        _hooks = []
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


message = Message
message_holder = MessageHolder.create

# def message_holder():
#     return Var.create_safe('{contextHolder}')
