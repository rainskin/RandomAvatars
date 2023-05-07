// from botty import Message, User, r, obtain_invite_link

import { PictureCategory } from "enums"
import { saveChat } from "../helpers.ts"
import { Context } from "types"

// import answers
// from api import PictureCategory, get_cooldown, get_picture
// from lib.helpers import save_chat
// from .required_join import RequiredJoin
// from .response import Response

export function onPictureRequest(ctx: Context, category: PictureCategory) {
  return new PictureRequest(ctx).respond(category)
}

export class PictureRequest {
  _picture: string[] = []
  private chat

  constructor(private ctx: Context) {
    this.chat = ctx.chat!
  }

  async respond(category: PictureCategory): Promise<boolean> {
    saveChat(this.ctx)
    await this.ctx.reply(category)
    return true
    //         if chat_id := await RequiredJoin(self._chat, self._user_id).get_chat_id():
    //             await self._ask_to_join_chat(chat_id)
    //             return False

    //         if cooldown := get_cooldown(self._user_id, self._chat.type):
    //             await self._ask_wait(cooldown)
    //             return False

    //         picture = get_picture(category, self._chat.id)
    //         resp = Response(picture, self._message, self._user_id)
    //         return await resp.send()
  }
}

//     async function _ask_to_join_chat(self, chat_id: int):
//         invite_link = await obtain_invite_link(chat_id)
//         await r(self._message, answers.join_required(invite_link))

//     function _ask_wait(self, cooldown: int):
//         return r(self._message, answers.wait_for(cooldown), quote=True)
