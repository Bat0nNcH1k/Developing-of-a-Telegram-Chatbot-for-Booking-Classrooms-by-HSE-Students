from telebot import types

from hse_nn_bot.constants import BUILDINGS


def get_buildings_kb() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    buttons = []

    for building in BUILDINGS:
        button = types.InlineKeyboardButton(
            building, callback_data=building
        )
        buttons.append(button)

    for i in range(0, len(buttons), 2):
        markup.row(*buttons[i : i + 2])

    return markup
