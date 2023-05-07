import { App } from "grammy_app"
import { session } from "types"

const app = new App(session)
const handlers = app.handlers

export { app, handlers }
