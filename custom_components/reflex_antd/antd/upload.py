from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue


class Upload(AntdComponent):
    tag = 'Upload'

    accept: Var[str]
    action: Var[Union[str, JsValue]]
    before_upload: Var[JsValue]
    custom_request: Var[JsValue]
    data: Var[Union[ContainVar, JsValue]]
    default_file_list: Var[List[ContainVar]]
    directory: Var[bool]
    disabled: Var[bool]
    file_list: Var[List[ContainVar]]
    headers: Var[Dict]
    icon_render: Var[JsValue]
    is_image_url: Var[JsValue]
    list_type: Var[str]
    max_count: Var[int]
    method: Var[str]
    multiple: Var[bool]
    name: Var[str]
    open_file_dialog_on_click: Var[bool]
    preview_file: Var[JsValue]
    progress: Var[Dict]
    show_upload_list: Var[Union[bool, Dict]]
    with_credentials: Var[Union[bool]]

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda file, file_list,event: [file, file_list,event],
            "on_drop": lambda event: [event],
            "on_download": lambda file: [file],
            "on_preview": lambda file: [file],
            "on_remove": lambda file: [file]
        })
        return _triggers


upload = Upload.create

