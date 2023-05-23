from botty import dp

import handlers
from lib import set_commands

handlers.setup()
dp.run(set_commands())
