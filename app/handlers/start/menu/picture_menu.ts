// from botty import dp, Message, r
// import answers
// from assets import kbs
// from botty import dp, Message
// from api import get_picture_category
// from assets import kbs
// from lib import on_picture_request

// @dp.text(kbs.PictureMenu.GET_ANOTHER)
// async def _(msg: Message):
//     category = get_picture_category(msg.from_user.id)
//     await on_picture_request(msg, category)

// @dp.text(kbs.PictureMenu.BACK)
// def _(msg: Message):
//     return r(msg, answers.start(msg))
