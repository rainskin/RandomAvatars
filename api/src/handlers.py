import random
import time

import config
from database import models
from database.models import Chat
from enums import PictureCategory, ChatType
from loader import db, app

JSON = list | str | int | bool


def make_response(result: JSON) -> dict:
    return {'result': result}


OK = make_response(True)


@app.get('/picture/{category}')
def get_picture(category: PictureCategory, chat_id: int):
    pictures = db.get_pictures(category, chat_id)
    picture: models.Picture = random.choice(pictures)
    db.save_sent_picture(chat_id, picture)
    return make_response(picture.photo_ids)


@app.get('/cooldown/{user_id}')
def get_cooldown(user_id: int, chat_type: ChatType):
    user = db.get_user(user_id)

    delta = int(time.time() - user.last_request_time)
    remaining_time = max(0, config.REQUEST_COOLDOWN - delta)

    if chat_type == ChatType.PRIVATE:
        remaining_time = 0

    return make_response(remaining_time)


@app.post('/cooldown/{user_id}')
def set_cooldown(user_id: int):
    user = db.get_user(user_id)
    user.save_last_request_time(time.time())
    return OK


@app.get('/picture-category/{user_id}')
async def get_picture_category(user_id: int):
    user = db.get_user(user_id)
    return make_response(user.picture_category)


@app.post('/picture-category/{user_id}')
async def set_picture_category(user_id: int, category: PictureCategory):
    user = db.get_user(user_id)
    user.save_picture_category(category)
    return OK


@app.get('/chats')
async def get_chats():
    chat_ids = [c.id for c in Chat().find_docs()]
    return make_response(chat_ids)


@app.post('/chats/{chat_id}')
async def save_chat(chat_id: int):
    Chat.find_doc(id=chat_id) or Chat(id=chat_id).save()
    return OK
