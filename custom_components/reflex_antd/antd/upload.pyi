from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue

class Upload(AntdComponent):

    def get_event_triggers(self) -> Dict[str, Any]:
        ...

    @overload
    @classmethod
    def create(cls, *children, accept: Optional[Union[Var[str], str]]=None, action: Optional[Union[Var[Union[str, JsValue]], Union[str, JsValue]]]=None, before_upload: Optional[Union[Var[JsValue], JsValue]]=None, custom_request: Optional[Union[Var[JsValue], JsValue]]=None, data: Optional[Union[Var[Union[ContainVar, JsValue]], Union[ContainVar, JsValue]]]=None, default_file_list: Optional[Union[Var[List[ContainVar]], List[ContainVar]]]=None, directory: Optional[Union[Var[bool], bool]]=None, disabled: Optional[Union[Var[bool], bool]]=None, file_list: Optional[Union[Var[List[ContainVar]], List[ContainVar]]]=None, headers: Optional[Union[Var[Dict], Dict]]=None, icon_render: Optional[Union[Var[JsValue], JsValue]]=None, is_image_url: Optional[Union[Var[JsValue], JsValue]]=None, list_type: Optional[Union[Var[str], str]]=None, max_count: Optional[Union[Var[int], int]]=None, method: Optional[Union[Var[str], str]]=None, multiple: Optional[Union[Var[bool], bool]]=None, name: Optional[Union[Var[str], str]]=None, open_file_dialog_on_click: Optional[Union[Var[bool], bool]]=None, preview_file: Optional[Union[Var[JsValue], JsValue]]=None, progress: Optional[Union[Var[Dict], Dict]]=None, show_upload_list: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]]=None, with_credentials: Optional[Union[Var[bool], bool]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_download: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_drop: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_preview: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_remove: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Upload':
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...
upload = Upload.create