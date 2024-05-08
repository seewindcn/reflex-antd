import reflex as rx

config = rx.Config(
    app_name="antd_demo",
    tailwind=dict(
        corePlugins=dict(
            preflight=False,
        ),
    ),
)

