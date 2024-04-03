from typing import List, Optional

import reflex as rx

from reflex_antd import general, helper


class GlobalState(rx.State):
    navbar_open_keys: List[str]
    navbar_selected_keys: List[str]

    icon: rx.Component = general.icon('InsertRowAboveOutlined')
    tooltip: str = 'abc'

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





