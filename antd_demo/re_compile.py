import sys
from os import environ
import time


environ['PYDANTIC_SKIP_VALIDATING_CORE_SCHEMAS'] = 'true'
environ['REFLEX_ENV_MODE'] = 'prod'

print('----------load')
start_time = time.time()
from reflex import reflex, app, constants
from reflex.utils import prerequisites
print('----------loaded', time.time() - start_time)


# load custom packages

app.App._get_frontend_packages = lambda *args, **kwargs: None


def re_compile():
    app_module = prerequisites.get_app(reload=False)
    app = getattr(app_module, constants.CompileVars.APP)
    _ = app._should_compile()
    _ = app._should_compile()
    prerequisites.get_compiled_app()
    print('done')


if __name__ == '__main__':
    re_compile()


