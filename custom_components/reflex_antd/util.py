from typing import List, Tuple, Any, Callable
import collections
import json

import reflex as rx
from reflex.utils import format


def dumps(data, **kwargs) -> str:
    return format.json_dumps(data, **kwargs)


loads = json.loads


def pretty_dumps(value: Any, indent=2, **kwargs) -> str:
    return format.json_dumps(value, indent=indent, **kwargs)


def switch(
        val: rx.Var,
        values: List[Tuple[Callable[[rx.Var, ], rx.Var] | str, rx.Component | Callable[..., rx.Component]]],
        default: rx.Component | Callable[..., rx.Component] = None,
) -> rx.Component | None:
    """
    chain cond, like:
    cond(condition1, com1,
        cond(condition2, com2,
            cond(condition3, com3, default)
        )
    )
     """
    conds = None
    for v in reversed(values):
        _op, _com = v
        _cond = _op(val) if callable(_op) else val == _op
        if conds is not None:
            conds = rx.cond(_cond, _com, conds)
        else:
            conds = rx.cond(_cond, _com, default)
    return conds


class OrderedSet(collections.abc.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

