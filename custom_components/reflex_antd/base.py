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
try:
    from reflex.base import pydantic_main as pydantic
except ImportError:
    from reflex.base import pydantic

from reflex.components.component import BaseComponent, CustomComponent, StatefulComponent, ComponentStyle
from reflex.components.base.bare import Bare
from reflex.components.core import Foreach, Match
from reflex.constants import Hooks, Reflex, MemoizationDisposition, MemoizationMode
from reflex.utils import imports, format, serializers, exceptions
from reflex.vars import BaseVar, VarData
from reflex.event import EventHandler, EventSpec, EventChain

from .constant import SizeType
from .util import OrderedSet

# 0.4.6 -> 000.004.006
version = '.'.join(map(lambda x: x.zfill(3), Reflex.VERSION.split('.')))

my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, '.templates')

APP_ROUTER = False
RE_KEY_IDX = re.compile(r'\.\d+\.')

memo_never = MemoizationMode().set(disposition=MemoizationDisposition.NEVER)
memo_never_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.NEVER, recursive=False)
memo_always = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS)
memo_always_no_recursive = MemoizationMode().set(disposition=MemoizationDisposition.ALWAYS, recursive=False)


def stateful(hd: Callable[..., Component] = None, forced=True) -> Callable:
    """ render a component into a function """

    def _my(_hd: Callable[..., Component]) -> Callable:
        @wraps(_hd)
        def _wrap(*args, **kwargs):
            _com = _hd(*args, **kwargs)
            if forced:
                _com._memoization_mode = memo_always
                # _com._memoization_mode.recursive = False
            _sc = StatefulComponent.create(_com)
            return _sc if _sc is not None else _com
            # return _com

        return _wrap

    if hd is None:
        return _my
    else:
        return _my(hd)


def pretty_dumps(value: Any, indent=2) -> str:
    return format.json.dumps(value, ensure_ascii=False, default=serializers.serialize, indent=indent)


def get_component_all_imports(com: Component) -> imports.ImportDict:
    if version <= '000.004.006':
        return {} if isinstance(com, str) else com.get_imports()
    else:
        return {} if isinstance(com, str) else com._get_all_imports()


def get_component_hooks(com) -> Set[str] | Dict[str, None]:
    if version <= '000.004.006':
        return set() if isinstance(com, str) else com.get_hooks()
    return {} if isinstance(com, str) \
        else com._get_all_hooks_internal() | com._get_all_hooks()


def get_component_custom_code(com: Component) -> Set[str]:
    if version <= '000.004.006':
        return com.get_custom_code() if isinstance(com, BaseComponent) else set()
    return com._get_all_custom_code() if isinstance(com, BaseComponent) else set()


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

    def get_state(self) -> str:
        return ''

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        if version <= '000.004.006':
            return set()
        return {}

    def get_interpolations(self) -> List[Tuple[int, int]]:
        return []

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
            interpolations=self.get_interpolations(),
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

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return get_component_hooks(self.item)

    def get_custom_components(self) -> set[CustomComponent]:
        return {self.item} if isinstance(self.item, CustomComponent) else set()

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
    hd: EventHandler
    # event_trigger use for custom trigger, must work with fmt=True
    event_trigger: Callable
    _item: "ExEventHandlerItem" = None

    def __init__(self, hd: Any, js: str = '', fmt: bool = False, event_trigger: Callable = None):
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

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return self.hd_item.get_hooks()

    def get_imports(self) -> imports.ImportDict:
        return self.hd_item.get_imports()


class ExLambdaHandlerItem(ExItem):
    item: Callable
    event_trigger: Callable = None

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

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

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        if version <= '000.004.005':
            key = self._get_event_trigger_key()
            chain = self.parent._create_event_chain(key, self.item)
        else:
            key = self._get_event_trigger()
            chain = self.parent._create_event_chain(key, self.item)
        rendered_chain = format.format_prop(chain).strip("{}")
        _hook = f"""const {self._get_fn_name()} = useCallback({rendered_chain}, [addEvents, Event]);"""

        if version <= '000.004.006':
            return {_hook}
        return {_hook: None}


class ExCallableItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

    def serialize(self) -> str:
        return str(self.item())

    def get_imports(self) -> imports.ImportDict:
        return get_component_all_imports(self.item())

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return get_component_hooks(self.item())


class ExStateItem(ExItem):
    item: BaseVar

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, BaseVar) and item._var_full_name.startswith("state__")

    def serialize(self) -> str:
        return self.item._var_full_name

    def get_imports(self) -> imports.ImportDict:
        return self.item._var_data.imports

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return self.item._var_data.hooks

    def get_state(self) -> str:
        return self.item._var_data.state


class FakeComponentMixin:
    def _create_event_chain(self, *args, **kwargs):
        return Component._create_event_chain(self, *args, **kwargs)

    def get_event_triggers(self) -> Dict[str, Any]:
        return {}

    def get_hooks(self) -> Set[str] | Dict[str, None]:
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

    def __init__(self, value: Union[str, Callable, Component] = None, **kwargs):
        self.value = value
        self._init(**kwargs)

    def _init(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_ex_item(self, parent, key) -> ExItem:
        item = ExJsItem(self, parent, key=key)
        return item

    def serialize(self) -> str:
        return f"({self.value if isinstance(self.value, str) else str(self.value).strip('{}')})"

    def get_imports(self) -> imports.ImportDict:
        return get_component_all_imports(self.value)

    def get_state(self) -> str:
        return ''

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return get_component_hooks(self.value)

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
        )

    def get_custom_components(self) -> set[CustomComponent]:
        return get_component_custom_code(self.value)

    def to_hook_code(self, name: str) -> str:
        code = self.serialize()
        return code.strip('()')


class JsFunctionValue(JsValue):
    _value: Union[str, Component]

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)
        self._args = inspect.getfullargspec(self.value)
        args = self._args.args
        self._value = self.value(*[CasualVar.create_safe(arg, _var_is_string=False) for arg in args])

    def serialize(self) -> str:
        is_component = False
        if isinstance(self._value, str):
            v = self._value
        elif isinstance(self._value, Component):
            is_component = True
            v = str(self._value)
        else:
            raise TypeError(self._value)
        sep_1, sep_2 = ('{{', '}}') if not is_component else ('(', ')')
        return f"""(({','.join(self._args.args)}) => 
        {sep_1} {v} {sep_2} )"""

    def get_imports(self) -> imports.ImportDict:
        return get_component_all_imports(self._value)

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return get_component_hooks(self._value)

    def get_custom_components(self) -> set[CustomComponent]:
        return set() if not isinstance(self._value, CustomComponent) else {self._value}

    def to_hook_code(self, name: str) -> str:
        code = self.serialize().strip('()')
        code = f"{name}{code.replace('=>', ' ', 1)}"
        return code


def js_value(value: Union[str, Callable, Foreach, Match], **kwargs) -> JsValue:
    """ """
    if isinstance(value, (str, Component)):
        return JsValue(value, **kwargs)
    if isinstance(value, Callable):
        return JsFunctionValue(value, **kwargs)
    raise NotImplemented("Not implemented: %s(%s)" % (type(value), value))


class ExJsItem(ExItem):
    item: JsValue

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, JsValue)

    def serialize(self) -> str:
        return self.item.serialize()

    def get_imports(self) -> imports.ImportDict:
        return self.item.get_imports()

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return self.item.get_hooks()

    def get_custom_components(self) -> set[CustomComponent]:
        return self.item.get_custom_components()


class ExVarItem(ExItem):
    item: Var

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Var)

    def serialize(self) -> str:
        return str(self.item).strip('{}')

    def get_imports(self) -> imports.ImportDict:
        return self.item._var_data.imports if self.item._var_data else {}

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return self.item._var_data.hooks if self.item._var_data else {}

    def get_state(self) -> str:
        return self.item._var_data.state if self.item._var_data else ""

    def get_interpolations(self) -> List[Tuple[int, int]]:
        return self.item._var_data.interpolations if self.item._var_data else []


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

    def __init__(self, value: Any, parent: Component, name: str = ''):
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
            elif isinstance(_v, dict):
                return _dict(_v, pkey=key)
            elif isinstance(_v, (int, float, str, bool)):
                return _v

            _id = _v
            for ex in self.items:
                if ex.isinstance(_v):
                    _id = uuid.uuid4().hex
                    self._coms[_id] = ex(_v, self.parent, key=key)
                    return _id

            if isinstance(_v, Base):
                _d = dict(_v._iter(exclude_unset=True, exclude_none=True, to_dict=False))
                return _dict(_d, pkey=key)
            elif dataclasses.is_dataclass(_v):
                _d = dataclasses.asdict(_v)
                return _dict(_d, pkey=key)

            return _v

        def _list(_v: List, pkey: str) -> List[Any]:
            return [_op(i, key=f'{pkey}.{idx}') for idx, i in enumerate(_v)]

        def _dict(_v: Dict, pkey: str) -> Dict[str, Any]:
            return dict((format.to_camel_case(k), _op(v, key=f'{pkey}.{k}')) for k, v in _v.items() if v is not None)

        rs = _op(value, key=self.name)
        self._value = rs

    def get_ex_item(self, key: str) -> ExItem | None:
        for i in self._coms.values():
            if i.key == key:
                return i

    def get_value(self) -> str:
        v = pretty_dumps(self._value)
        for k, ex in self._coms.items():
            v = v.replace(f'"{k}"', ex.serialize())
        return v

    def get_imports(self) -> imports.ImportDict:
        _imports = imports.merge_imports(
            *(c.get_imports() for c in self._coms.values()),
        )
        return _imports

    def get_state(self) -> str:
        for _, ex in self._coms.items():
            _state = ex.get_state()
            if _state != '':
                return _state
        return ''

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        if version <= '000.004.006':
            hooks = set()
        else:
            hooks = {}
        for _, ex in self._coms.items():
            _hooks = ex.get_hooks()
            hooks.update(_hooks)
        return hooks

    def get_interpolations(self) -> List[Tuple[int, int]]:
        rs = []
        for _, ex in self._coms.items():
            rs += ex.get_interpolations()
        return rs

    def get_var_data(self) -> VarData:
        return VarData(
            state=self.get_state(),
            imports=self.get_imports(),
            hooks=self.get_hooks(),
            interpolations=self.get_interpolations(),
        )


class ExVar(BaseVar):
    _var_value: Any

    def __init__(self, *args, _var_value=None, **kwargs):
        self._var_value = _var_value
        super().__init__(*args, **kwargs)

    @classmethod
    def create(
            cls, value: Any, _var_is_local: bool = True, _var_is_string: bool = False,
            _var_data: VarData | None = None,
    ) -> Var | None:
        v = BaseVar.create(value, _var_is_local=_var_is_local, _var_is_string=_var_is_string, _var_data=_var_data)
        return cls(
            _var_name=v._var_name,
            _var_type=v._var_type,
            _var_is_local=v._var_is_local,
            _var_is_string=v._var_is_string,
            _var_data=v._var_data,
        )

    def _replace(self, merge_var_data=None, **kwargs: Any) -> Self:
        return self.__class__(
            _var_name=kwargs.pop("_var_name", self._var_name),
            _var_type=kwargs.pop("_var_type", self._var_type),
            _var_is_local=kwargs.pop("_var_is_local", self._var_is_local),
            _var_is_string=kwargs.pop("_var_is_string", self._var_is_string),
            _var_full_name_needs_state_prefix=kwargs.pop(
                "_var_full_name_needs_state_prefix",
                self._var_full_name_needs_state_prefix,
            ),
            _var_data=VarData.merge(
                kwargs.get("_var_data", self._var_data), merge_var_data
            ),
        )


class CasualVar(ExVar):
    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except (AttributeError,):
            if name.startswith("_"):
                raise
            return self.create_safe(
                f'{self._var_name}.{name}',
                _var_is_string=False,
                _var_is_local=False,
            )

    def __getitem__(self, i: Any) -> Var:
        try:
            return super().__getitem__(i)
        except (exceptions.VarTypeError,):
            if str(i).startswith("_"):
                raise
            return self.create_safe(
                f'{self._var_name}["{i}"]',
                _var_is_string=False,
                _var_is_local=False,
            )

    def to_js(self) -> Self:
        return self._replace(
            _var_type=str,
            _var_name=f'({self._var_name})'
        )

    def to_react(self) -> Self:
        return self._replace(
            _var_type=str,
            _var_name=f'{{{self._var_name}}}'
        )


casual_var = CasualVar.create


class NodeVar(ExVar):
    """
    support:
        . base types: int, float, bool, str
        . js, like: {show ? 11 : 0}
     """
    pass


class ContainVar(ExVar):
    _var_fmt: ExFormatter

    @property
    def _var_full_name(self) -> str:
        """ ContainVar used at Component property """
        if getattr(self, '_var_fmt', None) is None:
            raise AttributeError('please call init first')
        return self._var_fmt.get_value()

    @classmethod
    def create(cls, _args_: Any = None, **kwargs) -> Self:
        value = _args_ if _args_ is not None else kwargs
        # v: BaseVar = super().create(_name, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        rs = cls(
            _var_name='',
            _var_type=cls,
            _var_is_local=True,
            _var_is_string=False,
            _var_data=None,
            _var_value=value,
        )
        return rs

    def init(self, parent: Component, name: str) -> Self:
        fmt = ExFormatter(self._var_value, parent=parent, name=name)
        self._var_fmt = fmt
        self._var_data = fmt.get_var_data()
        return self

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

    def get_hooks(self) -> Set[str] | Dict[str, None]:
        return self._var_data.hooks

    def get_imports(self) -> imports.ImportDict:
        return self._var_data.imports

    def to_hook_code(self) -> Dict[str, None]:
        """ ContainVar used at hook code
        . only support list or dict
        . list item only support: JsValue, JsFunctionValue
        """
        assert isinstance(self._var_value, (list, dict)), 'ContainVar.to_hook_code only supports list'
        items = self._var_value if isinstance(self._var_value, list) else self._var_value.values()
        for item in items:
            assert isinstance(item, (JsValue, JsFunctionValue, JsEvent)), \
                'ContainVar.to_hook_code list item only support: JsValue, JsFunctionValue'

        def _iter_items():
            _prefix = f'{self._var_fmt.name}_' if self._var_fmt.name else '_'
            if isinstance(self._var_value, list):
                for idx, item in enumerate(self._var_value):
                    yield f'{_prefix}{idx}', item
            elif isinstance(self._var_value, dict):
                for k, v in self._var_value.items():
                    yield f'{_prefix}{k}', v

        hooks: Dict[str, None] = {}
        for name, ex in _iter_items():
            if isinstance(ex, JsEvent):
                ex.get_ex_item(self, name)
            hook = ex.to_hook_code(name)
            hooks[hook] = None

        return hooks


contain = ContainVar.create


def container(data: Union[list, dict, JsValue], name: str = '') -> rx.Component:
    """ wrap contain to Component, use for:
        .foreach:  rx.foreach(GlobalState.subnav_items, _sub_item)
            GlobalState.subnav_items = [{"title": "home", "href": "/home"}, ]
            def _sub_item(i: dict) -> rx.Component:
                b = helper.container(
                    dict(title=rx.link(i['title'], href=i['href']))
                )
                return b
    """
    d = contain(data)
    b = Bare()
    d.init(b, name)
    b.contents = d
    return b


# no use
class VarDataMixin:
    def __iter__(self):
        v = Var()
        v._var_data = VarData(
            imports=self.get_imports(),
        )
        yield from [v]


class DataClassMixin:
    def to_component(self) -> Component:
        fields = dataclasses.fields(self)
        result = []
        for f in fields:
            v = getattr(self, f.name)
            if v is None:
                continue
            elif isinstance(v, BaseVar):
                ...  # v = v._var_full_name
            result.append((f.name, v))
        d = dict(result)
        c = container(d)
        return c


class AntdBaseComponent(Component):
    _custom_components: Set[CustomComponent] = pydantic.PrivateAttr(default_factory=set)
    _ex_hooks: List[ContainVar] = pydantic.PrivateAttr(default_factory=list)

    def __init__(self, *args, ex_hooks: List[ContainVar | list | dict] = None, **kwargs):
        contains = {}
        exs = {}
        kw = {}
        for k, v in kwargs.items():
            if isinstance(v, ContainVar):
                contains[k] = v
            elif isinstance(v, (JsValue, JsEvent)):
                exs[k] = v
            else:
                kw[k] = v
        # super().__init__(*args, **kw)
        try:
            super().__init__(*args, **kw)
        except Exception as err:
            print(f"class<{self}>, args={args}, kw={kw}, error: {err}")
            raise
        self._init_contains(contains, exs, ex_hooks)

    def _get_all_custom_components(
            self, seen: set[str] | None = None
    ) -> Set[CustomComponent]:
        _coms = super()._get_all_custom_components(seen=seen)
        if hasattr(self, '_custom_components') and self._custom_components:
            _coms |= self._custom_components
        return _coms

    def _get_all_custom_code(self) -> Set[str]:
        code = super()._get_all_custom_code()
        for k, v in self._iter_contains():
            code.update(v.get_custom_code())
        return code

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
        if self._ex_hooks:
            for ex in self._ex_hooks:
                _imports = imports.merge_imports(
                    ex.get_imports(),
                    _imports,
                )
        return _imports

    def _get_all_hooks(self) -> dict[str, None]:
        """ fix 0.5.1 bug #3365 """
        rs = super()._get_all_hooks()
        rs = dict((k, None) for k in rs.keys())
        return rs

    def add_hooks(self) -> list[str]:
        hooks = []
        if self._ex_hooks:
            for ex in self._ex_hooks:
                hooks.extend(ex.get_hooks().keys())
                codes = ex.to_hook_code()
                if codes:
                    hooks.extend(codes)

        return hooks

    def _get_events_hooks(self) -> set[str] | Dict[str, None]:
        _hooks = super()._get_events_hooks()
        js_events: List[BaseVar] = [
            v for k, v in self.event_triggers.items()
            if isinstance(v, BaseVar) and v._var_data is not None and v._var_data.hooks]

        if version <= '000.004.006':
            rs = OrderedSet(_hooks)
        else:
            rs = _hooks

        if js_events:
            for ev in js_events:
                rs |= ev._var_data.hooks
        return rs

    def _get_hooks_internal(self) -> Set[str] | Dict[str, None]:
        """Get the React hooks for this component managed by the framework.

        Downstream components should NOT override this method to avoid breaking
        framework functionality.

        Returns:
            Set of internally managed hooks.
        """
        # need order hooks, useContext code need first
        if version <= '000.004.006':
            s = OrderedSet(
                hook
                for hook in [self._get_mount_lifecycle_hook(), self._get_ref_hook()]
                if hook
            )

            s |= self._get_events_hooks()
            var_hooks = self._get_vars_hooks()
            if [h for h in var_hooks if 'addEvents' in h]:
                s.add(Hooks.EVENTS)
            s |= var_hooks
            s |= self._get_special_hooks()
            return s
        else:
            s = {
                hook: None
                for hook in [self._get_ref_hook(), self._get_mount_lifecycle_hook()]
                if hook is not None
            }
            var_hooks = self._get_vars_hooks()
            if [h for h in var_hooks if 'addEvents' in h]:
                s[Hooks.EVENTS] = None
            s |= var_hooks
            s |= self._get_events_hooks()
            s |= self._get_special_hooks()
            return s

    def _iter_contains(self) -> Iterable[Tuple[str, ContainVar]]:
        for k in self.get_fields().keys():
            v = getattr(self, k, None)
            if isinstance(v, ContainVar):
                yield k, v

    def _init_contains(self, contains: Dict[str, ContainVar], exs: Dict[str, Any], ex_hooks: List[ContainVar]) -> None:
        self._ex_hooks = []
        if ex_hooks:
            for ex in ex_hooks:
                if not isinstance(ex, ContainVar):
                    ex = contain(ex)
                self._ex_hooks.append(ex.init(self, ''))

        for k, v in contains.items():
            v.init(self, k)
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
                _var_name=item.serialize(),
                _var_is_local=True,
                _var_data=item.get_var_data(),
                _var_value=v,
            )
            if k in event_keys:
                self.event_triggers[k] = _v
            else:
                setattr(self, k, _v)


class AntdComponent(AntdBaseComponent):
    """A component that wraps an Antd component."""
    library = "antd"

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        from .antd.base import config_provider
        return {
            (40, "AntdProvider"): _config_provider if _config_provider is not None else config_provider(),
        }


class AntdSubComponent(AntdBaseComponent, Component):
    base_tag: str = None

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        return {}


_config_provider: Optional[Component] = None


def default_config(provider: Component):
    global _config_provider
    from .antd.base import ConfigProvider
    assert isinstance(provider, ConfigProvider)
    _config_provider = provider


def patch_all():
    from reflex import constants, vars
    from reflex.compiler import templates

    constants.Templates.Dirs.JINJA_TEMPLATE = [path.join(template_path, 'jinja'),
                                               constants.Templates.Dirs.JINJA_TEMPLATE]

    templates.DOCUMENT_ROOT = templates.get_template("web/pages/_document.js.jinja2")
    old_extract_var_data = vars._extract_var_data

    def _my_extract_var_data(value: Union[Iterable, Component]) -> list[VarData | None]:
        if isinstance(value, Component):
            return [
                VarData(
                    imports=get_component_all_imports(value),
                    hooks=get_component_hooks(value),
                )
            ]
        var_datas = old_extract_var_data(value)
        return var_datas

    vars._extract_var_data = _my_extract_var_data

    def _my_get_memoized_event_triggers(
            cls,
            component: Component,
    ) -> dict[str, tuple[Var, str]]:
        """ fix: some js function can not memo """
        pass

    # StatefulComponent._get_memoized_event_triggers = classmethod(_my_get_memoized_event_triggers)


ReactNode = Union[str, Component]
JsNode = Union[JsValue, JsEvent]
