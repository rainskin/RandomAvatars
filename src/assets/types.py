from typing import Literal

PictureCategory = Literal["avatar", "paired_avatars", "cute", "angry"]

Command = Literal[
    "start",
    "get_avatars",
    "get_paired",
    "get_cute",
    "get_angry",
    "send_picture",
    "admin",
]
