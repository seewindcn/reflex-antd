from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List, Set, Iterator
import uuid
from reflex import Component, Var
from reflex.utils import imports
from reflex.components.base.bare import Bare
from reflex.vars import BaseVar
from ..base import AntdComponent, ContainVar, JsValue, ReactNode, ExStateItem, version
from ..constant import MessageType
from . import helper

class Message(JsValue):
    is_global: bool
    class_name: Optional[Var[str]]
    content: Optional[Var[ReactNode]]
    duration: Optional[Var[Union[int, float]]]
    icon: Optional[Var[ReactNode]]
    key: Optional[Var[Union[str, int]]]
    style: Optional[Var[dict]]
    type: Optional[MessageType]
    config: Optional[Var[dict]]
    top: Optional[Var[int]]
    rtl: Optional[Var[bool]]
    prefix_cls: Optional[Var[str]]
    max_count: Optional[Var[int]]

    @property
    def config_item(self) -> Optional[ExStateItem]:
        ...

    @property
    def uid(self) -> str:
        ...

    def get_open_message(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def serialize(self) -> str:
        ...

class MessageHolder(Bare):

    @overload
    @classmethod
    def create(cls, *children, msg: Optional[Message]=None, contents: Optional[Union[Var[str], str]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'MessageHolder':
        """"""
        ...
message = Message
message_holder = MessageHolder.create