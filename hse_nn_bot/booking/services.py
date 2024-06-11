import sqlite3


def write_booking(user_id, chosen_corp, number, start_time, end_time):
    # Запись бронирования в базу данных
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        location TEXT,
                        room_number INTEGER,
                        start_time TEXT,
                        end_time TEXT)""")
    cursor.execute(
        """INSERT INTO bookings (user_id, location, room_number, start_time, end_time)
                      VALUES (?, ?, ?, ?, ?)""",
        (
            user_id,
            chosen_corp,
            number,
            start_time.isoformat(),
            end_time.isoformat(),
        ),
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_bookings(user_id):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT location, room_number, start_time, end_time FROM bookings WHERE user_id = ?""",
        (user_id,),
    )
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()

    return bookings
