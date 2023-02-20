import logging

import httpx

from database import Database

logger = logging.getLogger()
db = Database()
client = httpx.AsyncClient()
