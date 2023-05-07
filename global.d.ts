// deno-lint-ignore-file no-explicit-any
import * as deps from "deps"
import * as grammy from "grammy"
import * as tg from "tg"

declare global {
  type Message = tg.Message
  type User = tg.User
  type Chat = tg.Chat
  type Query = tg.CallbackQuery
  type ReplyMarkup =
    | tg.ReplyKeyboardMarkup
    | tg.InlineKeyboardMarkup
    | tg.ReplyKeyboardRemove
    | tg.ForceReply
}

declare global {
  const reply: typeof deps.r
  const Keyboard: typeof grammy.Keyboard
  const InlineKeyboard: typeof grammy.InlineKeyboard
}

declare global {
  interface String {
    format(vars: Record<string, any>): string
  }
}
