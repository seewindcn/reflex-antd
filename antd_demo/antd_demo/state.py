from typing import List, Optional, Type
import inspect

import reflex as rx

from reflex_antd import general, helper

from antd_demo import layout as route


class MyBaseState(rx.State):
    @rx.var
    def current_url(self) -> str:
        return self.router.page.full_raw_path

    @rx.var
    def current_path(self) -> str:
        return self.router.page.path

    def get_route(self) -> route.Route:
        r = route.routes.get(self.router.page.path, None)
        return r

    async def get_base_state(self) -> Type[rx.state]:
        return await self.get_state(rx.State)

    async def get_global_state(self) -> Type["GlobalState"]:
        return await self.get_state(GlobalState)

    async def get_state_by(self, full_name: str) -> Type["MyBaseState"] | None:
        r = self.get_route()
        if not r:
            return
        path = full_name.split('.')
        bs = await self.get_base_state()
        ss = bs.get_substate(path)
        return ss


class GlobalState(MyBaseState):
    navbar_open_keys: List[str]
    navbar_selected_keys: List[str]
    subnav_items: list[dict[str, str]] = []

    icon: rx.Component = general.icon('InsertRowAboveOutlined')
    tooltip: str = 'abc'

    def update_subnav(self, path_urls: list[tuple[str, str] | list] = None) -> None:
        def _add(title, href):
            subnav_items.append(dict(title=title, href=href))

        subnav_items = []
        if path_urls:
            _add('Home', '/')
            for item in path_urls:
                _add(item[0], item[1])
        self.subnav_items = subnav_items

    async def on_page_load(self):
        self.update_subnav()
        r = self.get_route()
        if not r:
            return
        if r.state and hasattr(r.state, 'on_page_load'):
            s = await self.get_state(r.state)
            await getattr(s, 'on_page_load')()
        elif r.sub_on_load:
            path = r.sub_on_load.state_full_name.split('.')
            bs = await self.get_base_state()
            ss = bs.get_substate(path)

            if inspect.iscoroutinefunction(r.sub_on_load.fn):
                await r.sub_on_load.fn(ss)
            else:
                r.sub_on_load.fn(ss)

    def tooltip_click(self):
        """ https://babeljs.io/repl """
        if self.tooltip.startswith('abc'):
            if 0:
                self.tooltip = ("""
                    const a = React.createElement("a", null, "___ok...");
                    a.hidden = false;
                    a.href = '/ok';
                    return a;
                """)
            else:
                self.tooltip = ("""const op = () => {
                    const a = React.createElement("a", {
                      href: "/ok",
                      hidden: false,
                    }, " ---ok ~~~");
                    return a;
                }
                return op;
                """)

        else:
            self.tooltip = 'abc'

    def on_event0(self):
        print(f'on_event0')

    def on_event1(self, ev):
        print('on_event1', ev)

    def on_navbar_select(self, ev):
        print("navbar_selected_keys: ", ev)
        # self.navbar_selected_keys = ev['selected_keys']





