from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Type, Any, Tuple, Dict, List, Iterable, Callable, Set, Union, Optional, Self
import sys
from os import path
from abc import ABC, abstractmethod
from functools import lru_cache, wraps
from hashlib import md5
import uuid
import dataclasses
import inspect
import re
import reflex as rx
from reflex import Component, Var, State, Base, ImportVar
from reflex.base import pydantic_main as pydantic_md
from reflex.components.component import BaseComponent, CustomComponent, StatefulComponent, ComponentStyle
from reflex.components.base.bare import Bare
from reflex.components.core import Foreach, Match
from reflex.constants import Hooks, Reflex, MemoizationDisposition, MemoizationMode
from reflex.utils import imports, format, serializers, exceptions
from reflex.vars import BaseVar, VarData
from reflex.event import EventHandler, EventSpec, EventChain
from .constant import SizeType
from .util import OrderedSet
pydantic = pydantic_md
version = '.'.join(map(lambda x: x.zfill(3), Reflex.VERSION.split('.')))
my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, '.templates')
APP_ROUTER = False
RE_KEY_IDX = re.compile('\\.\\d+\\.')
memo_never = MemoizationMode().set(disposition=MemoizationDisposition.NEVER)
memo_never_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.NEVER, recursive=False)
memo_always = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS)
memo_always_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS, recursive=False)

def stateful(hd: Callable[..., Component]=None, forced=True) -> Callable:
    ...

def pretty_dumps(value: Any, indent=2) -> str:
    ...

def get_component_all_imports(com: Component) -> imports.ImportDict:
    ...

def get_component_hooks(com) -> Dict[str, None]:
    ...

def get_component_custom_code(com: Component) -> Set[str]:
    ...

class ExItem(ABC):

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    @abstractmethod
    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_state(self) -> str:
        ...

    def get_hooks(self) -> Dict[str, None]:
        ...

    def get_interpolations(self) -> List[Tuple[int, int]]:
        ...

    def get_var_data(self) -> VarData:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

    def get_custom_code(self) -> set[str]:
        ...

class ExComponentItemBase(ExItem):
    item: Component

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

    def get_custom_code(self) -> set[str]:
        ...

class ExComponentItem(ExComponentItemBase):
    item: Component

class ExStatefulComponentItem(ExComponentItemBase):
    item: StatefulComponent

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

class JsEvent:
    hd: EventHandler
    event_trigger: Callable

    def get_state_full_name(self) -> str:
        ...

    def get_event_args(self) -> str:
        ...

    def get_ex_item(self, parent, key) -> ExItem:
        ...

    def to_hook_code(self, name: str) -> str:
        ...
js_event = JsEvent

class ExEventHandlerItem(ExItem):
    item: JsEvent

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    @property
    def hd_item(self) -> 'ExLambdaHandlerItem':
        ...

    def serialize(self) -> str:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

class ExLambdaHandlerItem(ExItem):
    item: Callable
    event_trigger: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Dict[str, None]:
        ...

class ExCallableItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

class ExStateItem(ExItem):
    item: BaseVar

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_state(self) -> str:
        ...

class FakeComponentMixin:

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

class JsValue:
    value: Callable | str | Component
    to_js: bool

    @property
    def to_react(self) -> bool:
        ...

    def get_ex_item(self, parent, key) -> ExItem:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_state(self) -> str:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_var_data(self) -> VarData:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

    def to_hook_code(self, name: str) -> str:
        ...

class JsFunctionValue(JsValue):

    @property
    def args(self):
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

    def to_hook_code(self, name: str) -> str:
        ...

def js_value(value: Union[str, Callable, Foreach, Match], **kwargs) -> JsValue:
    ...

class ExJsItem(ExItem):
    item: JsValue

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

class ExVarItem(ExItem):
    item: Var

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        ...

    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_state(self) -> str:
        ...

    def get_interpolations(self) -> List[Tuple[int, int]]:
        ...

class ExFormatter:
    items: List[Type[ExItem]]

    def get_ex_item(self, key: str) -> ExItem | None:
        ...

    def get_value(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def get_state(self) -> str:
        ...

    def get_hooks(self) -> Dict[str, None]:
        ...

    def get_interpolations(self) -> List[Tuple[int, int]]:
        ...

    def get_var_data(self) -> VarData:
        ...

class ExVar(BaseVar):

    @classmethod
    def create(cls, value: Any, _var_is_local: bool=True, _var_is_string: bool=False, _var_data: VarData | None=None) -> Var | None:
        ...

class CasualVar(ExVar):

    def to_js(self) -> Self:
        ...

    def to_react(self) -> Self:
        ...

    def to_event(self) -> Self:
        ...
casual_var = CasualVar.create

class NodeVar(ExVar):
    pass

class ContainVar(ExVar):

    @classmethod
    def create(cls, _args_: Any=None, **kwargs) -> Self:
        ...

    def init(self, parent: Component, name: str) -> Self:
        ...

    def get_custom_components(self) -> set[CustomComponent]:
        ...

    def get_custom_code(self) -> Set[str]:
        ...

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        ...

    def get_imports(self) -> imports.ImportDict:
        ...

    def to_hook_code(self) -> Dict[str | Var, None]:
        ...
contain = ContainVar.create

def container(data: Union[list, dict, JsValue], name: str='') -> rx.Component:
    ...

class VarDataMixin:
    ...

class DataClassMixin:

    def to_component(self) -> Component:
        ...

class AntdBaseComponent(Component):

    def add_imports(self) -> dict[str, str | ImportVar | list[str | ImportVar]]:
        ...

    def add_hooks(self) -> list[str | Var]:
        ...

    @overload
    @classmethod
    def create(cls, *children, _custom_components: Optional[Set[CustomComponent]]=None, _ex_hooks: Optional[List[ContainVar]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'AntdBaseComponent':
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class AntdComponent(AntdBaseComponent):

    @overload
    @classmethod
    def create(cls, *children, _custom_components: Optional[Set[CustomComponent]]=None, _ex_hooks: Optional[List[ContainVar]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'AntdComponent':
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class AntdSubComponent(AntdBaseComponent, Component):

    @overload
    @classmethod
    def create(cls, *children, base_tag: Optional[str]=None, _custom_components: Optional[Set[CustomComponent]]=None, _ex_hooks: Optional[List[ContainVar]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'AntdSubComponent':
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

def default_config(provider: Component):
    ...

def patch_all():
    ...
ReactNode = Union[str, Component]
JsNode = Union[JsValue, JsEvent]