import os
import sqlite3
from typing import Final

from api.bookings.schemas import BookingCreate, BookingRead

BOOKINGS_DB: Final = os.getenv("BOOKINGS_DB", "bookings.db")


def write_booking(creation: BookingCreate) -> int:
    # Запись бронирования в базу данных
    conn = sqlite3.connect(BOOKINGS_DB)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        location TEXT,
                        room_number INTEGER,
                        start_time TIMESTAMP,
                        end_time TIMESTAMP)""")
    cursor.execute(
        """INSERT INTO bookings (user_id, location, room_number, start_time, end_time)
                      VALUES (?, ?, ?, ?, ?)""",
        (
            creation.user_id,
            creation.location,
            creation.room_number,
            creation.start_time,
            creation.end_time,
        ),
    )
    booking_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return booking_id


def get_bookings(user_id: int) -> list[BookingRead]:
    conn = sqlite3.connect(BOOKINGS_DB)
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM bookings WHERE user_id = ?""",
        (user_id,),
    )
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        BookingRead(
            id=b[0],
            user_id=b[1],
            location=b[2],
            room_number=b[3],
            start_time=b[4],
            end_time=b[5],
        )
        for b in bookings
    ]
