from typing import Literal


ThemeType = Literal["light", "dark"]
PlacementType = Literal["start", "end"]
AlignType = Literal["start", "end", "center", "baseline"]
OrientationType = Literal["left", "right", "top", "bottom", "center"]
DirectionType = Literal["vertical", "horizontal"]
SizeType = Literal["default", "small", "medium", "middle", "large"]
StatusType = Literal['default', 'error', 'warning']

MenuModeType = Literal["vertical", "horizontal", 'inline']

ButtonType = Literal['default', 'primary']
ButtonShape = Literal['default', 'circle', 'round']


FloatGroupTriggerType = Literal["click", "hover"]
FloatGroupShapeType = Literal["circle", "square"]

BadgeStatusType = Literal["success", 'processing', 'default', 'error', 'warning']
