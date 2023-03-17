from core import keyboards

AnyKeyboard = keyboards.Keyboard | type[keyboards.Keyboard]
AnyInlineKeyboard = keyboards.Inline | type[keyboards.Inline]
ReplyKeyboard = AnyKeyboard | None
