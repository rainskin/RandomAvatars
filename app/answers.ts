import { texts } from "api/texts.ts"
import { kbs } from "assets"
import { getMention, Msg, startGroupUrl } from "deps"
import { app } from "loader"
// from api import Text, Sign
// from assets import kbs

class Answers {
  greetGroup = new Msg(texts.greetGroup)
  menu = (user: User) =>
    new Msg(
      texts.greet(getMention(user)),
      new kbs.Menu(startGroupUrl(app)),
    )
  start(msg: Message) {
    return msg.chat.type == "private" ? this.menu(msg.from!) : this.greetGroup
  }
  doesNotWork = new Msg(texts.doesNotWork)
  pictureMenu = new Msg(texts.pictureMenuHint, kbs.pictureMenu)
}

const answers = new Answers()
export default answers

// def utm(key_count: dict[str, int]):
//     strings = [f"{bold(k)}: {c}" for k, c in key_count.items()]
//     return Answer("\n".join(strings), kbs.CANCEL)

// def wait_for(seconds: int):
//     return Answer(Text.WAIT_FOR.format(seconds=seconds))

// def join_required(url: str):
//     return Answer(Text.JOIN_REQUIRED.format(url=url))

// def required_join(invite_link: str | None = None):
//     if invite_link:
//         text = Text.REQUIRED_JOIN.format(invite_link)
//     else:
//         text = Text.REQUIRED_JOIN_DISABLED
//     return Answer(text, kbs.RequiredJoin(not invite_link))

// def sign(s: Sign):
//     return Answer(s.text, kbs.SignMenu(s.str_id))

// ADMIN_MENU = Answer(Text.ADMIN_PANEL, kbs.ADMIN_MENU)
// ASK_POST = Answer(Text.ASK_POST, kbs.CANCEL)
// BROADCAST_START = Answer(Text.BROADCAST_START)
// REQUIRED_JOIN = required_join()
// ASK_CHANNEL_POST = Answer(Text.ASK_CHANNEL_POST, kbs.CANCEL)
// FORWARD_ERROR = Answer(Text.FORWARD_ERROR)
// RIGHTS_ERROR = Answer(Text.RIGHTS_ERROR)
// ASK_RIGHTS = Answer(Text.ASK_RIGHTS)
// SIGNS = Answer(Text.ADMIN_PANEL, kbs.SIGNS)
// ASK_SIGN = Answer(Text.ASK_SIGN, kbs.CANCEL)
