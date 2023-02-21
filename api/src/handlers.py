import random
import time

from pydantic import BaseModel

import config
from core import make_response, OK
from database import models
from enums import PictureCategory, ChatType
from loader import db, app


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
    remaining_time = max(0, config.PICTURE_REQUEST_COOLDOWN - delta)

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
    chat_ids = [c.id for c in db.get_chats()]
    return make_response(chat_ids)


@app.post('/chats/{chat_id}')
async def save_chat(chat_id: int):
    db.save_chat(chat_id)
    return OK


@app.get('/required-join/chat')
async def get_required_join_chat():
    chat = db.get_required_join_chat()
    return make_response(chat)


class RequiredJoinChat(BaseModel):
    chat_id: int | None


@app.post('/required-join/chat')
async def set_required_join_chat(chat: RequiredJoinChat):
    db.set_required_join_chat(chat.chat_id)
    return OK
