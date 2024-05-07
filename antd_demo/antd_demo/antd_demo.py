from os import path
import sys
import reflex as rx

my_path = path.dirname(path.realpath(__file__))
custom_components_path = path.join(path.dirname(my_path), '..', 'custom_components')
if path.exists(custom_components_path):
    sys.path.insert(0, custom_components_path)

from reflex_antd.helper import patch_all, default_config, config_provider, Locale, theme

patch_all()
app = rx.App(
)

# config antd
default_config(config_provider(
    # locale=Locale('en_US'),
    locale=Locale(value='zh_CN'),
    theme=theme(
        token={
            'colorPrimary': '#00B96B',
            'colorPrimaryBg': '#e6f7ff',
            'colorLink': '#1890ff',
        },
        inherit=True,
    ),
))


def load_pages():
    from antd_demo.layout import load_modules, Route, routes
    from antd_demo import pages
    for md in load_modules(pages, is_pkg=False):
        name = f"{md.__name__.rsplit('.', 1)[-1]}_page"
        if name == 'page404_page':
            app.add_custom_404_page(md.page404_page.component)
            continue

    for key, route in routes.items():
        route.add_page(app)


load_pages()
