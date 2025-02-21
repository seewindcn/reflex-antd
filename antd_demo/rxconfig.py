import os
from os import environ
import reflex as rx
from reflex import constants
from reflex.utils import processes, exec


if environ.get('DEBUG', None):
    environ['FRONTEND_PORT'] = '3001'
    environ['BACKEND_PORT'] = '8101'


def dev_run_backend(
    host: str,
    port: int,
    loglevel: constants.LogLevel = constants.LogLevel.ERROR,
    frontend: bool = False,
):
    """debug but don't reload; Run the backend.
    """
    from reflex.config import get_config
    import uvicorn

    config = get_config()
    app_module = f"reflex.app_module_for_backend:{constants.CompileVars.APP}"

    # Create a .nocompile file to skip compile for backend.
    if os.path.exists(constants.Dirs.WEB):
        with open(constants.NOCOMPILE_FILE, "w"):
            pass

    # Run the backend in development mode.
    uvicorn.run(
        app=f"{app_module}.{constants.CompileVars.API}",
        host=host,
        port=port,
        log_level=loglevel.value,
        reload=False,  # disable reload
        reload_dirs=[config.app_name],
        reload_excludes=[constants.Dirs.WEB],
    )


async def _disable():
    ...


if environ.get("DEV_NO_RELOAD", False):
    processes.is_process_on_port = lambda port: False
    exec.run_backend = dev_run_backend
    from reflex.utils import compat
    compat.windows_hot_reload_lifespan_hack = _disable

variants = ['hover', 'focus']
corePlugins = {
    "preflight": False,
}
safelist = [  # global css, no purge
    # {"pattern": r"/(justify|content|items|self|place)-[\w-]+/", "variants": variants},
    # {"pattern": r"/(basis|flex|grow|shrink|order|grid|col|row|gap)-[\w-]+/", "variants": variants},
    # {"pattern": r"/(p|px|py|ps|pe|pt|pb|pl|pr)-[\w-]+/", "variants": variants},
    # {"pattern": r"/(m|mx|my|ms|me|mt|mb|ml|mr)-[\w-]+/", "variants": variants},
    {"pattern": r"/(static|fixed|absolute|relative|sticky|visible|invisible|collapse)/", "variants": variants},
    {"pattern": r"/(top|left|right|bottom)-[\w]+/", "variants": variants},
    {"pattern": r"/(resize|resize-[\w-]+)/", "variants": variants},
    {"pattern": r"/(shadow|shadow-[\w-]+)/", "variants": variants},
    {"pattern": r"/(z-[\w-]+)/", "variants": variants},
    {
      "pattern": r"/bg-(red|green|blue|gray|indigo|violet|purple)-(50|100|300)/",
      "variants": variants,
    },
]

config = rx.Config(
    app_name="antd_demo",
    tailwind={
        "headers": [
            "const colors = require('tailwindcss/colors')",
        ],
        "theme": {
            "extend": {},
            "colors": "'colors'",
        },
        "plugins": ["@tailwindcss/typography"],
        "corePlugins": corePlugins,
        "safelist": safelist,
        # "important": True,
        # "prefix": "tw-",
        # "separator": "_",
    }
)

