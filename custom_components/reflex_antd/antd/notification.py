from typing import Optional, Union, Dict, Any, List, Set

from reflex import Component, Var
from reflex.utils import imports
import uuid
from ..base import AntdComponent, ContainVar, JsValue, ReactNode, version
from ..constant import PlacementType, RoleType


class Notification(JsValue):
    btn: Optional[Var[ReactNode]]
    class_name: Optional[Var[str]]
    close_icon: Optional[Var[ReactNode]]
    description: Optional[Var[str]]
    duration: Optional[Var[int]]
    icon: Optional[Var[ReactNode]]
    key: Optional[Var[str]]
    message: Optional[Var[str]]
    placement: Optional[Var[PlacementType]]
    role: Optional[Var[RoleType]]
    props: Optional[Var[Union[dict, ContainVar]]]

    def get_imports(self) -> imports.ImportDict:
        _imports = {
            "antd": [imports.ImportVar(tag='notification')],
        }
        return _imports

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        open_func = """
        const %(name)s = () => {
          notification.open({
            message: '%(message)s',
            description:'%(description)s',
            placement:'%(placement)s',
            duration:'%(duration)s',
          });
        };
        """ % dict(name=self.get_open_notification(), message=self.message, description=self.description,
                   placement=self.placement, duration=self.duration)

        _hooks = []
        _hooks.extend([
            """const [api, contextHolder] = notification.useNotification();""",
            open_func,
        ])
        if version <= '000.004.006':
            return set(_hooks)
        return dict((h, None) for h in _hooks)

    @property
    def uid(self) -> str:
        try:
            return self._uid
        except AttributeError:
            self._uid = uuid.uuid4().hex
            return self._uid

    def get_open_notification(self) -> str:
        return f'openNotification_{self.uid}'

    def serialize(self) -> str:
        return self.get_open_notification()


notification = Notification
