
1. # Телеграмм-бот 'Занято!' для бронирования аудиторий  в НИУ ВШЭ (НиНо).

2. ## Описание
Этот проект представляет собой телеграмм-бота, предназначенного для бронирования аудиторий в учебных корпусах. Бот создан для того, чтобы оптимизировать и упростить процесс бронирования нужной аудитории для студентов и преподователей.

3. ## Функциональность
- Регистрация пользователей.
- Бронирование аудиторий на определённые даты и время.
- Отмена бронирований.
- Уведомления о предстоящих бронированиях.
- Просмотр актуальных бронирований.

4. ## Требования
Для запуска и работы телеграмм-бота необходимы следующие компоненты:
- Python 3.8 или выше: Рекомендуется использовать последнюю стабильную версию Python для лучшей совместимости и безопасности.
- Библиотеки Python:
  pyTelegramBotAPI
  pytz
  sqlite3
  Полный список библиотек и их версии можно найти в файле requirements.txt.
- В данном проекте в качестве базы данных используется SQLite.
    
5. ## Использование
Клонируйте репозиторий и установите необходимые библиотеки:
   
Bash
pip install -r requirements.txt
    
Для взаимодействия непосредственно  с ботом, найдите его в Телеграмме по имени пользователя или по ссылке, и начните с команды /start. Далее следуйте сообщениям, предоставляемым ботом.
https://web.telegram.org/a/#6867213889

7. ## Примеры команд
- /start - Начать работу с ботом.
- /help - Получить список доступных команд.
- /book - Забронировать аудиторию.
- /mybookings - Показать мои бронирования.
- /cancel - Отменить бронирование
  
8. ## Структура проекта
- bot.py - Основной файл для инициализации бота.
- booking - Подкаталог, содержащий модули, связанные с функционалом бронирования.
- menu - Отвечает за обработку команд меню и создание клавиатур для взаимодействия с пользователем.
- requirements.txt - Список зависимостей проекта.
- .env - Файл конфигурации окружения.
- bookings.db - Файл базы данных SQLite.
  
9. ## Автор и контакты
[Илья Шалявин],
[Золотова Ангелина],
[Смирнова Анастасия]
