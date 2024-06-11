FROM python:3.12-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN chmod 755 .
COPY hse_nn_bot hse_nn_bot
COPY bookings.db .

