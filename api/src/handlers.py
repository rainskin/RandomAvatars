import random
import time

import config
from database import models
from enums import PictureCategory, ChatType
from loader import db, app


@app.get('/picture/{category}')
def get_picture(category: PictureCategory, chat_id: int) -> list[str]:
    pictures = db.get_pictures(category, chat_id)
    picture: models.Picture = random.choice(pictures)
    db.save_sent_picture(chat_id, picture)
    return picture.photo_ids


@app.get('/cooldown/{user_id}')
def get_cooldown(user_id: int, chat_type: ChatType) -> dict:
    user = db.get_user(user_id)

    delta = int(time.time() - user.last_request_time)
    remaining_time = max(0, config.REQUEST_COOLDOWN - delta)

    if chat_type == ChatType.PRIVATE:
        remaining_time = 0

    return {'remaining_time': remaining_time}


@app.post('/cooldown/{user_id}')
def set_cooldown(user_id: int) -> dict:
    user = db.get_user(user_id)
    user.save_last_request_time(time.time())
    return {'ok': True}
