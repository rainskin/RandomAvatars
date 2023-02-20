import random
import time

import config
from database import models
from database.models import Chat
from enums import PictureCategory, ChatType
from loader import db, app


@app.get('/picture/{category}')
def get_picture(category: PictureCategory, chat_id: int) -> list[str]:
    pictures = db.get_pictures(category, chat_id)
    picture: models.Picture = random.choice(pictures)
    db.save_sent_picture(chat_id, picture)
    return picture.photo_ids


@app.get('/cooldown/{user_id}')
def get_cooldown(user_id: int, chat_type: ChatType):
    user = db.get_user(user_id)

    delta = int(time.time() - user.last_request_time)
    remaining_time = max(0, config.REQUEST_COOLDOWN - delta)

    if chat_type == ChatType.PRIVATE:
        remaining_time = 0

    return {'remaining_time': remaining_time}


@app.post('/cooldown/{user_id}')
def set_cooldown(user_id: int):
    user = db.get_user(user_id)
    user.save_last_request_time(time.time())
    return {'ok': True}


@app.get('/picture-category/{user_id}')
async def get_picture_category(user_id: int):
    user = db.get_user(user_id)
    return {'category': user.picture_category}


@app.post('/picture-category/{user_id}')
async def set_picture_category(user_id: int, category: PictureCategory):
    user = db.get_user(user_id)
    user.save_picture_category(category)
    return {'ok': True}


@app.get('/chats')
async def get_chats() -> list[int]:
    return [c.id for c in Chat().find_docs()]
