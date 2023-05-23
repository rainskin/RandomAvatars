import re
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

import botty
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InputMediaPhoto,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.utils.markdown import hlink
from botty import CallbackButton, FSMContext, Message, Query, UrlButton, dp


def mention(name: str, user_id: int) -> str:
    return hlink(name, f"tg://user?id={user_id}")


def inline_keyboard(*buttons: CallbackButton | UrlButton, row_width: int = 1):
    return InlineKeyboardMarkup(row_width).add(*buttons)


def reply_keyboard(*buttons: str, row_width: int = 1):
    return ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True).add(*buttons)


AsyncFunc = Awaitable[Any]
MessageCallback = (
    Callable[[Message], AsyncFunc] | Callable[[Message, FSMContext], AsyncFunc]
)
MessageHandler = Callable[[MessageCallback], MessageCallback]


def on_start(payload_prefix: str | None = None) -> MessageHandler:
    payload = re.compile(f"^{payload_prefix}.+") if payload_prefix else None
    f = CommandStart(deep_link=payload)
    return dp.message_handler(f, state="*")  # type: ignore[TODO]


@dataclass
class Answer(botty.Answer):
    photo: str | list[str] | None = None


def r(event: Message | Query, answer: Answer):
    if not answer.photo:
        return botty.r(event, answer)
    msg = event if isinstance(event, Message) else event.message
    if isinstance(answer.photo, list):
        media = [InputMediaPhoto(p) for p in answer.photo]
        media[0].caption = answer.text
        return msg.answer_media_group(media)  # type: ignore[TODO]
    markup = answer.markup
    if isinstance(markup, bool):
        markup = ReplyKeyboardRemove()
    return msg.answer_photo(answer.photo, answer.text, reply_markup=markup)


def e(query: Query, answer: Answer):
    if not answer.photo:
        return botty.e(query, answer)
    if isinstance(answer.photo, list):
        _ = f"Bad photo: {answer.photo}"
        raise TypeError(_)
    markup = answer.markup
    if not isinstance(markup, InlineKeyboardMarkup):
        _ = f"Bad markup: {markup}"
        raise TypeError(_)
    media = InputMediaPhoto(answer.photo, answer.text)
    return query.message.edit_media(media, reply_markup=markup)
