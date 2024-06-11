from telebot import types


def get_options_kb():
    markup = types.InlineKeyboardMarkup()

    website_button = types.InlineKeyboardButton(
        "Сайт нашего кампуса", url="https://nnov.hse.ru"
    )
    buildings_button = types.InlineKeyboardButton(
        "Забронировать аудиторию", callback_data="Забронировать аудиторию"
    )
    user_reservation_button = types.InlineKeyboardButton(
        "Мои бронирования", callback_data="Мои бронирования"
    )

    markup.row(buildings_button, website_button)
    markup.add(user_reservation_button)

    return markup
