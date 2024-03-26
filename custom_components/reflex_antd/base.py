from typing import Type, Any, Tuple, Dict, List, Iterable, Callable, Set, Union
from os import path
from abc import ABC, abstractmethod
from functools import lru_cache
from hashlib import md5
import uuid
import dataclasses
import inspect

import reflex as rx
from reflex import Component, Var, State
from reflex.constants import Hooks
from reflex.utils import imports, format
from reflex.vars import BaseVar, VarData
from reflex.event import EventHandler, EventSpec, EventChain

from .util import OrderedSet

my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, '.templates')

APP_ROUTER = False


def pretty_dumps(value: Any, indent=2) -> str:
    return format.json.dumps(value, ensure_ascii=False, default=format.serialize, indent=indent)


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

    def get_hooks(self) -> Set[str]:
        return set()

    def get_interpolations(self) -> List[Tuple[int, int]]:
        return []


class ExComponentItem(ExItem):
    item: Component

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Component)

    def serialize(self) -> str:
        return str(self.item)

    def get_imports(self) -> imports.ImportDict:
        return self.item.get_imports()

    def get_hooks(self) -> Set[str]:
        return self.item.get_hooks()


class JsEvent:
    hd: EventHandler

    def __init__(self, hd: EventHandler, *args):
        self.hd = hd
        self.args = args

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
            rs.append(f'{_arg}:{self.args[idx-1]}')
        return ','.join(rs)


js_event = JsEvent


class ExEventHandlerItem(ExItem):
    item: JsEvent

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, JsEvent)

    def _get_fn_name(self) -> str:
        return f"{self.key.replace('.', '_')}_{md5(self.key.encode('utf-8')).hexdigest()}"

    def serialize(self) -> str:
        return self._get_fn_name()

    def get_hooks(self) -> Set[str]:
        _hook = f"""const {self._get_fn_name()} = useCallback(({','.join(self.item.args)}) => addEvents(
        [Event("{self.item.get_state_full_name()}", {{ {self.item.get_event_args()} }})], 
        ({','.join(self.item.args)}), {{}}), [addEvents, Event]);
        """
        return {_hook}


class ExLambdaHandlerItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

    def _get_fn_name(self) -> str:
        return f"{self.key.replace('.', '_')}_{md5(self.key.encode('utf-8')).hexdigest()}"

    def get_event_triggers(self):
        return dict(hack=self.item)

    def serialize(self) -> str:
        return self._get_fn_name()

    def get_hooks(self) -> Set[str]:
        chain = self.parent._create_event_chain(self.key, self.item)
        rendered_chain = format.format_prop(chain).strip("{}")
        _hook = f"""const {self._get_fn_name()} = useCallback({rendered_chain}, [addEvents, Event]);"""
        return {_hook}


class ExCallableItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

    def serialize(self) -> str:
        return str(self.item())

    def get_imports(self) -> imports.ImportDict:
        return self.item().get_imports()

    def get_hooks(self) -> Set[str]:
        return self.item().get_hooks()


class ExStateItem(ExItem):
    item: BaseVar

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, BaseVar) and item._var_full_name.startswith("state__")

    def serialize(self) -> str:
        return self.item._var_full_name

    def get_imports(self) -> imports.ImportDict:
        return self.item._var_data.imports

    def get_hooks(self) -> Set[str]:
        return self.item._var_data.hooks

    def get_state(self) -> str:
        return self.item._var_data.state


class JsValue:
    def __init__(self, value: Union[str, Callable]):
        self.value = value
        self._init()

    def _init(self) -> None:
        pass

    def serialize(self) -> str:
        return self.value

    def get_imports(self) -> imports.ImportDict:
        return {}

    def get_state(self) -> str:
        return ''

    def get_hooks(self) -> Set[str]:
        return set()


class JsFunctionValue(JsValue):
    def _init(self) -> None:
        self._args = inspect.getfullargspec(self.value)
        args = self._args.args
        self._value = self.value(*args)

    def serialize(self) -> str:
        if isinstance(self._value, str):
            return f"""({','.join(self._args.args)}) => (
            {self._value}
            )
            """
        elif isinstance(self._value, Component):
            return f"""({','.join(self._args.args)}) => (
            {self._value}
            )
            """
        raise TypeError(self._value)

    def get_imports(self) -> imports.ImportDict:
        return {} if isinstance(self._value, str) else self._value.get_imports()

    def get_hooks(self) -> Set[str]:
        return set() if isinstance(self._value, str) else self._value.get_hooks()
        # return set(['const abc = 1;'])


def js_value(value: Union[str, Callable]) -> JsValue:
    if isinstance(value, str):
        return JsValue(value)
    if isinstance(value, Callable):
        return JsFunctionValue(value)
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

    def get_hooks(self) -> Set[str]:
        return self.item.get_hooks()


class ExFormatter:
    items: List[Type[ExItem]] = [
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
            return _v

        def _list(_v: List, pkey: str) -> List[Any]:
            return [_op(i, key=f'{pkey}.{idx}') for idx, i in enumerate(_v)]

        def _dict(_v: Dict, pkey: str) -> Dict[str, Any]:
            return dict((format.to_camel_case(k), _op(v, key=f'{pkey}.{k}')) for k, v in _v.items())

        rs = _op(value, key=self.name)
        self._value = rs

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

    def get_hooks(self) -> Set[str]:
        hooks = set()
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
    _var_value: Any = dataclasses.field(default=Any)


class NodeVar(ExVar):
    """
    support:
        . base types: int, float, bool, str
        . js, like: {show ? 11 : 0}
     """
    pass


class ContainVar(ExVar):

    @property
    def _var_full_name(self) -> str:
        return self._var_name

    @classmethod
    def create(cls, _args_: Any = None, **kwargs) -> Var | None:
        value = _args_ if _args_ is not None else kwargs
        # v: BaseVar = super().create(_name, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        return cls(
            _var_name='',
            _var_type=cls,
            _var_is_local=True,
            _var_is_string=False,
            _var_data=None,
            _var_value=value,
        )

    def init(self, parent: Component, name: str):
        fmt = ExFormatter(self._var_value, parent=parent, name=name)
        self._var_name = fmt.get_value()
        self._var_data = fmt.get_var_data()


contain = ContainVar.create


# no use
class VarDataMixin:
    def __iter__(self):
        v = Var()
        v._var_data = VarData(
            imports=self.get_imports(),
        )
        yield from [v]


class AntdBaseMixin:
    def _get_style(self) -> dict:
        """Get the style for the component.

        Returns:
            The dictionary of the component style as value and the style notation as key.
        """
        return {"style": self.style}

    def _get_hooks_internal(self) -> Set[str]:
        """Get the React hooks for this component managed by the framework.

        Downstream components should NOT override this method to avoid breaking
        framework functionality.

        Returns:
            Set of internally managed hooks.
        """
        # need order hooks, useContext code need first
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

    def _init_contains(self, contains: Dict[str, ContainVar]):
        for k, v in contains.items():
            v.init(self, k)
            setattr(self, k, v)


class AntdComponent(AntdBaseMixin, Component):
    """A component that wraps a Chakra component."""

    library = "antd"

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (160, "AntdProvider"): antd_provider,
        }

    def __init__(self, *args, **kwargs):
        contains = {}
        kw = {}
        for k,v in kwargs.items():
            if isinstance(v, ContainVar):
                contains[k] = v
            else:
                kw[k] = v
        super().__init__(*args, **kw)
        self._init_contains(contains)


class AntdSubComponent(AntdBaseMixin, Component):
    def _get_imports(self) -> imports.ImportDict:
        return {}


class AntdProvider(AntdComponent):
    """Top level antd provider must be included in any app using antd components."""

    tag = "ConfigProvider"
    alias = "AntdConfigProvider"

    theme: Var[str]

    @classmethod
    def create(cls) -> Component:
        """Create a new AntdProvider component.

        Returns:
            A new AntdProvider component.
        """
        return super().create(
            theme=Var.create("theme", _var_is_local=False),
        )

    def _get_imports(self) -> imports.ImportDict:
        _imports = super()._get_imports()
        _imports.setdefault("/utils/theme.js", []).append(
            imports.ImportVar(tag="theme", is_default=True),
        )
        return _imports

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        """ support app router """
        if APP_ROUTER:
            return {
                (170, "AntdRegistryProvider"): antd_registry_provider,
            }
        else:
            return {}


class AntdRegistryProvider(Component):
    library = "@ant-design/nextjs-registry"
    tag = "AntdRegistry"


antd_provider = AntdProvider.create()
antd_registry_provider = AntdRegistryProvider.create()


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
                    imports=value.get_imports(),
                    hooks=set(value.get_hooks()),
                )
            ]
        var_datas = old_extract_var_data(value)
        return var_datas

    vars._extract_var_data = _my_extract_var_data
