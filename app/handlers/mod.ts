import answers from "answers"
import { handlers } from "loader"

import("./start/mod.ts")
handlers.command("send_picture", (ctx) => ctx.r(answers.doesNotWork))
