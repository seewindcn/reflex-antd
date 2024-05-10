
from reflex import State, Var

from .base import JsValue


def hook_state(state_field: Var | str, on_update: str, on_null: str = '') -> str:
    state = state_field
    if isinstance(state_field, Var):
        state = str(state_field).strip('{}')
    s = """useEffect(() => {
    if (%(state)s === null) { %(on_null)s }
    else { %(on_update)s }
  }, [%(state)s]) """ % dict(
        state=state,
        on_update=on_update,
        on_null=on_null,
    )
    return s
