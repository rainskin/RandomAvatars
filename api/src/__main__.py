import uvicorn

import config
from handlers import app

uvicorn.run(
    app,
    host=config.HOST,
    port=config.PORT,
    log_level=config.LOG_LEVEL,
)
