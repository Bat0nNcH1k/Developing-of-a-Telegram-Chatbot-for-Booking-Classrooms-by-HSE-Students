from hse_nn_bot import bot
from hse_nn_bot.menu.keyboards import get_options_kb


@bot.message_handler(commands=["start", "restart"])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if message.from_user.last_name:
        user_name += " " + message.from_user.last_name

    markup = get_options_kb()
    welcome_message = (
        "Привет, <a href='tg://user?id={}'>{}</a>!\n"
        "Бот предназначен для бронирования аудиторий на территории кампуса НИУ ВШЭ - Нижний Новгород.\n"
        "Для того, чтобы начать процесс бронирования аудитории, нажмите кнопку <b>Забронировать аудиторию</b>.\n"
        "Для того, чтобы проверить свои бронирования, нажмите кнопку <b>Мои бронирования</b>.\n"
        "Для того, чтобы перейти на сайт нашего кампуса, нажмите кнопку <b>Сайт нашего кампуса</b>."
    )

    bot.send_message(
        message.chat.id, welcome_message.format(user_id, user_name), parse_mode="HTML"
    )
    bot.send_message(
        message.chat.id, "Для дальнейшей работы нажмите кнопку.", reply_markup=markup
    )
