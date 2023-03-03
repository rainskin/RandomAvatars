from assets import PictureCategory
from core import *
from .picture_category_picker import PictureCategoryPicker
from .picture_request import PictureRequest


async def on_text(event: EVENT):
    category = PictureCategoryPicker(event).pick()

    if category:
        await respond_picture(event, category)


def respond_picture(request: EVENT, category: PictureCategory):
    return PictureRequest(request, category).respond()
