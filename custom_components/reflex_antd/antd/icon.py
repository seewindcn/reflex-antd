from typing import Optional

from reflex import Component, Var, ImportVar
from reflex.utils import format, imports
from ..base import AntdComponent


class BaseIconComponent(Component):
    library = "@ant-design/icons"


class IconComponent(BaseIconComponent):
    tag = "None"

    rotate: Var[int]
    spin: Var[bool]
    two_tone_color: Var[str]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Initialize the Icon component.
        """
        if children:
            if len(children) == 1 and type(children[0]) == str:
                props["tag"] = children[0]
                children = []
            else:
                raise AttributeError(
                    f"Passing multiple children to Icon component is not allowed: remove positional arguments {children[1:]} to fix"
                )
        if "tag" not in props.keys():
            raise AttributeError("Missing 'tag' keyword-argument for Icon")

        # if (
        #     type(props["tag"]) != str
        #     or format.to_snake_case(props["tag"]) not in LUCIDE_ICON_LIST
        # ):
        #     raise ValueError(
        #         f"Invalid icon tag: {props['tag']}. Please use one of the following: {', '.join(LUCIDE_ICON_LIST[0:25])}, ..."
        #         "\nSee full list at https://lucide.dev/icons."
        #     )

        # props["tag"] = format.to_title_case(format.to_snake_case(props["tag"]))
        # props["alias"] = f"antd{props['tag']}"
        return super().create(*children, **props)


class DynamicIcon(BaseIconComponent):
    """ dynamic icon """
    alias = 'Icon'

    icon: Var[str]  # icon str, like: 'QuestionCircleOutlined', 'CheckCircleOutlined'
    rotate: Var[int]
    spin: Var[bool]
    two_tone_color: Var[str]

    def add_custom_code(self) -> list[str]:
        return [
            """
        import * as icons from '@ant-design/icons';
        const Icon = (props) => {
            const { icon, ..._props } = props;
            const antIcon = icons;
            if (!icon) {
                return createElement(antIcon['QuestionCircleOutlined']);
            }
            return createElement(antIcon[icon], _props);
        };
            """
        ]

    def add_imports(self) -> dict[str, str | ImportVar | list[str | ImportVar]]:
        return {
            "react": [imports.ImportVar(tag="createElement")],
        }


icon = IconComponent.create
dynamic_icon = DynamicIcon.create

# class CustomerServiceOutlined(BaseIconComponent):
#     tag = 'CustomerServiceOutlined'
#
#
# class CommentOutlined(BaseIconComponent):
#     tag = 'CommentOutlined'
#
#
# class QuestionCircleOutlined(BaseIconComponent):
#     tag = 'QuestionCircleOutlined'
#
#
# class LaptopOutlined(BaseIconComponent):
#     tag = 'LaptopOutlined'
#
#
# class NotificationOutlined(BaseIconComponent):
#     tag = 'NotificationOutlined'
#
#
# class CloseCircleOutlined(BaseIconComponent):
#     tag = 'CloseCircleOutlined'
#
#
# class CloseSquareOutlined(BaseIconComponent):
#     tag = 'CloseSquareOutlined'
#
#
# class UserOutlined(BaseIconComponent):
#     tag = 'UserOutlined'
