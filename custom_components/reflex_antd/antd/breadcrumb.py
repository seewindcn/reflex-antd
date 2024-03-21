
from reflex import Var

from ..base import AntdComponent, ContainVar


class Breadcrumb(AntdComponent):
    tag = "Breadcrumb"

    items: Var[ContainVar]


breadcrumb = Breadcrumb.create
