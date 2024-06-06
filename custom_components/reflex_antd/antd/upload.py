from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers

from ..base import AntdComponent, ContainVar, JsValue


class Upload(AntdComponent):
    tag = 'Upload'

    accept: Optional[Var[str]]
    action: Optional[Var[Union[str, JsValue]]]
    before_upload: Optional[Var[JsValue]]
    custom_request: Optional[Var[JsValue]]
    data: Optional[Var[Union[ContainVar, JsValue]]]
    default_file_list: Optional[Var[List[ContainVar]]]
    directory: Optional[Var[bool]]
    disabled: Optional[Var[bool]]
    file_list: Optional[Var[List[ContainVar]]]
    headers: Optional[Var[Dict]]
    icon_render: Optional[Var[JsValue]]
    is_image_url: Optional[Var[JsValue]]
    list_type: Optional[Var[str]]
    max_count: Optional[Var[int]]
    method: Optional[Var[str]]
    multiple: Optional[Var[bool]]
    name: Optional[Var[str]]
    open_file_dialog_on_click: Optional[Var[bool]]
    preview_file: Optional[Var[JsValue]]
    progress: Optional[Var[Dict]]
    show_upload_list: Optional[Var[Union[bool, Dict]]]
    with_credentials: Optional[Var[Union[bool]]]

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

