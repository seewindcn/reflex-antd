from typing import Optional, Union, Any, Dict
import reflex as rx
from reflex import Var
from reflex_antd.helper import ContainVar, AntdNoSSRComponent, AntdBaseComponent


class ChartBase(AntdNoSSRComponent):
    """
    https://github.com/ant-design/ant-design-charts
    """
    library = '@ant-design/charts'
