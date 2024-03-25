from typing import List

import reflex as rx


class GlobalState(rx.State):
    navbar_open_keys: List[str]
    navbar_selected_keys: List[str]

    def on_event0(self):
        print(f'on_event0')

    def on_event1(self, ev):
        print('on_event1', ev)

    def on_navbar_select(self, ev):
        print("navbar_selected_keys: ", ev)
        # self.navbar_selected_keys = ev['selected_keys']





