import answers from "answers"
import { kbs } from "assets"
import { PictureCategory } from "enums"
import { PictureRequest } from "lib"
import { handlers } from "loader"
import { Context } from "types"

function on(button: string, category: PictureCategory) {
  handlers.callbackQuery(button, (ctx) => onPictureRequest(ctx, category))
}

on(kbs.Menu.ANIME_AVATARS, "avatar")
on(kbs.Menu.PAIRED_AVATARS, "paired_avatars")
on(kbs.Menu.CUTE_PICTURES, "cute")
on(kbs.Menu.ANGRY_PICTURES, "angry")

import("./picture_menu.ts")

async function onPictureRequest(
  ctx: Context,
  category: PictureCategory,
) {
  const request = new PictureRequest(ctx)
  if (await request.respond(category)) {
    await ctx.r(answers.pictureMenu)
    // set_picture_category(query.from_user.id, category)
  }
}
