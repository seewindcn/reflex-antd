from typing import Type, Any, Tuple, Dict, List, Iterable, Callable, Set, Union
from os import path
from abc import ABC, abstractmethod
from functools import lru_cache
import uuid
import dataclasses
import inspect

import reflex as rx
from reflex import Component, Var, State
from reflex.utils import imports, format
from reflex.vars import BaseVar, VarData

my_path = path.abspath(path.dirname(__file__))
template_path = path.join(my_path, '.templates')

APP_ROUTER = False


def pretty_dumps(value: Any, indent=2) -> str:
    return format.json.dumps(value, ensure_ascii=False, default=format.serialize, indent=indent)


class ExItem(ABC):
    @classmethod
    def isinstance(cls, item: Any) -> bool:
        pass

    def __init__(self, item: Any):
        self.item = item

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
        self. _init()

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
        ExComponentItem, ExCallableItem, ExStateItem,
        ExJsItem,
    ]

    def __init__(self, value: Any):
        self.value = value
        self._coms: Dict[str, ExItem] = {}
        self._value: Any = None
        self._extract()

    def _extract(self):
        value = self.value
        self._coms.clear()

        def _op(_v: Any):
            if isinstance(_v, (list, tuple)):
                return _list(_v)
            elif isinstance(_v, dict):
                return _dict(_v)
            elif isinstance(_v, (int, float, str, bool)):
                return _v

            _id = _v
            for ex in self.items:
                if ex.isinstance(_v):
                    _id = uuid.uuid4().hex
                    self._coms[_id] = ex(_v)
                    return _id
            return _v

        def _list(_v: List):
            return [_op(i) for i in _v]

        def _dict(_v: Dict):
            return dict((k, _op(v)) for k, v in _v.items())

        rs = _op(value)
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
    def create(
            cls, value: Any, _var_is_local: bool = True, _var_is_string: bool = False
    ) -> Var | None:
        fmt = ExFormatter(value)
        _name = fmt.get_value()
        # v: BaseVar = super().create(_name, _var_is_local=_var_is_local, _var_is_string=_var_is_string)
        return cls(
            _var_name=_name,
            _var_type=cls,
            _var_is_local=_var_is_local,
            _var_is_string=_var_is_string,
            _var_data=fmt.get_var_data(),
            _var_value=value,
        )


contains = ContainVar.create


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


class AntdComponent(AntdBaseMixin, Component):
    """A component that wraps a Chakra component."""

    library = "antd"

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (160, "AntdProvider"): antd_provider,
        }


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
    from reflex import constants
    from reflex.compiler import templates

    constants.Templates.Dirs.JINJA_TEMPLATE = [path.join(template_path, 'jinja'),
                                               constants.Templates.Dirs.JINJA_TEMPLATE]

    templates.DOCUMENT_ROOT = templates.get_template("web/pages/_document.js.jinja2")
