import config
from core import app
from handlers import HANDLERS

app.add_handlers(HANDLERS)
app.run(config.ADMIN_IDS)
