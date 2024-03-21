from typing import List

import reflex as rx


class GlobalState(rx.State):
    navbar_open_keys: List[str]
    navbar_selected_keys: List[str]

    def on_navbar_select(self, ev):
        print("navbar_selected_keys: ", ev)
        # self.navbar_selected_keys = ev['selected_keys']





