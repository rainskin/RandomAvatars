// deno-lint-ignore-file no-explicit-any
import * as deps from "deps"
import * as grammy from "grammy"

const _ = globalThis as any

_.reply = deps.r
_.Keyboard = grammy.Keyboard
_.InlineKeyboard = grammy.InlineKeyboard

String.prototype.format = function (
  this: string,
  vars: Record<string, any>,
) {
  let text
  for (const key in vars) {
    text = this.replaceAll(`{${key}}`, vars[key].toString())
  }
  return text || this
}
