import warnings
from abc import ABC

from telegram import BotCommand, BotCommandScopeChat, InputMediaPhoto
from telegram.error import TelegramError
from telegram.ext import ApplicationHandlerStop, ExtBot
from telegram.helpers import create_deep_linked_url

from core.keyboards import ReplyMarkup
from . import layer1
from ..helpers import get_reply_markup
from ..types import ReplyKeyboard


class Handler(layer1.Handler, ABC):

    @property
    def bot(self) -> ExtBot:
        return self.context.bot

    @property
    def text(self) -> str | None:
        if message := self.message:
            return message.text

    def reply(self, text: str, keyboard: ReplyKeyboard = ...):
        markup = get_reply_markup(keyboard)
        return self.message.reply_text(text, reply_markup=markup)

    def reply_photo(self, photo: str):
        return self.message.reply_photo(photo)

    def reply_photos(self, photos: list[str]):
        if not photos:
            raise ValueError('No photos')

        if len(photos) == 1:
            return self.reply_photo(photos[0])

        media = [InputMediaPhoto(i) for i in photos]
        return self.message.reply_media_group(media)

    def edit(self, text: str, markup: ReplyMarkup = None):
        return self.message.edit_text(text, reply_markup=markup)

    async def cancel(self, text: str, keyboard: ReplyKeyboard = ...):
        await self.reply(text, keyboard)
        raise ApplicationHandlerStop()

    async def set_my_commands(self, commands: list[BotCommand], chat_id: int = None):
        scope = BotCommandScopeChat(chat_id) if chat_id else None
        try:
            await self.bot.set_my_commands(commands, scope)
        except TelegramError as e:
            warnings.warn(f"Can't set commands for chat `{chat_id}`: {e}")

    def get_start_url(self, payload: str = None, group: bool = False) -> str:
        username = self.bot.username
        return create_deep_linked_url(username, payload, group)

    def get_chat(self, chat_id: int):
        return self.bot.get_chat(chat_id)

    @property
    def startgroup_url(self) -> str:
        return self.get_start_url('0', group=True)

    @property
    def user_mention(self) -> str:
        return self.user.mention_html()

    async def obtain_invite_link(self, chat_id: int) -> str:
        chat = await self.get_chat(chat_id)

        if not chat.invite_link:
            link = await chat.create_invite_link()
            chat.invite_link = link.invite_link

        return chat.invite_link

    def get_chat_member(self, chat_id: int):
        return self.bot.get_chat_member(chat_id, self.user.id)

    async def is_chat_member(self, chat_id: int) -> bool:
        try:
            member = await self.get_chat_member(chat_id)
        except TelegramError as e:
            print(e)  # TODO: test
            return False

        return member.status not in [member.LEFT, member.BANNED]

    @property
    def is_chat_private(self) -> bool:
        return self.chat.type == self.chat.PRIVATE

    @property
    def is_chat_group(self) -> bool:
        return self.chat.type in [self.chat.GROUP, self.chat.SUPERGROUP]

    @property
    def admin_ids(self) -> list[int]:
        return self.context.bot_data.get('admin_ids', [])

    @property
    def is_user_admin(self) -> bool:
        return self.user.id in self.admin_ids

    async def set_commands(self, for_users: list[BotCommand], for_admins: list[BotCommand]):
        await self.set_my_commands(for_users)

        for admin_id in self.admin_ids:
            await self.set_my_commands(for_admins, admin_id)

    @property
    def command(self) -> str | None:
        prefix = '/'
        text = self.text

        if text.startswith(prefix):
            return text.removeprefix(prefix).split('@')[0]
