import logging

import config
from api import Api
from database import Database

logger = logging.getLogger()
db = Database()
api = Api(config.API_BASE_URL)
