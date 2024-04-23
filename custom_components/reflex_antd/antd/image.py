from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Image(AntdComponent):
    tag = 'Image'

    alt: Optional[Var[str]]
    fallback: Optional[Var[str]]
    height: Optional[Var[Union[str, int]]]
    placeholder: Optional[Var[ReactNode]]
    description: Optional[Var[ReactNode]]
    preview: Optional[Var[Union[bool, dict]]]
    src: Optional[Var[str]]
    width: Optional[Var[Union[str, int]]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            "on_error": lambda event: [],
        })
        return _triggers


class ImagePreviewGroup(AntdComponent):
    tag = 'Image.PreviewGroup'

    preview: Optional[Var[Union[bool, Component]]]
    items: Optional[Var[list]]
    fallback: Optional[Var[str]]


image = Image.create
image_preview_group = ImagePreviewGroup.create
