import warnings

from telegram.constants import ParseMode
from telegram.ext import Application, Defaults, PicklePersistence, ExtBot

from . import config
from .handlers import Handlers, HandlerClass

warnings.filterwarnings('ignore', "If 'per_message=False'")
warnings.filterwarnings('ignore', "`Application` instances should be")

DEFAULTS = Defaults(
    parse_mode=ParseMode.HTML,
    disable_web_page_preview=True,
)

PERSISTENCE_FILE = '.persistence'
PERSISTENCE = PicklePersistence(PERSISTENCE_FILE)

AdminIds = list[int]


class App:

    def __init__(self, bot_token: str):
        self.raw = self._build(bot_token)
        self.admin_ids: AdminIds = []

    def _build(self, bot_token: str) -> Application:
        builder = Application.builder()
        builder.token(bot_token).defaults(DEFAULTS).concurrent_updates(True)
        builder.persistence(PERSISTENCE).post_init(self.post_init)
        return builder.build()

    async def post_init(self, application: Application):
        application.bot_data.update(admin_ids=self.admin_ids)  # TODO

    def add_handlers(self, handlers: Handlers):
        for h in handlers:
            self.add_handler(h)

    def add_handler(self, handler: HandlerClass):
        self.raw.add_handler(handler.build())

    def run(self, admin_ids: AdminIds):
        self.admin_ids = admin_ids
        self.raw.run_polling()

    @property
    def bot(self) -> ExtBot:
        return self.raw.bot


app = App(config.BOT_TOKEN)
