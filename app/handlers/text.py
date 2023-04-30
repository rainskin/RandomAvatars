from botty import dp, Message

from api import PictureCategory, TriggerWords
from lib import on_picture_request


@dp.TEXT
async def _(msg: Message):
    if category := pick_category(msg):
        await on_picture_request(msg, category)


def pick_category(msg: Message) -> PictureCategory | None:
    words = msg.text.lower().split()
    for word in words:
        for category, triggers in TRIGGERS_BY_CATEGORY.items():
            if word in triggers:
                return category


TRIGGERS_BY_CATEGORY = {
    PictureCategory.AVATAR: TriggerWords.avatar,
    PictureCategory.PAIRED_AVATARS: TriggerWords.paired_avatars,
    PictureCategory.CUTE: TriggerWords.cute_picture,
    PictureCategory.ANGRY: TriggerWords.angry_picture,
}
