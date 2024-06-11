"""Подключение всех обработчиков и запуск бота"""
import hse_nn_bot.booking.handlers  # noqa: F401
import hse_nn_bot.menu.handlers  # noqa: F401
from hse_nn_bot import bot

bot.infinity_polling()
