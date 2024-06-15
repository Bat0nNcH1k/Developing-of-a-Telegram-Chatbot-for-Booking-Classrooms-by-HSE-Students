import datetime
import pytz
from unittest.mock import patch, MagicMock
import pytest
from hse_nn_bot import user_data

@pytest.fixture(scope="function")
def bot_instance():
    with patch("hse_nn_bot.bot") as mocked_bot:
        yield mocked_bot

def test_process_number_input(bot_instance):
    message = MagicMock()
    message.text = "101"
    message.chat.id = 123456

    user_data[message.chat.id] = {}  # Initialize user data
    from hse_nn_bot.booking.handlers import process_number_input

    process_number_input(message)

    assert user_data[123456]["number"] == 101

def test_process_start_time_input(bot_instance):
    message = MagicMock()
    message.text = "24.05.24 13:00"
    message.chat.id = 123456

    user_data[message.chat.id] = {}  # Initialize user data
    from hse_nn_bot.booking.handlers import process_start_time_input

    process_start_time_input(message)

    expected_start_time = datetime.datetime(2024, 5, 24, 13, 0)
    expected_start_time = pytz.timezone("Europe/Moscow").localize(expected_start_time)
    assert user_data[123456]["start_time"] == expected_start_time

def test_process_end_time_input(bot_instance):
    message = MagicMock()
    message.text = "24.05.24 14:00"
    message.chat.id = 123456

    user_data[message.chat.id] = {
        "chosen_corp": "Сормовское шоссе, 30",
        "number": 101,
        "start_time": datetime.datetime(2024, 5, 24, 13, 0, tzinfo=pytz.timezone("Europe/Moscow")),
        "user_id": 123456,
    }

    from hse_nn_bot.booking.handlers import process_end_time_input

    with patch("hse_nn_bot.booking.handlers.write_booking") as mocked_write_booking:
        process_end_time_input(message)

        expected_end_time = datetime.datetime(2024, 5, 24, 14, 0)
        expected_end_time = pytz.timezone("Europe/Moscow").localize(expected_end_time)

        mocked_write_booking.assert_called_once_with(
            123456,
            "Сормовское шоссе, 30",
            101,
            datetime.datetime(2024, 5, 24, 13, 0, tzinfo=pytz.timezone("Europe/Moscow")),
            expected_end_time,
        )