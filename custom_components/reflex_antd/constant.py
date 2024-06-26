from typing import Literal


ThemeType = Literal["light", "dark"]
PlacementType = Literal["start", "end", "bottom", "bottomLeft", "bottomRight", "top", "topLeft", "topRight"]
AlignType = Literal["start", "end", "center", "baseline", "left", "right"]
OrientationType = Literal["left", "right", "top", "bottom", "center"]
DirectionType = Literal["vertical", "horizontal", "inline"]
SizeType = Literal["default", "small", "medium", "middle", "large"]
StatusType = Literal['default', 'success', 'error', 'warning', 'info', 'exception', 'normal', 'active']
TriggerType = Literal["click", "hover", "focus", 'contextMenu']
VariantType = Literal['outlined', 'borderless', 'filled']
TypeType = Literal['default', 'primary', 'dashed', 'link', 'text']
RoleType = Literal['alert', 'status']
BreakpointType = Literal['xs', 'sm', 'md', 'lg', 'xl', 'xxl']

ColorFormatType = Literal['rgb', 'hex', 'hsb']

ButtonShape = Literal['default', 'circle', 'round']

TypographyTextType = Literal['secondary', 'success', 'warning', 'danger']

FloatGroupShapeType = Literal["circle", "square"]

BadgeStatusType = Literal["success", 'processing', 'default', 'error', 'warning']

StepsStatusType = Literal['wait', 'process', 'finish', 'error']
StepsType = Literal['default', 'navigation', 'inline']

DatePickerModeType = Literal['time', 'date', 'month', 'year', 'decade']
DatePickerType = Literal['date', 'week', 'month', 'quarter', 'year']

RadioStyleType = Literal['outline', 'solid']
RadioType = Literal['default', 'button']

SelectModeType = Literal['multiple', 'tags']

ProgressType = Literal['line', 'circle', 'dashboard']

TimelineModeType = Literal['left', 'alternate', 'right']

TabsType = Literal['line', 'card', 'editable-card']

QRCodeType = Literal['canvas', 'svg']
QRCodeErrorLevelType = Literal['L', 'M', 'Q', 'H']
QRCodeStatusType = Literal['active', 'expired', 'loading', 'scanned']

MessageType = Literal['info', 'success', 'error', 'loading', 'warning']
