from typing import Literal


ThemeType = Literal["light", "dark"]
PlacementType = Literal["start", "end", "bottom", "bottomLeft", "bottomRight", "top", "topLeft", "topRight"]
AlignType = Literal["start", "end", "center", "baseline"]
OrientationType = Literal["left", "right", "top", "bottom", "center"]
DirectionType = Literal["vertical", "horizontal"]
SizeType = Literal["default", "small", "medium", "middle", "large"]
StatusType = Literal['default', 'error', 'warning']
TriggerType = Literal["click", "hover"]
VariantType = Literal['outlined', 'borderless', 'filled']

ColorFormatType = Literal['rgb', 'hex', 'hsb']

MenuModeType = Literal["vertical", "horizontal", 'inline']

ButtonType = Literal['default', 'primary']
ButtonShape = Literal['default', 'circle', 'round']


FloatGroupShapeType = Literal["circle", "square"]

BadgeStatusType = Literal["success", 'processing', 'default', 'error', 'warning']

StepsStatusType = Literal['wait', 'process', 'finish', 'error']
StepsType = Literal['default', 'navigation', 'inline']


