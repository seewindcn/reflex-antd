from os import path
import sys
import reflex as rx

my_path = path.dirname(path.realpath(__file__))
custom_components_path = path.join(path.dirname(my_path), '..', 'custom_components')
if path.exists(custom_components_path):
    sys.path.insert(0, custom_components_path)

from reflex_antd.helper import (
    patch_all, default_config, config_provider, antd_app, contain,
    Locale, theme, light_theme_var, dark_theme_var
)

patch_all()
theme_scheme = 'light' if 1 else 'dark'
app = rx.App(
    theme=rx.theme(
        appearance=theme_scheme,
    )
)
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
        if name == 'page404_page':
            app.add_custom_404_page(md.page404_page.component)
            continue

    for key, route in routes.items():
        if not load_all and key not in ['/', '/404', '/general']:
            continue
        route.add_page(app)


load_pages()
