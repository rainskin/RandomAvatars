import "$"

// from botty import InlineKeyboard, UrlButton, CallbackButton, ReplyKeyboard

// BACK_BUTTON = CallbackButton("🔙 Назад")

// export class Menu extends InlineKeyboard {
export class Menu extends InlineKeyboard {
  static ANIME_AVATARS = "⛩ Аниме авы"
  static PAIRED_AVATARS = "🎎 Парные аватарки"
  static CUTE_PICTURES = "💖 Милые пикчи"
  static ANGRY_PICTURES = "😡 Агрессивные"

  constructor(startGroupUrl: string) {
    super()
    this
      .text(Menu.ANIME_AVATARS).text(Menu.PAIRED_AVATARS).row()
      .text(Menu.CUTE_PICTURES).text(Menu.ANGRY_PICTURES).row()
      .url("💬 Добавить в чат", startGroupUrl)
  }
}

export class PictureMenu extends Keyboard {
  static GET_ANOTHER = "♻️ Ещё"
  static BACK = "🔙 Меню"

  constructor() {
    super()
    this.text(PictureMenu.GET_ANOTHER).text(PictureMenu.BACK).resized()
  }
}

export const pictureMenu = new PictureMenu()

// class AdminMenu(InlineKeyboard):
//     BROADCAST = CallbackButton("📩 Рассылка")
//     REQUIRED_JOIN = CallbackButton("✅ Обязательная подписка")
//     UTM = CallbackButton("🏷 UTM (Рефералы)")
//     SIGNS = CallbackButton("✍️ Подписи")

//     buttons = [BROADCAST, REQUIRED_JOIN, UTM, SIGNS]

// class Signs(InlineKeyboard):
//     ADD = CallbackButton("Добавить подпись")
//     SHOW = CallbackButton("Просмотреть подписи")

//     buttons = [ADD, SHOW, BACK_BUTTON]

// class SignMenu(InlineKeyboard):
//     DELETE = CallbackButton("Удалить", "delete-sign:{id}")

//     def __init__(self, sign_id: str):
//         button = self.DELETE.format(id=sign_id)
//         super().__init__(button)

// class Cancel(InlineKeyboard):
//     buttons = [BACK_BUTTON]

// class RequiredJoin(InlineKeyboard):
//     SELECT_CHANNEL = CallbackButton("Выбрать канал")
//     DISABLE = CallbackButton("Отключить")

//     buttons = [SELECT_CHANNEL]

//     def __init__(self, disabled: bool):
//         buttons = [] if disabled else [self.DISABLE]
//         super().__init__(*buttons, BACK_BUTTON)

// PICTURE_MENU = PictureMenu()
// ADMIN_MENU = AdminMenu()
// CANCEL = Cancel()
// SIGNS = Signs()
