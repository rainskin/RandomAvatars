from lib.assets import PictureCategory
from .picture_category_picker import PictureCategoryPicker
from .picture_request import PictureRequest
from core.constants import *


async def on_any_request(request: REQUEST):
    category = PictureCategoryPicker(request).pick()

    if category:
        await respond_picture(request, category)


def respond_picture(request: REQUEST, category: PictureCategory):
    return PictureRequest(request, category).respond()
