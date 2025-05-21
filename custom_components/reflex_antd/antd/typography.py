from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import TypographyTextType


class TypographyBase(AntdComponent):
    code: Var[bool]
    copyable: Var[Union[bool, ContainVar]]
    delete: Var[bool]
    disabled: Var[bool]
    editable: Var[Union[bool, ContainVar]]
    ellipsis: Var[Union[bool, dict, ContainVar]]

    mark: Var[bool]
    italic: Var[bool]
    type: Var[TypographyTextType]
    underline: Var[bool]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CLICK: lambda ev: [ev],
            'copyable.on_copy': lambda ev: [ev],
            'editable.on_change': lambda s: [s],
            'editable.on_cancel': lambda: [],
            'editable.on_start': lambda: [],
            'editable.on_end': lambda: [],
            'ellipsis.on_expand': lambda ev, info: [ev, info],
            'ellipsis.on_ellipsis': lambda ellipsis: [ellipsis],
        })
        return _triggers


class TypographyText(TypographyBase):
    tag = 'Typography.Text'

    keyboard: Var[bool]
    strong: Var[bool]


class TypographyTitle(TypographyBase):
    tag = 'Typography.Title'

    level: Var[int]


class TypographyParagraph(TypographyBase):
    tag = 'Typography.Paragraph'

    strong: Var[bool]


class Typography(AntdComponent):
    tag = 'Typography'


typography = Typography.create
typography_text = TypographyText.create
typography_title = TypographyTitle.create
typography_paragraph = TypographyParagraph.create

