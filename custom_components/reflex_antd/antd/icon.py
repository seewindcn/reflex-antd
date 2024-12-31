from typing import Optional

from reflex import Component, Var
from reflex.utils import format


class BaseIconComponent(Component):
    library = "@ant-design/icons"


class IconComponent(BaseIconComponent):
    tag = "None"

    rotate: Optional[Var[int]]
    spin: Optional[Var[bool]]
    two_tone_color: Optional[Var[str]]

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


icon = IconComponent.create


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
