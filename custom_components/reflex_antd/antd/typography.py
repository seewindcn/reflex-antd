from typing import Optional, Union, Dict, Any, List, Tuple

from reflex import Component, Var
from reflex.utils import imports
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue
from ..constant import TypographyTextType


class TypographyBase(AntdComponent):
    code: Optional[Var[bool]]
    copyable: Optional[Var[Union[bool, ContainVar]]]
    delete: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    editable: Optional[Var[Union[bool, ContainVar]]]
    ellipsis: Optional[Var[Union[bool, ContainVar]]]

    mark: Optional[Var[bool]]
    italic: Optional[Var[bool]]
    type: Optional[Var[TypographyTextType]]
    underline: Optional[Var[bool]]

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

    keyboard: Optional[Var[bool]]
    strong: Optional[Var[bool]]


class TypographyTitle(TypographyBase):
    tag = 'Typography.Title'

    level: Optional[Var[int]]


class TypographyParagraph(TypographyBase):
    tag = 'Typography.Paragraph'

    strong: Optional[Var[bool]]


class Typography(AntdComponent):
    tag = 'Typography'


typography = Typography.create
typography_text = TypographyText.create
typography_title = TypographyTitle.create
typography_paragraph = TypographyParagraph.create

