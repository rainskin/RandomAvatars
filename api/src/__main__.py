import random

import uvicorn

from database import models
from enums import PictureCategory
from loader import db, app


@app.get('/picture/{category}')
def get_picture(category: PictureCategory) -> list[str]:
    pictures = db.get_pictures(category)
    picture: models.Picture = random.choice(pictures)
    return picture.photo_ids


uvicorn.run(app, host='0.0.0.0', log_level=30)
