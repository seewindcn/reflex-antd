import reflex as rx


app = rx.App()


def load_pages():
    from antd_demo.layout import load_modules, Route
    from antd_demo import pages
    for md in load_modules(pages, is_pkg=False):
        name = f"{md.__name__.rsplit('.', 1)[-1]}_page"
        if name == 'page404_page':
            app.add_custom_404_page(md.page404_page.component)
            continue

        if hasattr(md, name):
            r: Route = getattr(md, name)
            r.add_page(app)
        if hasattr(md, 'pages'):
            pages = getattr(md, 'pages')
            pages(app)


load_pages()

