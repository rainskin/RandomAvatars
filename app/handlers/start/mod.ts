import answers from "answers"
import { saveChat } from "lib"
import { handlers } from "loader"

handlers.start((ctx) => {
  ctx.session.state = undefined
  saveChat(ctx)
  return ctx.r(answers.start(ctx.msg))
})

import("./menu/mod.ts")
