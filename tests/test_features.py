from asyncio import sleep
from collections.abc import AsyncGenerator
from typing import cast

import pytest
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@pytest.fixture(scope="session")
def app():
    a = Client(
        "userbot",
        session_string="AgAjVNwAumLgUQrK8O4iV-LeGYz43FLoVCnE1UVGKw7y1JWFzGRcsyeRfmgSr5T0HsRqoafA4I--MR3Hy0SzvNuNJ3LhhMTzLYU3Btygvaj7WIkRI6JbiUDjLi41zWke1pDVazqA3Vun-vud_zgH9K-nrvDDUxXkE8BmxrS91obZuZOgrI7RSdv-ntzpqPbrH7tmlrWJb-UpFWozWlkJQiLE4ufupXFsXNeWr07ZTJ82OKuW80F_VqM85Z2kJpfFxl2VjQxyQA71M_-RR1qoJvapxVgrK6qsY5ces26jBcV8nz86dEp5WyJRnF36DEWtJDgE23Eraibw2MCbGcV8K6-Jo7_t-QAAAAB2DH_rAA",
    )
    a.start()
    return a


@pytest.mark.asyncio()
async def test_start(app: Client):
    chat_id = "@anime_4bot"
    await app.send_message(chat_id, "/start")
    await sleep(0.5)
    m = await get_message(app, chat_id)
    assert m
    assert m.text == TEXT
    assert len(m.entities) == 1
    assert m.entities[0].user.is_self
    assert isinstance(m.reply_markup, InlineKeyboardMarkup)
    kb = m.reply_markup.inline_keyboard
    assert kb == KB
    print(m)


async def get_message(app: Client, chat_id: str):
    async for m in get_chat_history(app, chat_id, limit=1):
        assert not m.outgoing
        return m
    return None


async def get_chat_history(app: Client, chat_id: str, limit: int = 0):
    gen = cast(AsyncGenerator[Message, None], app.get_chat_history(chat_id, limit))
    async for m in gen:
        yield m


def callback_button(text: str):
    return InlineKeyboardButton(text, callback_data=text)


def url_button(text: str, url: str):
    return InlineKeyboardButton(text, url=url)


TEXT = """
⛩ Привет, Макс Соболь!

Я буду отправлять тебе аватарки и классные пикчи, которые ты сможешь использовать в своих диалогах 👌🏻

Добавляй меня в свой чат или начинай пользоваться прямо здесь 😉
""".strip()


KB = [
    [
        callback_button("⛩ Аниме авы"),
        callback_button("🎎 Парные аватарки"),
    ],
    [
        callback_button("💖 Милые пикчи"),
        callback_button("😡 Агрессивные"),
    ],
    [url_button("💬 Добавить в чат", "https://t.me/anime_4bot?startgroup=0")],
]
