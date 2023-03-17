from telegram import KeyboardButton, InlineKeyboardButton
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, ForceReply

ReplyMarkup = ReplyKeyboardMarkup | InlineKeyboardMarkup | ReplyKeyboardRemove | ForceReply
AnyReplyButton = str | KeyboardButton
AnyInlineButton = str | InlineKeyboardButton
AnyButton = AnyReplyButton | AnyInlineButton
