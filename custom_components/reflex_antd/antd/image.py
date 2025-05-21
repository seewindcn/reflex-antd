from typing import Optional, Union, Dict, Any, List

from reflex import Component, Var

from ..base import AntdComponent, ContainVar, JsValue, ReactNode


class Image(AntdComponent):
    tag = 'Image'

    alt: Var[str]
    fallback: Var[str]
    height: Var[Union[str, int]]
    placeholder: Var[ReactNode]
    description: Var[ReactNode]
    preview: Var[Union[bool, dict]]
    src: Var[str]
    width: Var[Union[str, int]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()

        _triggers.update({
            "on_error": lambda event: [],
        })
        return _triggers


class ImagePreviewGroup(AntdComponent):
    tag = 'Image.PreviewGroup'

    preview: Var[Union[bool, Component]]
    items: Var[list]
    fallback: Var[str]


image = Image.create
image_preview_group = ImagePreviewGroup.create
