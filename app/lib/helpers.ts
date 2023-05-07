import { app } from "loader"
import { Context } from "types"

// import random
// from contextlib import suppress

// from aiogram.types import BotCommandScopeChat
// from botty import bot, TelegramAPIError, User, Message

// import api
// from api import ADMIN_IDS, Sign
// from assets import commands

async function setCommands() {
  await app.api.setMyCommands([])
  // await bot.set_my_commands(commands.Groups.FOR_USERS);
  //     for admin_id in ADMIN_IDS:
  //         with suppress(TelegramAPIError):
  //             scope = BotCommandScopeChat(admin_id)
  //             await bot.set_my_commands(commands.Groups.FOR_ADMINS, scope)
}

// def is_admin(user: User):
//     return user.id in ADMIN_IDS

function saveChat(ctx: Context) {
  const utm = ctx.match || null
  console.log("New chat by:", utm) // TODO
  //   return api.save_chat(msg.chat.id, utm)
}

export { saveChat, setCommands }

// def get_random_sign() -> str | None:
//     signs = [s.text for s in Sign.find_all()]
//     return random.choice(signs) if signs else None
