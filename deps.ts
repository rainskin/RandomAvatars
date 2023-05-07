import { Bot } from "grammy"
import { Msg } from "grammy_r"
import { parse as parseYAML } from "std/yaml/parse.ts"
import { User } from "tg"

function format(text: string, vars: Record<string, string>) {
  for (const key in vars) {
    text = text.replace(`{${key}}`, vars[key])
  }
  return text
}

const textsYaml = await Deno.readTextFile("texts.yml")
const texts = parseYAML(textsYaml) as Record<string, string | undefined>

function t(key: string) {
  const value = texts[key]
  if (value == null) throw new Error("Text not found")
  return value
}

function getMention(user: User) {
  return link(user.first_name, `tg://user?id=${user.id}`)
}

function link(text: string, url: string) {
  return `<a href="${url}">${text}</a>`
}

function startGroupUrl(_bot: Bot) {
  return `https://t.me/${_bot.botInfo.username}?startgroup=0`
}

export { format, getMention, link, Msg, startGroupUrl, t }
