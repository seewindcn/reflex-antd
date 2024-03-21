from typing import Optional, Union, Type, Dict, List, Any
from pydantic import BaseModel
from reflex import Component, Var
from reflex.utils import imports

from ..base import AntdComponent, AntdSubComponent, ContainVar
from ..constant import ThemeType, MenuModeType


class MenuItem(BaseModel):
    key: str
    label: str
    icon: Component
    children: Optional[List["MenuItem"]] = None


class MenuItems(ContainVar):
    pass


class Menu(AntdComponent):
    tag = 'Menu'

    theme: Optional[Var[ThemeType]]
    mode: Optional[Var[MenuModeType]]

    items: Var[Union[MenuItems, List[MenuItem], List[dict]]]


menu = Menu.create
menu_items = MenuItems.create
