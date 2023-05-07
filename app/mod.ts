// @deno-types="../global.d.ts"
import "$"
import "handlers"
import { setCommands } from "lib"
import { app, handlers } from "loader"

setCommands()
app.run(handlers)
