from core import dp

from assets import commands

event = dp.command(commands.START, state='*')

group_welcome_text = f"""
💕 Спасибо, что добавили меня!

Я умею отправлять аватарки и пикчи для диалогов. Попробуй одну из этих команд:

👉🏻 /{commands.GET_AVATARS} 👉🏻 /{commands.GET_PAIRED}
👉🏻 /{commands.GET_CUTE} 👉🏻 /{commands.GET_ANGRY}
👉🏻 /{commands.SEND_PICTURE}
"""
