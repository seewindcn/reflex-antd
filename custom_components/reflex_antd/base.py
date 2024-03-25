from typing import Type, Any, Tuple, Dict, List, Iterable, Callable
from os import path
from abc import ABC, abstractmethod
from functools import lru_cache
import uuid
import dataclasses

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


class ExComponentItem(ExItem):
    item: Component

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Component)

    def serialize(self) -> str:
        return str(self.item)

    def get_imports(self) -> imports.ImportDict:
        return self.item.get_imports()


class ExCallableItem(ExItem):
    item: Callable

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, Callable)

    def serialize(self) -> str:
        return str(self.item())

    def get_imports(self) -> imports.ImportDict:
        c = self.item()
        return c.get_imports()


class ExStateItem(ExItem):
    item: State

    @classmethod
    def isinstance(cls, item: Any) -> bool:
        return isinstance(item, BaseVar) and item._var_full_name.startswith("state__")

    def serialize(self) -> str:
        return self.item._var_full_name


class ExFormatter:
    items: List[Type[ExItem]] = [
        ExComponentItem, ExCallableItem, ExStateItem,
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
            _var_data=VarData(
                imports=fmt.get_imports(),
            ),
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
