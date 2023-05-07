import { Command } from "enums"
import { AppContext, Handler as H } from "grammy_app"

type Session = { state?: string }
const session: Session = {}
const texts = { greet: "Hello!", count: "Count:" }
type Context = AppContext<Session, typeof texts>
const Handler = H<Context, Command>

export { Handler, session, texts }
export type { Command, Context }
