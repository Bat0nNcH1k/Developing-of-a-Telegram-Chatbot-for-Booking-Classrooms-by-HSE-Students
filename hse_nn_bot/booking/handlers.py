import datetime

import pytz

from hse_nn_bot import bot, user_data
from hse_nn_bot.booking.keyboards import get_buildings_kb
from hse_nn_bot.booking.services import write_booking, get_bookings
from hse_nn_bot.constants import BUILDINGS, ADMIN_CHAT_ID


@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data == "Забронировать аудиторию":
        markup = get_buildings_kb()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выбери адрес корпуса, в котором хочешь забронировать аудиторию.",
            reply_markup=markup,
        )
    elif call.data in BUILDINGS:
        bot.edit_message_text(
            f"Вы выбрали корпус по адресу {call.data}.",
            call.message.chat.id,
            call.message.message_id,
        )
        bot.send_message(
            call.message.chat.id,
            f"Введите номер аудитории, которую хотите забронировать.",
        )
        # Сохраняем выбранный корпус и user_id в словаре user_data
        user_data[call.message.chat.id] = {
            "chosen_corp": call.data,
            "user_id": call.message.chat.id,
        }
        bot.register_next_step_handler(call.message, process_number_input)
    elif call.data == "Мои бронирования":
        show_user_bookings(call.message)


def process_number_input(message):
    try:
        number = int(message.text)
        bot.send_message(
            message.chat.id,
            f"Введите дату и время начала бронирования в формате ДД.ММ.ГГ ЧЧ:ММ (например, 24.02.24 13:00).",
        )
        user_data[message.chat.id]["number"] = number
        bot.register_next_step_handler(message, process_start_time_input)
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Неверный формат номера аудитории. Пожалуйста, введите номер аудитории еще раз.",
        )
        bot.register_next_step_handler(message, process_number_input)


def process_start_time_input(message):
    try:
        start_time_naive = datetime.datetime.strptime(message.text, "%d.%m.%y %H:%M")
        start_time = pytz.timezone("Europe/Moscow").localize(start_time_naive)
        user_data[message.chat.id]["start_time"] = start_time
        bot.send_message(
            message.chat.id,
            f"Введите дату и время окончания бронирования в формате ДД.ММ.ГГ ЧЧ:ММ (например, 24.02.24 14:00).",
        )
        bot.register_next_step_handler(message, process_end_time_input)
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Неверный формат даты и времени начала бронирования. "
            "Пожалуйста, введите дату и время начала бронирования еще раз.",
        )
        bot.register_next_step_handler(message, process_start_time_input)


def process_end_time_input(message):
    try:
        end_time_naive = datetime.datetime.strptime(message.text, "%d.%m.%y %H:%M")
        end_time = pytz.timezone("Europe/Moscow").localize(end_time_naive)
        start_time = user_data[message.chat.id]["start_time"]
        chosen_corp = user_data[message.chat.id]["chosen_corp"]
        number = user_data[message.chat.id]["number"]
        user_id = user_data[message.chat.id]["user_id"]

        write_booking(user_id, chosen_corp, number, start_time, end_time)

        if end_time > start_time:
            bot.send_message(
                message.chat.id, "Поздравляем! Вы забронировали аудиторию."
            )
            user_link = f"<a href='tg://user?id={user_id}'>пользователь</a>"
            admin_message = (
                f"{user_link} забронировал аудиторию:\n"
                f"Корпус: {chosen_corp}\n"
                f"Аудитория: {number}\n"
                f"Начало: {start_time.strftime('%d.%m.%y %H:%M')}\n"
                f"Окончание: {end_time.strftime('%d.%m.%y %H:%M')}"
            )
            bot.send_message(ADMIN_CHAT_ID, admin_message, parse_mode="HTML")
        else:
            bot.send_message(
                message.chat.id,
                "Время окончания бронирования должно быть позже времени начала бронирования. "
                "Пожалуйста, введите дату и время окончания бронирования еще раз.",
            )
            bot.register_next_step_handler(message, process_end_time_input)
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Неверный формат даты и времени окончания бронирования. "
            "Пожалуйста, введите дату и время окончания бронирования еще раз.",
        )
        bot.register_next_step_handler(message, process_end_time_input)


def show_user_bookings(call):
    user_id = call.chat.id
    print("DEBUG: Chat ID from callback:", user_id)

    user_info = bot.get_chat_member(user_id, user_id)

    if user_info:
        user_id = user_info.user.id
        print("DEBUG: User ID:", user_id)
    else:
        print("DEBUG: Failed to fetch user info")

    bookings = get_bookings(user_id)

    if bookings:
        print(f"DEBUG: Found {len(bookings)} bookings for user {user_id}")
        booking_details = "Ваши бронирования:\n\n"
        for booking in bookings:
            booking_details += (
                f"Корпус: {booking[0]}\n"
                f"Аудитория: {booking[1]}\n"
                f"Начало: {datetime.datetime.fromisoformat(booking[2]).strftime('%d.%m.%y %H:%M')}\n"
                f"Окончание: {datetime.datetime.fromisoformat(booking[3]).strftime('%d.%m.%y %H:%M')}\n\n"
            )
        bot.send_message(call.chat.id, booking_details)
    else:
        print(f"DEBUG: No bookings found for user {user_id}")
        bot.send_message(call.chat.id, "У вас нет активных бронирований.")


@bot.callback_query_handler(func=lambda call: call.data == "Мои бронирования")
def my_bookings_callback(call):
    show_user_bookings(call)
