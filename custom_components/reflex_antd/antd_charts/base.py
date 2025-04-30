from typing import Optional, Union, Any, Dict, Sequence
import reflex as rx
from reflex.utils import imports, types

from ..base import Var, BaseModel, Base, ExTypes, ContainVar, AntdNoSSRComponent, AntdBaseComponent, ReactNode, PropBase
from . import g6


class ChartBase(AntdNoSSRComponent):
    """
    https://github.com/ant-design/ant-design-charts
    """
    library = '@ant-design/charts'


class GraphBase(g6.G6BaseComponent):
    """
    https://ant-design-charts.antgroup.com/options/graphs/overview

    **注意:
        react18,如果开启了 StrictMode , 会在dev时进行两次渲染:
            https://react.dev/blog/2022/03/08/react-18-upgrade-guide#updates-to-strict-mode
        g6 会引起 runtime 错误 instance 被重复释放:
            https://g6.antv.vision/manual/getting-started/integration/react
            https://github.com/ant-design/ant-design-charts/issues/1554

        graphs.js 想用于修复这个问题, 不过不熟悉前端, 解决不了; 只能修改 rxconfig.py(react_strict_mode=False)
    """
    # library = '@ant-design/graphs'
    _custom_js = 'graphs.js'
    library = '/components/antd/graphs'
    lib_dependencies: list[str] = ["@ant-design/graphs", ]

    # data 数据。关于图数据的详细说明
    # node 节点，支持 G6 内置节点
    node: Optional[Var[g6.G6Node]]
    # edge 边，支持 G6 内置边
    edge: Optional[Var[g6.G6Edge]]
    # combo 支持 G6 内置 Combo
    # layout 布局，支持 G6 内置布局

    # behaviors 设置用户交互事件
    behaviors: Optional[Var[ExTypes | dict]]

    # plugins 设置插件
    # transforms 设置数据处理
    # theme 主题

    def get_event_triggers(self) -> Dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            "on_init": lambda g: [g],
            "on_ready": lambda g: [g],
            "on_destroy": lambda: [],
            'on_click': lambda e: [e],
        })
        return _triggers

    def add_imports(self) -> imports.ImportDict | list[imports.ImportDict]:
        _imports: imports.ImportDict = super().add_imports()
        _imports = imports.merge_imports(_imports, {
            self.library: [
                imports.ImportVar(tag='RCNode'),
            ],
        })
        return _imports

    def _get_hooks(self) -> str | None:
        return "const { TextNode } = RCNode;"
