import logging
from typing import List, Any, Dict, Set
import asyncio
import random
import math
from datetime import datetime, timedelta

import reflex as rx
from reflex import State, Var

from reflex_antd import helper, display, general, entry, layout, feedback, pro, charts

from antd_demo.layout import page


class DashboardState(State):
    # 基础数据
    visits_data: List[Dict[str, Any]] = [
        {"x": f"2023-{i}", "y": random.randint(1000, 9000)} for i in range(1, 13)
    ]
    
    sales_data: List[Dict[str, Any]] = [
        {"x": f"2023-{i}", "y": random.randint(5000, 20000)} for i in range(1, 13)
    ]
    
    conversion_data: List[Dict[str, Any]] = [
        {"x": f"2023-{i}", "y": random.randint(10, 30)} for i in range(1, 13)
    ]
    
    # 饼图数据
    pie_data: List[Dict[str, Any]] = [
        {"type": "分类一", "value": 27},
        {"type": "分类二", "value": 25},
        {"type": "分类三", "value": 18},
        {"type": "分类四", "value": 15},
        {"type": "分类五", "value": 10},
        {"type": "其他", "value": 5},
    ]
    
    # 表格数据
    table_data: List[Dict[str, Any]] = [
        {
            "key": i,
            "name": f"项目 {i}",
            "owner": f"用户 {i % 5 + 1}",
            "status": random.choice(["进行中", "已完成", "已暂停"]),
            "updatedAt": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
            "progress": random.randint(0, 100),
        }
        for i in range(1, 6)
    ]
    
    # 活动数据
    activities: List[Dict[str, Any]] = [
        {
            "user": f"用户{i}",
            "action": random.choice(["创建了任务", "完成了任务", "评论了任务", "修改了文档"]),
            "target": f"「项目{random.randint(1, 10)}」",
            "time": f"{random.randint(1, 59)}分钟前",
        }
        for i in range(1, 8)
    ]
    
    # 待办事项
    todos: List[Dict[str, Any]] = [
        {"title": "完成产品设计", "done": False},
        {"title": "客户需求分析", "done": True},
        {"title": "开发任务分配", "done": False},
        {"title": "项目进度汇报", "done": False},
        {"title": "代码审查", "done": True},
    ]
    
    # 切换待办事项状态
    def toggle_todo(self, index: int):
        self.todos[index]["done"] = not self.todos[index]["done"]


def _ui_overview_cards() -> rx.Component:
    """顶部概览卡片"""
    return layout.row(
        layout.col(
            pro.statistic_card(
                title="总访问量",
                value="234,231",
                suffix="次",
                chart=charts.tiny_line(
                    data=DashboardState.visits_data,
                    height=60,
                    auto_fit=True,
                    smooth=True,
                ),
                footer=rx.text("日均: 1,234"),
            ),
            span=6,
        ),
        layout.col(
            pro.statistic_card(
                title="销售额",
                value="¥ 126,560",
                chart=charts.tiny_area(
                    data=DashboardState.sales_data,
                    height=60,
                    auto_fit=True,
                    smooth=True,
                ),
                footer=rx.text("周同比: +15%"),
            ),
            span=6,
        ),
        layout.col(
            pro.statistic_card(
                title="转化率",
                value="25.6%",
                chart=charts.tiny_column(
                    data=DashboardState.conversion_data,
                    height=60,
                    auto_fit=True,
                ),
                footer=rx.text("月环比: +2.1%"),
            ),
            span=6,
        ),
        layout.col(
            pro.statistic_card(
                title="活跃用户",
                value="12,821",
                suffix="人",
                chart=charts.tiny_area(
                    data=DashboardState.visits_data,
                    height=60,
                    auto_fit=True,
                    smooth=True,
                ),
                footer=rx.text("周活跃: 9,432"),
            ),
            span=6,
        ),
        gutter=16,
    )


def _ui_charts_section() -> rx.Component:
    """图表区域"""
    return layout.row(
        layout.col(
            pro.pro_card(
                charts.column(
                    data=DashboardState.sales_data,
                    x_field="x",
                    y_field="y",
                    label=helper.contain({"position": "middle"}),
                    title=helper.contain({"text": "月度销售额"}),
                    height=300,
                ),
                title="销售趋势",
                bordered=True,
            ),
            span=16,
        ),
        layout.col(
            pro.pro_card(
                charts.pie(
                    data=DashboardState.pie_data,
                    angle_field="value",
                    color_field="type",
                    radius=0.8,
                    label=helper.contain({"type": "outer"}),
                    height=300,
                ),
                title="销售分布",
                bordered=True,
            ),
            span=8,
        ),
        gutter=16,
        style={"marginTop": "16px"},
    )


def _ui_project_table() -> rx.Component:
    """项目表格"""
    return pro.pro_card(
        pro.pro_table(
            columns=helper.contain([
                {"title": "项目名称", "dataIndex": "name", "key": "name"},
                {"title": "负责人", "dataIndex": "owner", "key": "owner"},
                {"title": "状态", "dataIndex": "status", "key": "status", 
                 "render": helper.js_value(lambda record: 
                    display.tag(
                        record["status"],
                        color="green" if record["status"] == "已完成" else 
                              "blue" if record["status"] == "进行中" else "orange"
                    )
                 )},
                {"title": "更新时间", "dataIndex": "updatedAt", "key": "updatedAt"},
                {"title": "进度", "dataIndex": "progress", "key": "progress",
                 "render": helper.js_value(lambda record: 
                    entry.progress(percent=record["progress"], size="small")
                 )},
            ]),
            dataSource=DashboardState.table_data,
            pagination=helper.contain({"pageSize": 5}),
            search=False,
            options=False,
        ),
        title="项目列表",
        bordered=True,
        style={"marginTop": "16px"},
    )


def _ui_activity_and_todo() -> rx.Component:
    """活动和待办事项"""
    return layout.row(
        layout.col(
            pro.pro_card(
                display.list(
                    data_source=DashboardState.activities,
                    render_item=helper.js_value(lambda item: 
                        display.list_item(
                            display.list_item_meta(
                                avatar=display.avatar(icon=general.icon("UserOutlined")),
                                title=rx.text(f"{item['user']} {item['action']} {item['target']}"),
                                description=rx.text(item["time"]),
                            )
                        )
                    ),
                ),
                title="动态",
                bordered=True,
            ),
            span=16,
        ),
        layout.col(
            pro.pro_card(
                display.list(
                    data_source=DashboardState.todos,
                    render_item=helper.js_value(lambda item, index: 
                        display.list_item(
                            layout.space(
                                entry.checkbox(
                                    checked=item["done"],
                                    on_change=lambda e, i=index: DashboardState.toggle_todo(i),
                                ),
                                rx.text(
                                    item["title"],
                                    decoration="line-through" if item["done"] else "none",
                                ),
                                align="center",
                            )
                        )
                    ),
                    header=rx.text("待办事项"),
                    footer=general.button("添加任务", type="dashed", block=True, icon=general.icon("PlusOutlined")),
                ),
                title="待办事项",
                bordered=True,
            ),
            span=8,
        ),
        gutter=16,
        style={"marginTop": "16px"},
    )


# @page('/dashboard', 'dashboard')
def dashboard_page11() -> rx.Component:
    """Dashboard 主页面"""
    return rx.box(
        layout.page_header(
            title="数据看板",
            sub_title="实时数据分析与监控",
            extra=layout.space(
                general.button("今日", type="default"),
                general.button("本周", type="default"),
                general.button("本月", type="default"),
                general.button("全年", type="primary"),
                size="small",
            ),
        ),
        _ui_overview_cards(),
        _ui_charts_section(),
        _ui_project_table(),
        _ui_activity_and_todo(),
        padding="24px",
    )