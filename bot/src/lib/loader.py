import logging

import config
from lib.api import Api

logger = logging.getLogger()
api = Api(config.API_BASE_URL)
