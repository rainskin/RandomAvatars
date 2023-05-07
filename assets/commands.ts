import { BotCommand } from "tg"
import { Command } from "enums"

function C(cmd: Command, text: string): BotCommand {
  return { command: cmd, description: text }
}

class Groups {
  FOR_USERS = [
    C("start", "Главное меню"),
    C("get_avatars", "Получить аватарку"),
    C("get_paired", "Получить парные аватарки"),
    C("get_cute", "Получить милую пикчу"),
    C("get_angry", "Получить агрессивную пикчу"),
    C("send_picture", "Отправить пикчу пользователю"),
  ]
  FOR_ADMINS = this.FOR_USERS.concat([
    C("admin", "Админ-панель"),
  ])
}

export const groups = new Groups()
