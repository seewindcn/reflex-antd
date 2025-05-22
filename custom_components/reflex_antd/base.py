from typing import Type, Any, Tuple, Dict, List, Iterable, Callable, Set, Union, Optional, Self, cast
import functools
import logging
import os
import types
import sys
from os import path
from abc import ABC, abstractmethod
from functools import lru_cache, wraps
from hashlib import md5
import dataclasses
import inspect
import re
import json

import pydantic as pydantic2_md
import reflex as rx
from reflex import Component, Var, State, Base, ImportVar, NoSSRComponent
from reflex.vars import StringVar, base as vars_base
from reflex.base import pydantic_main as pydantic_md, BaseModel  # noqa

from reflex.components.component import (
    BaseComponent, CustomComponent, StatefulComponent, ComponentStyle, render_dict_to_var,
)
from reflex.components.base.bare import Bare
from reflex.components.core import Foreach, Match, Cond
from reflex.components.tags import Tag
from reflex.constants import Hooks, Reflex, MemoizationDisposition, MemoizationMode
from reflex.utils import imports, format, serializers, exceptions
from reflex.vars import Var, VarData
from reflex.vars.base import get_unique_variable_name, var_operation_return
from reflex.event import EventHandler, EventSpec, EventChain
from reflex.experimental import hooks

from . import util, constant

pydantic = pydantic_md
# 0.4.6 -> 000.004.006
version = '.'.join(map(lambda x: x.zfill(3), Reflex.VERSION.split('.')))

my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, 'templates')

APP_ROUTER = True
RE_KEY_IDX = re.compile(r'\.\d+\.')

memo_never = MemoizationMode().set(disposition=MemoizationDisposition.NEVER)
memo_never_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.NEVER, recursive=False)
memo_always = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS)
memo_always_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS, recursive=False)

use_pretty_dumps = True
default_to_js = False
is_dynamic = False


def wrap_use_pretty_dumps(func):
    @wraps(func)
    def _wrap(*args, **kwargs):
        rs: str = func(*args, **kwargs)
        return rs if use_pretty_dumps else rs.replace('\n', '')
    return _wrap


class MyStatefulComponent(StatefulComponent):
    _valid_parents: List[str] = []  # hack: support use in rx.match


def stateless(hd: Callable[..., Component] = None, memo=memo_never_no_recursive) -> Callable:
    def _my(_hd: Callable[..., Component]) -> Callable:
        @wraps(_hd)
        def _wrap(*args, **kwargs):
            _com = _hd(*args, **kwargs)
            _com._memoization_mode = memo
            return _com

        return _wrap

    if hd is None:
        return _my
    else:
        return _my(hd)


def stateful(hd: Callable[..., Component] = None, forced=True, memo=memo_always) -> Callable:
    """ render a component into a function """

    def _my(_hd: Callable[..., Component]) -> Callable:
        @wraps(_hd)
        def _wrap(*args, **kwargs):
            _com = _hd(*args, **kwargs)
            if forced:
                _com._memoization_mode = memo
                # _com._memoization_mode.recursive = False
            _sc = MyStatefulComponent.create(_com)
            return _sc if _sc is not None else _com
            # return _com

        return _wrap

    if hd is None:
        return _my
    else:
        return _my(hd)


STR_TYPES = (str, list, dict)


def to_str(v: str | list | dict | Any) -> Any:
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        _v = dict([(k, to_str(_v)) for k, _v in v.items()])
        return _v
    if isinstance(v, list):
        _v = [to_str(i) for i in v]
        return _v
    return str(v)


def compose_react_imports(tags: list[str]):
    return {"react": [ImportVar(tag=tag, install=tag in ['useEffect', 'useState']) for tag in tags]}


def get_component_all_imports(com: Component | Var) -> imports.ImportDict:
    return {} if isinstance(com, STR_TYPES) or isinstance(com, Var) else com._get_all_imports()


def get_component_all_dynamic_imports(com: Component | Var) -> Set[str]:
    if hasattr(com, '_get_all_dynamic_imports') and callable(com._get_all_dynamic_imports):
        return com._get_all_dynamic_imports()
    return set()


def get_component_hooks(com) -> Dict[str, None]:
    return {} if isinstance(com, STR_TYPES) or isinstance(com, Var) \
        else (com._get_all_hooks() if version > '000.006.007' else com._get_all_hooks_internal() | com._get_all_hooks())


def get_component_custom_code(com: Component) -> Set[str]:
    return com._get_all_custom_code() if isinstance(com, BaseComponent) else set()


def get_custom_components(com: Any) -> set[CustomComponent]:
    if isinstance(com, CasualVar):
        return set()
    if isinstance(com, CustomComponent):
        return {com}
    if hasattr(com, 'get_custom_components') and callable(com.get_custom_components):
        return com.get_custom_components()
    if hasattr(com, '_get_all_custom_components') and callable(com._get_all_custom_components):
        return com._get_all_custom_components()
    return set()


def get_var_data(v: Var) -> VarData | None:
    if hasattr(v, '_get_all_var_data'):
        _data = v._get_all_var_data()
    elif hasattr(v, 'get_var_data'):
        _data = v.get_var_data()
    else:
        _data = None
    return _data


def get_var_data_hooks(v: Union[Var, VarData, "JsValue"]) -> dict[str, None]:
    if isinstance(v, JsValue):
        return v.get_hooks()
    _var_data = get_var_data(v) if isinstance(v, Var) else v
    return {hook: None for hook in _var_data.hooks} if _var_data else {}


class ExItem(ABC):
    @classmethod
    def isinstance(cls, item: Any) -> bool:
        pass

    def __init__(self, item: Any, parent: Component, key: str = ''):
        self.item = item
        self.key = key
        self.parent = parent

    @abstractmethod
    def serialize(self) -> str:
        ...

    def get_imports(self) -> imports.ImportDict:
        return {}

    def get_dynamic_imports(self) -> Set[str]:
        return set()

    def get_state(self) -> str:
        return ''

    def get_hooks(self) -> Dict[str, None]:
        return {}

    # def get_interpolations(self) -> List[Tuple[int, int]]:
    #     return []

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
            # interpolations=self.get_interpolations(),
        )

    def get_custom_components(self) -> set[CustomComponent]:
        return set()

    def get_custom_code(self) -> set[str]:
        return set()


class ExComponentItemBase(ExItem):
    item: Component

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Component)

    def serialize(self) -> str:
        return str(self.item)

    def get_imports(self) -> imports.ImportDict:
        return get_component_all_imports(self.item)

    def get_dynamic_imports(self) -> Set[str]:
        return get_component_all_dynamic_imports(self.item)

    def get_hooks(self) -> Dict[str, None]:
        return get_component_hooks(self.item)

    def get_custom_components(self) -> set[CustomComponent]:
        return get_custom_components(self.item)

    def get_custom_code(self) -> set[str]:
        rs = get_component_custom_code(self.item)
        if isinstance(self.item, StatefulComponent):
            rs.add(self.item.code)
        return rs


class ExComponentItem(ExComponentItemBase):
    item: Component


class ExStatefulComponentItem(ExComponentItemBase):
    item: StatefulComponent

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, StatefulComponent)

    def serialize(self) -> str:
        return f'<{self.item.tag}/>'


class JsEvent:
    """ can use like event value """
    hd: EventHandler
    # event_trigger use for custom trigger, must work with fmt=True
    event_trigger: Callable
    _item: "ExEventHandlerItem" = None

    def __init__(self, hd: Any, js: str = '', fmt: bool = False, event_trigger: Callable = None):
        """
        js样例:
            js='''(e) => {
                    let key= 1;
                    %(name)s(key);
            }''',
            fmt=True,
        """
        assert isinstance(hd, EventHandler)
        self.hd = hd
        self.js = js
        self.fmt = fmt
        self.event_trigger = event_trigger

    def get_state_full_name(self) -> str:
        name = str(self.hd.fn).split(' ')[1]
        _base = format.to_snake_case(name)
        return f'state.{_base}'

    def get_event_args(self) -> str:
        _args = inspect.getfullargspec(self.hd.fn)
        rs = []
        for idx, _arg in enumerate(_args.args):
            if idx == 0:  # ignore self
                continue
            rs.append(f'{_arg}:{self.args[idx - 1]}')
        return ','.join(rs)

    def get_ex_item(self, parent, key) -> ExItem:
        if self._item is not None:
            return self._item
        self._item = ExEventHandlerItem(self, parent, key=key)
        return self._item

    def to_hook_code(self, name: str) -> str:
        assert self._item is not None, 'JsEvent to_hook_code depend get_ex_item'
        code = self._item.serialize()
        return f'const {name} = {code}'


js_event = JsEvent


class ExEventHandlerItem(ExItem):
    item: JsEvent

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, JsEvent)

    @property
    def hd_item(self) -> 'ExLambdaHandlerItem':
        try:
            return self._hd_item
        except AttributeError:
            self._hd_item = ExLambdaHandlerItem(self.item.hd, self.parent, key=self.key)
            self._hd_item.event_trigger = self.item.event_trigger
            return self._hd_item

    def _get_fn_name(self) -> str:
        if 0:
            return (f"{self.key.replace('.', '_')}_{md5(f'{str(self.item.hd)}'.encode('utf-8')).hexdigest()}"
                    f"_{id(self)}")
        return f"{self.key.replace('.', '_')}_{md5(f'{str(self.item.hd)}'.encode('utf-8')).hexdigest()}"

    @wrap_use_pretty_dumps
    def serialize(self) -> str:
        hd_name = self.hd_item.serialize()
        trigger = self.hd_item._get_event_trigger()
        args = inspect.getfullargspec(trigger).args

        if not self.item.fmt:
            return f"""(({','.join(args)}) => {{
                {self.item.js}
                {hd_name}({','.join(args)})
            }})"""
        else:
            return self.item.js % dict(name=hd_name)

    def get_hooks(self) -> Dict[str, None]:
        return self.hd_item.get_hooks()

    def get_imports(self) -> imports.ImportDict:
        return self.hd_item.get_imports()


class ExLambdaHandlerItem(ExItem):
    item: Callable
    event_trigger: Callable = None

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        # return isinstance(item, Callable)
        return isinstance(item, Callable) and type(item) in (
            types.LambdaType, types.MethodType,
            EventHandler,
        )

    def _get_fn_name(self) -> str:
        if 0:
            return (f"{self.key.replace('.', '_')}_{md5(f'{str(self.item)}'.encode('utf-8')).hexdigest()}"
                    f"_{id(self)}")
        return f"{self.key.replace('.', '_')}_{md5(f'{str(self.item)}'.encode('utf-8')).hexdigest()}"

    def _get_event_trigger_key(self) -> str:
        return RE_KEY_IDX.sub('.*.', self.key)

    def _get_event_trigger(self) -> Callable:
        if self.event_trigger is not None:
            return self.event_trigger
        triggers = self.parent.get_event_triggers()
        rs = triggers.get(self._get_event_trigger_key(), lambda: [])
        return rs

    def serialize(self) -> str:
        return self._get_fn_name()

    def get_imports(self) -> imports.ImportDict:
        return {"react": [imports.ImportVar(tag="useCallback")]}

    def get_hooks(self) -> Dict[str, None]:
        key = self._get_event_trigger()
        chain = self.parent._create_event_chain(key, self.item)
        rendered_chain = format.format_prop(chain).strip("{}")
        _hook = f"""const {self._get_fn_name()} = useCallback({rendered_chain}, [addEvents, Event]);"""
        return {Hooks.EVENTS: None, _hook: None}


class ExCallableItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

    def serialize(self) -> str:
        return str(self.item())

    def get_imports(self) -> imports.ImportDict:
        return get_component_all_imports(self.item())

    def get_dynamic_imports(self) -> Set[str]:
        return get_component_all_dynamic_imports(self.item())

    def get_hooks(self) -> Dict[str, None]:
        return get_component_hooks(self.item())


class ExStateItem(ExItem):
    item: Var

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Var) and str(item).startswith("state__")

    def serialize(self) -> str:
        return str(self.item)

    def get_imports(self) -> imports.ImportDict:
        _var_data = get_var_data(self.item)
        return _var_data.old_school_imports() if _var_data else {}

    def get_hooks(self) -> Dict[str, None]:
        _var_data = get_var_data(self.item)
        return {hook: None for hook in _var_data.hooks} if _var_data else {}

    def get_state(self) -> str:
        _var_data = get_var_data(self.item)
        return _var_data.state if _var_data else ''


class FakeComponentMixin:
    def _create_event_chain(self, *args, **kwargs):
        return Component._create_event_chain(self, *args, **kwargs)

    def get_event_triggers(self) -> Dict[str, Any]:
        return {}

    def get_hooks(self) -> Dict[str, None]:
        return {}

    def get_imports(self) -> imports.ImportDict:
        return {}


class JsValue:
    """
    Component: support rx.foreach...,
      <Breadcrumb items={(state__global_state.subnav_items.map((i, index_de38f21f196b8746f2b4ca2b3fd6b46b) => (
        {
          "title": <RadixThemesLink asChild={true}>
              <NextLink href={i["href"]} passHref={true}>
              {i["title"]}
              </NextLink>
          </RadixThemesLink>
        }
          )))}
      />
    """
    value: Callable | str | Component
    to_js: bool = None
    custom_imports: imports.ImportDict = None
    dynamic_imports: Set[str] = None

    @property
    def to_react(self) -> bool:
        if self.to_js is None:
            return not default_to_js
        return not self.to_js

    def __init__(
            self, value: Union[str, List[str], Callable, Component] = None,
            custom_imports: imports.ImportDict = None,
            dynamic_imports: Set[str] = None,
            **kwargs):
        self.value = value
        self.custom_imports = custom_imports if custom_imports is not None else {}
        self.dynamic_imports = dynamic_imports if dynamic_imports is not None else set()
        if self.dynamic_imports:
            self.custom_imports.update(
                {"next/dynamic": [ImportVar(tag="dynamic", is_default=True)]}
            )
        self._init(**kwargs)

    def _init(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_ex_item(self, parent, key) -> ExItem:
        item = ExJsItem(self, parent, key=key)
        return item

    @wrap_use_pretty_dumps
    def serialize(self) -> str:
        if isinstance(self.value, str):
            code = self.value
        else:
            code = str(self.value)
            code = code[2:] if code.startswith('<>') else code
            code = code[:-3] if code.endswith('</>') else code
            code = code.strip('{}')
        return f"({code})" if self.to_js else f"{code}"

    def get_imports(self) -> imports.ImportDict:
        _imports = imports.merge_imports(
            get_component_all_imports(self.value),
            self.custom_imports
        )
        return _imports

    def get_dynamic_imports(self) -> Set[str]:
        return get_component_all_dynamic_imports(self.value) | self.dynamic_imports

    def get_state(self) -> str:
        return ''

    def get_hooks(self) -> Dict[str, None]:
        return get_component_hooks(self.value)

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
        )

    def get_custom_code(self) -> set[str]:
        rs = get_component_custom_code(self.value)
        return rs

    def get_custom_components(self) -> set[CustomComponent]:
        return get_custom_components(self.value)

    def to_hook_code(self, name: str) -> str:
        return self.serialize()


class JsFunctionValue(JsValue):
    _value: Union[str, "CasualVar", Component, JsValue]

    @property
    def args(self):
        args = [CasualVar.create_safe(arg, ) for arg in self._args.args]
        return args

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)
        self._args = inspect.getfullargspec(self.value)
        self._value = self.value(*self.args)

    @wrap_use_pretty_dumps
    def serialize(self) -> str:
        is_component = False
        if isinstance(self._value, str):
            v = self._value
        elif isinstance(self._value, Component):
            is_component = True
            v = str(self._value)
        else:
            v = to_str(self._value)
            # raise TypeError(self._value)
        sep_1, sep_2 = (('{', '}') if self.to_react else ('(', ')')) if not is_component else ('(', ')')
        return f"""(({','.join(self._args.args)}) => 
        {sep_1} {v} {sep_2} )"""

    def get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            get_component_all_imports(self._value),
            self.custom_imports,
        )

    def get_dynamic_imports(self) -> Set[str]:
        return get_component_all_dynamic_imports(self._value) | self.dynamic_imports

    def get_hooks(self) -> Dict[str, None]:
        return get_component_hooks(self._value)

    def get_custom_code(self) -> set[str]:
        return get_component_custom_code(self._value)

    def get_custom_components(self) -> set[CustomComponent]:
        return get_custom_components(self._value)

    def to_hook_code(self, name: str) -> str:
        """
        """
        code = self.serialize()  # .strip('()')
        code = f"const {name} = {code}"
        # code = f"const {name} = {code.replace('=>', ' ', 1)}"
        return code


def js_value(value: Union[str, Callable, Foreach, Match, Cond], **kwargs) -> JsValue:
    """ """
    if isinstance(value, (str, Component)):
        return JsValue(value, **kwargs)
    if isinstance(value, Callable):
        return JsFunctionValue(value, **kwargs)
    raise NotImplemented("Not implemented: %s(%s)" % (type(value), value))


class JsUseEffect(JsValue):
    value: rx.Var[dict]
    js: str
    dep_name: str = None

    def get_dep_name(self) -> str:
        if self.dep_name is not None:
            return self.dep_name
        return str(self.value)
        # state name
        # _var_data = get_var_data(self.value)
        # return format.format_state_name(_var_data.state) if _var_data else ''

    def __init__(
            self, value: rx.Var[dict],
            js: str,
            dep_name: str = None,
            **kwargs):
        """
        :param js:str
         """
        super().__init__(value, **kwargs)
        self.dep_name = dep_name
        self.js = js

    def serialize(self) -> str:
        return ''

    def _get_hooks(self, **kwargs) -> Dict[str, None]:
        return {
            """
useEffect(() => {
  if (! %(value)s) {
    return
  }
  %(js)s
}, [%(dep)s]);
            """ % kwargs: None,
        }

    def get_hooks(self) -> Dict[str, None]:
        kw = dict(
            value=str(self.value),
            dep=self.get_dep_name(),
            js=self.js,
        )
        _hooks = get_var_data_hooks(self.value)
        _my_hooks = self._get_hooks(**kw)
        _hooks.update(_my_hooks)
        return _hooks

    def get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            compose_react_imports(['useState', 'useEffect']),
            self.custom_imports,
        )


class JsLocalDictVar(JsUseEffect):
    """ custom local state's var by reflex state
    """
    name: str

    def __init__(
            self, name: str, value: dict | rx.Var,
            js: str,
            **kwargs):
        """
        :param js:str, sample:
            values['test_date'] = dayjs(values['test_date'])
         """
        super().__init__(value, js, **kwargs)
        self.name = name

    def serialize(self) -> str:
        return self.name

    def get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            compose_react_imports(['useState', 'useEffect']),
            self.custom_imports,
        )

    def _get_hooks(self, **kwargs) -> Dict[str, None]:
        kwargs['name'] = self.name
        return {
            "const[%(name)s, set%(name)s] = useState({})" % kwargs: None,
            """
useEffect(() => {
  if (! %(value)s) {
    return
  }
  var values = { ...%(value)s}
  %(js)s
  set%(name)s(values)
}, [%(dep)s]);
            """ % kwargs: None,
        }


class ExJsItem(ExItem):
    item: JsValue

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, JsValue)

    @wrap_use_pretty_dumps
    def serialize(self) -> str:
        return self.item.serialize()

    def get_imports(self) -> imports.ImportDict:
        return self.item.get_imports()

    def get_dynamic_imports(self) -> Set[str]:
        return self.item.get_dynamic_imports()

    def get_hooks(self) -> Dict[str, None]:
        return self.item.get_hooks()

    def get_custom_components(self) -> set[CustomComponent]:
        return self.item.get_custom_components()

    def get_custom_code(self) -> set[str]:
        return self.item.get_custom_code()


class ExVarItem(ExItem):
    item: Var

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Var)

    def __init__(self, item: Any, parent: Component, key: str = ''):
        if isinstance(item, ContainVar):  # nesting ContainVar
            item = item.init(parent, key)
        super().__init__(item, parent, key=key)

    def serialize(self) -> str:
        if isinstance(self.item, ContainVar):  # nesting ContainVar
            return str(self.item)
        return str(self.item).strip('{}')

    def get_imports(self) -> imports.ImportDict:
        _var_data = get_var_data(self.item)
        return _var_data.imports if _var_data else {}

    def get_hooks(self) -> Dict[str, None]:
        return get_var_data_hooks(self.item)

    def get_state(self) -> str:
        _var_data = get_var_data(self.item)
        return _var_data.state if _var_data else ""

    # def get_interpolations(self) -> List[Tuple[int, int]]:
    #     return self.item._var_data.interpolations if self.item._var_data else []


class ExFormatter:
    items: List[Type[ExItem]] = [
        ExVarItem,
        ExStatefulComponentItem,
        ExComponentItem,
        ExStateItem,
        ExJsItem,
        ExEventHandlerItem,
        ExLambdaHandlerItem,
        # ExCallableItem,
    ]

    def __init__(self, value: Any, parent: Component = None, name: str = ''):
        self.name = name
        self.value = value
        self.parent = parent
        self._coms: Dict[str, ExItem] = {}
        self._value: Any = None
        self._extract()

    def _extract(self):
        value = self.value
        self._coms.clear()

        def _op(_v: Any, key: str):
            if isinstance(_v, (list, tuple)):
                return _list(_v, pkey=key)
            elif isinstance(_v, PropBase):
                return _dict(_v.to_dict(), pkey=key)
            elif isinstance(_v, dict):
                return _dict(_v, pkey=key)
            elif isinstance(_v, (int, float, str, bool)):
                return _v

            _id = _v
            for ex in self.items:
                if ex.isinstance(_v):
                    _id = get_unique_variable_name()
                    self._coms[_id] = ex(_v, self.parent, key=key)
                    return _id

            if isinstance(_v, Base):
                _d = dict(_v._iter(exclude_unset=True, exclude_none=True, to_dict=False))
                return _dict(_d, pkey=key)
            elif dataclasses.is_dataclass(_v):
                _fields = dataclasses.fields(_v)
                _d = dict((_f.name, getattr(_v, _f.name)) for _f in _fields)
                # _d = dataclasses.asdict(_v)
                return _dict(_d, pkey=key)

            return _v

        def _list(_v: List, pkey: str) -> List[Any]:
            return [_op(i, key=f'{pkey}.{idx}') for idx, i in enumerate(_v)]

        def _dict(_v: Dict, pkey: str) -> Dict[str, Any]:
            return dict((format.to_camel_case(k), _op(v, key=f'{pkey}.{k}')) for k, v in _v.items() if v is not None)

        rs = _op(value, key=self.name)
        self._value = rs

    def iter_items(self) -> Iterable[Tuple[str, ExItem]]:
        for k, v in self._coms.items():
            yield k, v

    def get_ex_item(self, key: str) -> ExItem | None:
        for _, i in self.iter_items():
            if i.key == key:
                return i

    def get_value(self) -> str:
        v = util.pretty_dumps(self._value) if use_pretty_dumps else util.dumps(self._value)
        for k, ex in self.iter_items():
            v = v.replace(f'"{k}"', ex.serialize())
        return v

    def get_imports(self) -> imports.ImportDict:
        _imports = imports.merge_imports(
            *(c.get_imports() for _, c in self.iter_items()),
        )
        return _imports

    def get_state(self) -> str:
        for _, ex in self.iter_items():
            _state = ex.get_state()
            if _state != '':
                return _state
        return ''

    def get_hooks(self) -> Dict[str, None]:
        hooks = {}
        for _, ex in self.iter_items():
            _hooks = ex.get_hooks()
            hooks.update(_hooks)
        return hooks

    # def get_interpolations(self) -> List[Tuple[int, int]]:
    #     rs = []
    #     for _, ex in self._coms.items():
    #         rs += ex.get_interpolations()
    #     return rs

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
            # interpolations=self.get_interpolations(),
        )


class ExVar(Var):
    _var_value: Any = dataclasses.field()

    def __init__(self, *args, _var_value=None, **kwargs):
        self._var_value = _var_value
        super().__init__(*args, **kwargs)

    @classmethod
    def create(
            cls, value: Any, _var_is_local: bool = True, _var_is_string: bool = False,
            _var_data: VarData | None = None,
    ) -> Var | None:
        v = Var.create(value, _var_is_local=_var_is_local, _var_is_string=_var_is_string, _var_data=_var_data)
        return cls(
            _js_expr=v._js_expr,
            _var_type=v._var_type,
            _var_is_local=v._var_is_local,
            _var_is_string=v._var_is_string,
            _var_data=v._var_data,
        )


class CasualVar(StringVar):
    @classmethod
    def create(
            cls,
            value: Any,
            _var_is_local: bool | None = None,
            _var_is_string: bool | None = None,
            _var_data: VarData | None = None,
            _var_type: type = str,
    ) -> Var:
        if isinstance(value, Var):
            _var_type = value._var_type
            _var_data = get_var_data(value)
            value = str(value)
        return cls(value, _var_data=_var_data, _var_type=_var_type)

    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except (AttributeError,):
            if name.startswith("_"):
                raise
            return self.create_safe(
                f'{self._js_expr}.{name}',
            )

    def __getitem__(self, i: Any) -> Var:
        return self.create_safe(
            f'{self._js_expr}["{i}"]',
        )
        # try:
        #     return super().__getitem__(i)
        # except (exceptions.VarTypeError,):
        #     if str(i).startswith("_"):
        #         raise
        #     return self.create_safe(
        #         f'{self._js_expr}["{i}"]',
        #     )

    def to_js(self) -> Self:
        return self._replace(
            _var_type=str,
            _js_expr=f'({self._js_expr})'
        )

    def to_raw(self) -> str:
        return self._js_expr

    def to_react(self) -> Self:
        return self._replace(
            _var_type=str,
            _js_expr=f'{self._js_expr}'
        )

    def to_event(self) -> Self:
        return self._replace(
            _var_type=EventChain,
            _js_expr=f'({self._js_expr})'
        )

    def array_filter(self, filter_op: str | Callable[[Self], Self]):
        if callable(filter_op):
            filter_op = filter_op(casual_var('item'))
        rs = var_operation_return(
            js_expression=f"{self}.filter(item => {filter_op})",
            var_type=list,
        )
        return rs

    to_type = Var.to


casual_var = CasualVar.create


class CasualDict(dict):
    def __missing__(self, key):
        return None


class NodeVar(ExVar):
    """
    support:
        . base types: int, float, bool, str
        . js, like: {show ? 11 : 0}
     """
    pass


class ContainVar(ExVar):
    _var_fmt: ExFormatter

    def __str__(self):
        rs = self._var_full_name
        return rs

    @property
    def _var_full_name(self) -> str:
        """ ContainVar used at Component property """
        if getattr(self, '_var_fmt', None) is None:
            _c = self.init(None, '')
            return _c._var_fmt.get_value()
            # raise AttributeError('please call init first')
        return self._var_fmt.get_value()

    @classmethod
    def create(cls, _args_: Any = None, **kwargs) -> Self:
        value = _args_ if _args_ is not None else kwargs
        # v: Var = super().create(_name, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        rs = cls(
            _js_expr='',
            _var_type=cls,
            _var_is_local=True,
            _var_is_string=False,
            _var_data=None,
            _var_value=value,
        )
        return rs

    def init(self, parent: Optional[Component], name: str) -> Self:
        _vv = self._var_value
        fmt = ExFormatter(_vv, parent=parent, name=name)
        _var = dataclasses.replace(
            self,
            _js_expr=fmt.get_value(),
            _var_value=_vv,
            _var_fmt=fmt,
            _var_data=fmt.get_var_data(),
        )
        return _var

    def get_custom_components(self) -> set[CustomComponent]:
        rs = set()
        for ex in self._var_fmt._coms.values():
            rs |= ex.get_custom_components()
        return rs

    def get_custom_code(self) -> Set[str]:
        rs = set()
        for ex in self._var_fmt._coms.values():
            rs |= ex.get_custom_code()
        return rs

    def get_hooks(self) -> Dict[str, None]:
        return get_var_data_hooks(self)

    def get_imports(self) -> imports.ImportDict:
        return self._var_data.old_school_imports()

    def get_dynamic_imports(self) -> Set[str]:
        rs = set()
        for _, i in self._var_fmt.iter_items():
            rs |= i.get_dynamic_imports()
        return rs

    def to_hook_code(self) -> Dict[str | Var, None]:
        """ ContainVar used at hook code
        . only support list or dict
        . list item only support: JsValue, JsFunctionValue
        """
        support_clses = (JsValue, JsEvent, JsFunctionValue)
        _vv = self._var_value
        if isinstance(_vv, rx.Var):
            return {_vv: None}
        elif isinstance(_vv, support_clses):
            items = [_vv]
        elif isinstance(_vv, (list, dict)):
            items = _vv
        else:
            raise ValueError(f"to_hook_code Unsupported type {type(_vv)}")

        def _check(i):
            _is_ok = isinstance(i, support_clses)
            # assert _is_ok, \
            #     'ContainVar.to_hook_code list item only support: JsValue, JsFunctionValue'
            return _is_ok

        def _iter_items():
            _prefix = f'{self._var_fmt.name}_' if self._var_fmt.name else '_'
            if isinstance(items, list):
                for idx, item in enumerate(items):
                    yield f'{_prefix}{idx}', item
            elif isinstance(items, dict):
                for k, v in items.items():
                    yield f'{_prefix}{k}', v

        hooks: Dict[str, None] = {}
        for name, ex in _iter_items():
            if _check(ex):
                if isinstance(ex, JsEvent):
                    ex.get_ex_item(self, name)
                _hook = ex.to_hook_code(name)
            else:
                _hook = str(ex)  # support reflex's hook, like ConnectionToaster, use Var to code js
            hooks[_hook] = None

        return hooks


class PropBase(BaseModel):
    # v1
    class Config:
        arbitrary_types_allowed = True
    # v2
    # model_config = dict(
    #     arbitrary_types_allowed=True,  # 允许你在 Pydantic 模型中使用任意类型，而不仅仅是内置的 Python 类型
    # )

    def to_dict(self) -> dict:
        """
            . support use in Component, field is Var, can not use model_dump
        """
        # keys = self.model_fields.keys()  # v2
        keys = self.__fields__.keys()  # v1
        values = {}
        for k in keys:
            v = getattr(self, k)
            if v is None:
                continue
            values[k] = v
        # rs = self.model_dump(exclude_none=True)
        return values

    def to_component(self) -> Component:
        """ sometimes, prop use with rx.foreach, like TabItem """
        d = self.to_dict()
        c = container(d)
        return c


class PropVar(ContainVar):
    @classmethod
    def create(cls, prop: PropBase) -> Self:
        # v: Var = super().create(_name, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        rs = cls(
            _js_expr='',
            _var_type=cls,
            _var_is_local=True,
            _var_is_string=False,
            _var_data=None,
            _var_value=prop,
        )
        return rs

    def to_dict(self) -> dict:
        d = dict((k, v) for k, v in self.__dict__.items() if k[0] != '_')
        return d
        # return self._var_value.copy()

    def init(self, parent: Component, name: str) -> Self:
        return super().init(parent, name)

    def __bool__(self):
        return bool(self._var_value)


# @serializers.serializer(to=dict)
# def serialize_prop_var(prop: PropBase) -> dict:
#     _prop = cast(PropVarBase, prop)
#     rs = _prop.to_dict()
#     return rs


contain = ContainVar.create


class Container(Bare):
    def _render(self) -> Tag:
        from reflex.components.tags.tagless import Tagless
        return Tagless(contents=str(self.contents))

    @classmethod
    def create(cls, contents: ContainVar, name: str = None) -> Component:
        assert isinstance(contents, ContainVar), f'contents({type(contents)}) must be a ContainVar'
        rs = super().create(None)
        rs.contents = contents.init(rs, name)
        return rs

    def _get_all_custom_code(self) -> set[str]:
        codes = self.contents.get_custom_code()
        return codes

    def _get_all_custom_components(
            self, seen: set[str] | None = None
    ) -> Set[CustomComponent]:
        return self.contents.get_custom_components()

    def _get_dynamic_imports(self) -> str | None:
        rs = self.contents.get_dynamic_imports()
        return '\n'.join(rs) if rs else None


def container(
        data: Union[list, dict, JsValue, JsEvent, JsFunctionValue, ContainVar],
        name: str = '') -> rx.Component:
    """ wrap contain to Component, use for:
        .foreach:  rx.foreach(GlobalState.subnav_items, _sub_item)
            GlobalState.subnav_items = [{"title": "home", "href": "/home"}, ]
            def _sub_item(i: dict) -> rx.Component:
                b = helper.container(
                    dict(title=rx.link(i['title'], href=i['href']))
                )
                return b
    """
    d = contain(data) if not isinstance(data, ContainVar) else data
    b = Container.create(d, name=name)
    return b


class DataClassMixin:
    def to_component(self) -> Component:
        fields = dataclasses.fields(self)
        result = []
        for f in fields:
            v = getattr(self, f.name)
            if v is None:
                continue
            # elif isinstance(v, ContainVar):
            #     ...
            # elif isinstance(v, Var):
            #     ...  # v = v._js_expr
            result.append((f.name, v))
        d = dict(result)
        c = container(d)
        return c


_custom_jss = {}


class AntdBaseComponent(Component):
    _custom_components: Set[CustomComponent] = pydantic.PrivateAttr(default_factory=set)
    _ex_hooks: List[ContainVar] = pydantic.PrivateAttr(default_factory=list)
    _custom_js: str | None = pydantic.PrivateAttr(default=None)

    def _render_custom_js(self):
        _custom_js = self.__class__._custom_js
        if _custom_js in _custom_jss:
            return
        _custom_jss[_custom_js] = ''
        import sys
        from reflex.utils import prerequisites
        from os.path import dirname, join
        web_dir = '.web'  # prerequisites.get_web_dir()
        cur_path = dirname(sys.modules[self.__module__].__file__)
        js_path = join(cur_path, _custom_js)
        # if not path.exists(path.dirname(js_path)):
        #     os.makedirs(path.dirname(js_path), exist_ok=True)
        if path.isfile(js_path):
            suffix = _custom_js.split('.')[-1]
            dst_path = join(web_dir, f'{self.library[1:]}.{suffix}')
        else:
            dst_path = join(web_dir, f'{self.library[1:]}')
        dst_parent_path = dirname(dst_path)
        if not path.exists(dst_parent_path):
            os.makedirs(dst_parent_path, exist_ok=True)
        prerequisites.path_ops.cp(js_path, dst_path)

    def __init__(self, *args, ex_hooks: List[ContainVar | list | dict] = None, **kwargs):
        contains = {}
        exs = {}
        kw = {}
        for k, v in kwargs.items():
            if isinstance(v, (ContainVar, PropBase)):
                if isinstance(v, PropBase):
                    v = PropVar.create(v)
                contains[k] = v
            elif isinstance(v, (JsValue, JsEvent)):
                exs[k] = v
            elif isinstance(v, Component):
                kw[k] = LiteralAntdComponentVar.create(v)
            else:
                kw[k] = v
        # super().__init__(*args, **kw)
        try:
            super().__init__(*args, **kw)
        except Exception as err:
            logging.exception(f"class<{self.__class__}>, args={args}, kw={kw}, error: {err}")
            raise
        self._init_contains(contains, exs, ex_hooks)

    def _render(self, *args, **kwargs) -> Tag:
        if isinstance(self.__class__._custom_js, str):
            self._render_custom_js()
        rs = super()._render(*args, **kwargs)
        return rs

    def _get_all_custom_components(
            self, seen: set[str] | None = None
    ) -> Set[CustomComponent]:
        _coms = super()._get_all_custom_components(seen=seen)
        if hasattr(self, '_custom_components') and self._custom_components:
            _coms |= self._custom_components
        return _coms

    def _get_all_custom_code(self) -> Set[str]:
        code = super()._get_all_custom_code()
        for v in self._iter_all_contains():
            code.update(v.get_custom_code())
        for k, v in self._iter_exs():
            code.update(v.get_custom_code())
        for n, prop in self.iter_component_props():
            code.update(prop._get_all_custom_code())
        return code

    def _get_all_dynamic_imports(self) -> Set[str]:
        rs = super()._get_all_dynamic_imports()
        for v in self._iter_all_contains():
            rs |= v.get_dynamic_imports()
        for k, v in self._iter_exs():
            rs |= v.get_dynamic_imports()
        return rs

    def _get_style(self) -> dict:
        """Get the style for the component.

        Returns:
            The dictionary of the component style as value and the style notation as key.
        """
        return {"style": self.style}

    def _add_style_recursive(
            self, style: ComponentStyle
            , theme: Optional[Component] = None
    ) -> Component:
        # hack: support style for properties
        _prop_keys = []
        if type(self) in style:
            component_style = style[type(self)]
        elif self.create in style:
            component_style = style[self.create]
        else:
            component_style = None
        if component_style:
            for k, v in component_style.copy().items():
                # is property
                if hasattr(self, k) and getattr(self, k) is None:
                    setattr(self, k, v)
                    _prop_keys.append(k)

        rs = super()._add_style_recursive(style, theme=theme)
        # remove from style
        for _k in _prop_keys:
            self.style.pop(_k, None)
        return rs

    def add_imports(self) -> dict[str, str | ImportVar | list[str | ImportVar]]:
        _imports = {}
        for ex in self._iter_all_contains():
            _imports = imports.merge_imports(
                ex.get_imports(),
                _imports,
            )
        return _imports

    def _get_all_hooks_internal(self) -> dict[str, None]:
        try:
            return self._cache_get_all_hooks_internal_
        except AttributeError:
            self._cache_get_all_hooks_internal_ = super()._get_all_hooks_internal()
            return self._cache_get_all_hooks_internal_

    def _get_hooks_internal(self) -> dict[str, VarData | None]:
        if is_dynamic:
            return {}
        rs = super()._get_hooks_internal()
        return rs

    def _get_all_hooks(self) -> dict[str, VarData | None]:
        """  """
        rs = super()._get_all_hooks()

        # remove double Hooks.EVENTS, component._get_all_hooks_internal and _get_all_hooks is not merge
        # in stateful_component.js.jinja2,
        if version <= '000.006.007':
            _i_hooks = self._get_all_hooks_internal()
            for _k in set(_i_hooks).intersection(rs):
                rs.pop(_k, None)

        return rs

    def add_hooks(self) -> list[str | Var]:
        hooks = []
        for ex in self._ex_hooks:
            hooks.extend(ex.get_hooks().keys())
            codes = ex.to_hook_code()
            if codes:
                hooks.extend(codes)

        return hooks

    def _get_vars_hooks(self) -> dict[str, None]:
        var_hooks = super()._get_vars_hooks()
        if [h for h in var_hooks if 'addEvents' in h]:
            var_hooks = {Hooks.EVENTS: None, **var_hooks}
        return var_hooks

    def iter_component_props(self) -> Iterable[tuple[str, Component]]:
        cls = self.__class__
        _props = cls.get_props()
        for name, field in cls.get_fields().items():
            if name not in _props:
                continue
            _p = getattr(self, name)
            if isinstance(_p, Var):
                _v = getattr(_p, '_var_value', None)
                if isinstance(_v, Component):
                    yield name, _v

    def _iter_contains(self) -> Iterable[Tuple[str, ContainVar]]:
        """ iter component's property which is ContainVar """
        for k in self.get_fields().keys():
            v = getattr(self, k, None)
            if isinstance(v, ContainVar):
                yield k, v

    def _iter_exs(self) -> Iterable[Tuple[str, ExItem]]:
        """ iter component's property which is ContainVar """
        for k in self.get_fields().keys():
            v = getattr(self, k, None)
            if isinstance(v, ExVar) and isinstance(v._var_value, ExItem):
                yield k, v._var_value

    def _iter_ex_hooks(self) -> Iterable[ContainVar]:
        for ex in self._ex_hooks:
            yield ex

    def _iter_all_contains(self) -> Iterable[ContainVar]:
        for k, v in self._iter_contains():
            yield v
        for ex in self._iter_ex_hooks():
            yield ex

    def _init_contains(self, contains: Dict[str, ContainVar], exs: Dict[str, Any], ex_hooks: List[ContainVar]) -> None:
        self._ex_hooks = []
        if ex_hooks:
            for ex in ex_hooks:
                if not isinstance(ex, ContainVar):
                    ex = contain(ex)
                self._ex_hooks.append(ex.init(self, ''))

        for k, v in contains.items():
            v = v.init(self, k)
            self._custom_components |= v.get_custom_components()
            setattr(self, k, v)

        event_keys = self.get_event_triggers().keys()
        for k, v in exs.items():
            if isinstance(v, (JsValue, JsEvent)):
                item = v.get_ex_item(self, k)
            else:
                raise NotImplementedError(f"Unsupported type: {type(v)}")
            self._custom_components |= item.get_custom_components()
            _v = ExVar(
                _js_expr=item.serialize(),
                _var_data=item.get_var_data(),
                _var_value=item,
            )
            if k in event_keys:
                self.event_triggers[k] = _v
            else:
                setattr(self, k, _v)


class AntdComponentVar(Var[Component], python_types=AntdBaseComponent):
    """A Var that represents a Component."""
    ...


@dataclasses.dataclass(
    eq=False,
    frozen=True,
)
class LiteralAntdComponentVar(vars_base.CachedVarOperation, vars_base.LiteralVar, AntdComponentVar):
    """A Var that represents a Component that get _var_value._var_data forever """

    _var_value: Component = dataclasses.field(default_factory=lambda: Bare.create(""))

    @vars_base.cached_property_no_lock
    def _cached_var_name(self) -> str:
        """Get the name of the var.

        Returns:
            The name of the var.
        """
        var_data = self._get_all_var_data()
        if var_data is not None:
            # flatten imports
            imported_names = {j.alias or j.name for i in var_data.imports for j in i[1]}
        else:
            imported_names = set()
        return str(render_dict_to_var(self._var_value.render(), imported_names))

    @vars_base.cached_property_no_lock
    def _cached_get_all_var_data(self) -> VarData | None:
        """Get the VarData for the var.

        Returns:
            The VarData for the var.
        """
        return VarData.merge(
            VarData(
                imports={
                    "@emotion/react": [
                        ImportVar(tag="jsx"),
                    ],
                }
            ),
            VarData(
                imports=self._var_value._get_all_imports(),
                hooks=get_component_hooks(self._var_value),
            ),
            VarData(
                imports={
                    "react": [
                        ImportVar(tag="Fragment"),
                    ],
                }
            ),
        )

    def __hash__(self) -> int:
        """Get the hash of the var.

        Returns:
            The hash of the var.
        """
        return hash((type(self).__name__, self._js_expr))

    @classmethod
    def create(
            cls,
            value: Component,
            _var_data: VarData | None = None,
    ):
        """Create a var from a value.

        Args:
            value: The value of the var.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return LiteralAntdComponentVar(
            _js_expr="",
            _var_type=type(value),
            _var_data=_var_data,
            _var_value=value,
        )


class AntdComponent(AntdBaseComponent):
    """A component that wraps an Antd component."""
    library = "antd"

    hidden: Optional[Var[bool]]

    # @staticmethod
    # @lru_cache(maxsize=None)
    # def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
    #     from .antd.base import config_provider, antd_app
    #     return {
    #         (50, "AntdApp"): _config_app if _config_app is not None else antd_app(),
    #         (51, "AntdProvider"): _config_provider if _config_provider is not None else config_provider(),
    #     }


class AntdNoSSRComponent(NoSSRComponent, AntdBaseComponent):
    ...


class AntdFragment(AntdBaseComponent):
    library = "react"
    tag = "Fragment"


class AntdSubComponent(AntdBaseComponent, Component):
    base_tag: str = None

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        return {}


_config_provider: Optional[Component] = None
_config_app: Optional[Component] = None


def default_config(provider: Component = None, antd_app: Component = None):
    global _config_provider, _config_app
    from reflex.utils import prerequisites
    from reflex import constants
    from .antd.base import ConfigProvider, AntdApp, antd_registry_provider
    if provider is not None:
        assert isinstance(provider, ConfigProvider)
        _config_provider = provider
    else:
        _config_provider = ConfigProvider()
    if antd_app is not None:
        assert isinstance(antd_app, AntdApp)
        _config_app = antd_app
    else:
        _config_app = AntdApp()

    _app = getattr(prerequisites.get_app(), constants.CompileVars.APP)
    _old_error_boundary = _app.error_boundary

    def _antd_error_boundary(*children: Component) -> Component:
        _coms = [_old_error_boundary(*children)] if _old_error_boundary else children
        _cfp = _config_provider.copy(update=dict(
            children=[
                _config_app.copy(update=dict(children=_coms)),
            ],
        ))
        is_app_router = False
        if not is_app_router:
            return _cfp
        else:
            return antd_registry_provider(_cfp)
    _app.error_boundary = _antd_error_boundary


_dynamic_ctx: dict = None


def get_dynamic_ctx(**kwargs) -> dict:
    global _dynamic_ctx
    if not _dynamic_ctx:
        from reflex_antd import (
            helper, display, entry, feedback, general, layout,
            navigation,
            charts,
        )
        _dynamic_ctx = {
            "rx": rx,
            'helper': helper,
            'display': display,
            'general': general,
            'layout': layout,
            'feedback': feedback,
            'entry': entry,
            'navigation': navigation,
            'charts': charts,
            **helper.__dict__,
        }
    kwargs.update(_dynamic_ctx)
    return kwargs


def patch_after_start():
    global use_pretty_dumps, default_to_js, is_dynamic
    # for support dynamic, which remove lines
    use_pretty_dumps = False
    default_to_js = True
    is_dynamic = True
    # line_stripped.startswith("{") and line_stripped.endswith("}")


def patch_all():
    from reflex import constants, vars
    from reflex.utils import prerequisites
    from reflex.compiler import templates, compiler
    from reflex.vars import sequence

    # hack json.dumps: support unicode
    sequence.json = util

    constants.Templates.Dirs.JINJA_TEMPLATE = [path.join(template_path, 'jinja'),
                                               constants.Templates.Dirs.JINJA_TEMPLATE]

    templates.DOCUMENT_ROOT = templates.get_template("web/pages/_document.js.jinja2")
    templates.TAILWIND_CONFIG = templates.get_template("web/pages/tailwind.config.js.jinja2")

    _r_js_regex = re.compile(r'"/([/*|\(\)\[\]+\\:\w-]+)/"')

    def _support_js_regex(data: str) -> str:
        s = _r_js_regex.sub(r'/\1/', data)
        return s.replace('\\\\', '\\') \
            .replace(""""'""", '') \
            .replace(''''"''', '')

    def _wrap_js_regex(_wrap_func, *args, **kwargs):
        d = _wrap_func(*args, **kwargs)
        return _support_js_regex(d)

    compiler._compile_tailwind = functools.partial(_wrap_js_regex, compiler._compile_tailwind)

    old_update_next_config = prerequisites.update_next_config
    old__update_next_config = prerequisites._update_next_config

    # 2. https://github.com/ant-design/pro-components/issues/8543
    def my__update_next_config(*args, **kwargs) -> str:
        fix_antd_pro = """, experimental: {
    forceSwcTransforms: true,
    optimizePackageImports: [
      '@ant-design/pro-card',
      '@ant-design/pro-components',
      '@ant-design/pro-descriptions',
      '@ant-design/pro-field',
      '@ant-design/pro-form',
      '@ant-design/pro-layout',
      '@ant-design/pro-list',
      '@ant-design/pro-layout',
      '@ant-design/pro-provider',
      '@ant-design/pro-skeleton',
      '@ant-design/pro-table',
      '@ant-design/pro-utils',
    ]
  }, transpilePackages:"""

        def _hack_json_dumps(next_config: dict):
            # sort transpilePackages, make sure next_config_file no update every times
            next_config["transpilePackages"].sort()
            return _old_json_dumps(next_config)
        _old_json_dumps = json.dumps
        json.dumps = _hack_json_dumps
        try:
            rs = old__update_next_config(*args, **kwargs)
        finally:
            json.dumps = _old_json_dumps

        return rs.replace(', transpilePackages:', fix_antd_pro)


    # 1. https://github.com/vercel/next.js/issues/58817 next.js 14.0.3 fail to use antd
    def my_update_next_config(export=False, transpile_packages: Optional[List[str]] = None):
        transpile_packages = transpile_packages or []
        transpile_packages.extend([
            "@ant-design",
            "@rc-component",
            "antd",
            "rc-cascader",
            "rc-checkbox",
            "rc-collapse",
            "rc-dialog",
            "rc-drawer",
            "rc-dropdown",
            "rc-field-form",
            "rc-image",
            "rc-input",
            "rc-input-number",
            "rc-mentions",
            "rc-menu",
            "rc-motion",
            "rc-notification",
            "rc-pagination",
            "rc-picker",
            "rc-progress",
            "rc-rate",
            "rc-resize-observer",
            "rc-segmented",
            "rc-select",
            "rc-slider",
            "rc-steps",
            "rc-switch",
            "rc-table",
            "rc-tabs",
            "rc-textarea",
            "rc-tooltip",
            "rc-tree",
            "rc-tree-select",
            "rc-upload",
            "rc-util",
        ])
        return old_update_next_config(export=export, transpile_packages=transpile_packages)

    prerequisites.update_next_config = my_update_next_config
    prerequisites._update_next_config = my__update_next_config

    def _my_get_memoized_event_triggers(
            cls,
            component: Component,
    ) -> dict[str, tuple[Var, str]]:
        """ fix: some js function can not memo """
        pass

    # StatefulComponent._get_memoized_event_triggers = classmethod(_my_get_memoized_event_triggers)


def vt(t):
    return t | Var[t]


ReactNode = BaseComponent | str
JsNode = JsValue | JsEvent
ExTypes = JsValue | ContainVar | JsEvent
fragment = AntdFragment.create
