from typing import Optional, Union, Dict, Any, List, Set, Iterator

from reflex import Component, Var, vars
from reflex.utils import imports, format
from reflex.components.component import ComponentNamespace
from reflex.components.base.bare import Bare
from reflex.event import EventSpec, call_script

from ..base import AntdComponent, ContainVar, JsValue, ReactNode, version, get_unique_variable_name
from ..constant import PlacementType, RoleType


_ref = Var(_js_expr="refs['__antd_notification']", )


class Notification(JsValue):
    is_global: bool = False
    btn: Var[ReactNode]
    class_name: Var[str | list]
    close_icon: Var[ReactNode]
    description: Var[str]
    duration: Var[int]
    icon: Var[ReactNode]
    key: Var[str]
    message: Var[str]
    placement: Var[PlacementType]
    role: Var[RoleType]
    props: Var[Union[dict, ContainVar]]

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='App'), imports.ImportVar(tag='notification', alias='notification_md')],
        }
        return _imports

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        if not self.is_global:
            open_func = """
            const %(name)s = () => {
              %(mn)s.open({
                message: '%(message)s',
                description:'%(description)s',
                placement:'%(placement)s',
                duration:'%(duration)s',
              });
            };
            """ % dict(
                name=self.get_open_notification(),
                mn='notificationApi' if not self.is_global else 'notification',
                message=self.message, description=self.description,
                placement=self.placement, duration=self.duration)

        _hooks = [
            'const { notification } = App.useApp();',
            str(f"{str(_ref)} = notification"),
        ]
        if not self.is_global:
            _hooks.extend([
                """const [notificationApi, contextHolder] = notification_md.useNotification();""",
                open_func,
            ])
        return dict((h, None) for h in _hooks)

    @property
    def uid(self) -> str:
        try:
            return self._uid
        except AttributeError:
            self._uid = get_unique_variable_name()
            return self._uid

    def get_open_notification(self) -> str:
        return f'openNotification_{self.uid}'

    def serialize(self) -> str:
        return self.get_open_notification() if not self.is_global else ''


class NotificationHolder(Bare):
    """
    Notification.hook:
        const [api, contextHolder] = notification.useNotification();

    NotificationHolder:
        <>
            {contextHolder}
        </>
     """
    noti: Optional[Notification]

    @classmethod
    def create(cls, noti: Notification) -> Component:
        cs = ['<>']
        if not noti.is_global:
            cs.append('{contextHolder}')
        cs.append('</>')
        data = '\n'.join(cs)
        rs = cls(
            noti=noti,
            contents=Var(
                _js_expr=data,
                _var_type=str,
            ),
        )
        rs.contents = data
        return rs

    def _get_vars(self, **kwargs) -> Iterator[Var]:
        yield self.contents
        yield Var(
            _js_expr='',
            _var_data=self.noti.get_var_data(),
        )


class Notifications(ComponentNamespace):
    @staticmethod
    def send(
            title: ReactNode, content: ReactNode, type: str | None = None,
            # onClick: Callable = None,
            # on_close: Callable = None,
            **props) -> EventSpec:
        """Send a message. """
        if type is None:
            type = 'open'
        cmd = f"{str(_ref)}.{type}"
        config = dict(
            message=title,
            description=content,
            **props
        )

        send_cmd = f"{cmd}({format.json_dumps(config)})"
        send_action = Var(_js_expr=send_cmd)
        return call_script(send_action)  # type: ignore

    @staticmethod
    def info(title: ReactNode, content: ReactNode, **kwargs):
        return Notifications.send(title, content, type="info", **kwargs)


notification = Notification
notification_holder = NotificationHolder.create
notifications = Notifications()
