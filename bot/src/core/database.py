import mongoengine as me

from . import config

me.connect(
    db=config.MONGO_DB,
    host=config.MONGO_HOST,
    username=config.MONGO_USER,
    password=config.MONGO_PASSWORD,
)


class BaseDatabase:
    pass
