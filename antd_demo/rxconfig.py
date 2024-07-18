import os
from os import environ
import reflex as rx
from reflex import constants
from reflex.utils import processes, exec

environ['FRONTEND_PORT'] = '3001'
environ['BACKEND_PORT'] = '8001'


def dev_run_backend(
    host: str,
    port: int,
    loglevel: constants.LogLevel = constants.LogLevel.ERROR,
):
    """debug but don't reload; Run the backend.

    Args:
        host: The app host
        port: The app port
        loglevel: The log level.
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
    yield


if environ.get("DEV_NO_RELOAD", False):
    processes.is_process_on_port = lambda port: False
    exec.run_backend = dev_run_backend
    from reflex.utils import compat
    compat.windows_hot_reload_lifespan_hack = _disable


config = rx.Config(
    app_name="antd_demo",
    tailwind=dict(
        corePlugins=dict(
            preflight=False,
        ),
    ),
)

