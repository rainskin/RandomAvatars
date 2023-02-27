from lib.assets import PictureCategory
from core.constants import *
from .picture_category_picker import PictureCategoryPicker
from .picture_request import PictureRequest


async def respond(request: REQUEST):
    category = PictureCategoryPicker(request).pick()

    if category:
        await respond_picture(request, category)


def respond_picture(request: REQUEST, category: PictureCategory):
    return PictureRequest(request, category).respond()
