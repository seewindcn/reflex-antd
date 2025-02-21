from os import path
import sys
import random
import reflex as rx

my_path = path.dirname(path.realpath(__file__))
custom_components_path = path.join(path.dirname(my_path), '..', 'custom_components')
if path.exists(custom_components_path):
    sys.path.insert(0, custom_components_path)

from reflex_antd.helper import (
    patch_all,
    default_config, config_provider, antd_app, contain,
    Locale, theme, light_theme_var, dark_theme_var
)

patch_all()
theme_scheme = 'light' if 1 else 'dark'


async def patch_after_start_lifespan_hack():
    from reflex_antd.base import patch_after_start
    patch_after_start()


class MyApp(rx.App):
    def __post_init__(self):
        super().__post_init__()
        self.register_lifespan_task(patch_after_start_lifespan_hack)

    @classmethod
    def init_antd(cls):
        """ for support dynamic ant-design
        1. patch_after_start_lifespan_hack
        2. dynamic.bundle_library
        3. base.random seek freeze
         """
        from reflex.components import dynamic
        for lib in [
            'antd',
            '@ant-design/icons',
            # '@ant-design/nextjs-registry',
            # '@ant-design/charts',  # charts no support
        ]:
            dynamic.bundle_library(lib)

    def _compile(self, *args, **kwargs):
        from reflex.vars import base
        _my_random = random.Random(123321)  # make get_unique_variable_name in clear random queue
        try:
            _my_random.abc = 1
            base.random = _my_random
            return super()._compile(*args, **kwargs)
        finally:
            base.random = random
            # random.seed()  # 去掉固定种子, 保证随机


app = MyApp(
    theme=rx.theme(
        appearance=theme_scheme,
    )
)
app.init_antd()
antd_theme_scheme = light_theme_var if theme_scheme == 'light' else dark_theme_var

# config antd
default_config(
    provider=config_provider(
        locale=Locale('en_US'),
        # locale=Locale(value='zh_CN'),
        theme=theme(
            algorithm=antd_theme_scheme,
            token={
                'colorPrimary': '#00B96B',
                'colorPrimaryBg': '#e6f7ff',
                'colorLink': '#1890ff',
            },
            inherit=True,
        ),
    ),
    antd_app=antd_app(
        message=contain(max_count=5),
        notification=contain(
            placement="topRight",
            duration=5, max_count=5,
            stack=dict(threshold=5),
            show_progress=True, pause_on_hover=True),
    ),
)


def load_pages():
    from antd_demo.layout import load_modules, Route, routes
    from antd_demo import pages
    load_all = True
    for md in load_modules(pages, is_pkg=False):
        name = f"{md.__name__.rsplit('.', 1)[-1]}_page"
        # if name == 'page404_page':
        #     app.add_custom_404_page(md.page404_page.component)
        #     continue

    for key, route in routes.items():
        if not load_all and key not in ['/', '/404', '/general']:
            continue
        route.add_page(app)


load_pages()
