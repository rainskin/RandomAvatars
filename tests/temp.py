import json
from copy import deepcopy
from datetime import datetime
from typing import cast

from pyrogram.client import Client
from pyrogram.enums import UserStatus
from pyrogram.types import Message

import snapshots

a = Client(
    "userbot",
    session_string="AgAjVNwAumLgUQrK8O4iV-LeGYz43FLoVCnE1UVGKw7y1JWFzGRcsyeRfmgSr5T0HsRqoafA4I--MR3Hy0SzvNuNJ3LhhMTzLYU3Btygvaj7WIkRI6JbiUDjLi41zWke1pDVazqA3Vun-vud_zgH9K-nrvDDUxXkE8BmxrS91obZuZOgrI7RSdv-ntzpqPbrH7tmlrWJb-UpFWozWlkJQiLE4ufupXFsXNeWr07ZTJ82OKuW80F_VqM85Z2kJpfFxl2VjQxyQA71M_-RR1qoJvapxVgrK6qsY5ces26jBcV8nz86dEp5WyJRnF36DEWtJDgE23Eraibw2MCbGcV8K6-Jo7_t-QAAAAB2DH_rAA",
)
a.start()  # type: ignore[TODO]
_ = [*a.get_chat_history("@anime_4bot", limit=1)]  # type: ignore[TODO]
message = cast(Message, _[0])

DATETIME = datetime(2023, 1, 1)


def snapshot(msg: Message):
    msg = deepcopy(msg)
    msg.id = 1
    msg.date = DATETIME
    msg.photo = None
    for e in msg.entities or []:
        if e.user:
            e.user.status = UserStatus.OFFLINE
            e.user.last_online_date = DATETIME
    return msg


r = snapshot(message)
d = {}


a = json.loads(str(r))
assert a == snapshots.GET_AVATARS
