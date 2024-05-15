from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Optional, Union, Dict, Any, List
from reflex import Var, Component
from reflex.constants import EventTriggers
from ..base import AntdComponent, ContainVar, JsValue, js_value, ReactNode
from ..constant import StatusType

class Transfer(AntdComponent):

    @overload
    @classmethod
    def create(cls, *children, data_source: Optional[Union[Var[List], List]]=None, disabled: Optional[Union[Var[bool], bool]]=None, selections_icon: Optional[Union[Var[Union[str, Component]], Union[str, Component]]]=None, filter_option: Optional[Union[Var[JsValue], JsValue]]=None, footer: Optional[Union[Var[JsValue], JsValue]]=None, list_style: Optional[Union[Var[Union[Dict, JsValue]], Union[Dict, JsValue]]]=None, locale: Optional[Union[Var[Union[Dict, ContainVar]], Union[Dict, ContainVar]]]=None, one_way: Optional[Union[Var[bool], bool]]=None, operations: Optional[Union[Var[List[str]], List[str]]]=None, operation_style: Optional[Union[Var[Dict], Dict]]=None, pagination: Optional[Union[Var[Union[ContainVar, bool]], Union[ContainVar, bool]]]=None, item_render: Optional[Union[Var[Union[JsValue, ContainVar]], Union[JsValue, ContainVar]]]=None, row_key: Optional[Union[Var[JsValue], JsValue]]=None, select_all_labels: Optional[Union[Var[JsValue], JsValue]]=None, selected_keys: Optional[Union[Var[List[str]], List[str]]]=None, show_search: Optional[Union[Var[bool], bool]]=None, showSelect_all: Optional[Union[Var[bool], bool]]=None, status: Optional[Union[Var[Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']], Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']]]=None, target_keys: Optional[Union[Var[List[str]], List[str]]]=None, titles: Optional[Union[Var[ContainVar], ContainVar]]=None, _custom_components: Optional[Set[CustomComponent]]=None, style: Optional[Style]=None, key: Optional[Any]=None, id: Optional[Any]=None, class_name: Optional[Any]=None, autofocus: Optional[bool]=None, custom_attrs: Optional[Dict[str, Union[Var, str]]]=None, on_blur: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_context_menu: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_double_click: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_focus: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_down: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_move: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_out: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_over: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_mouse_up: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_scroll: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_search: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_select_change: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, on_unmount: Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]=None, **props) -> 'Transfer':
        """"""
        ...

    def get_event_triggers(self) -> Dict[str, Any]:
        ...
transfer = Transfer.create