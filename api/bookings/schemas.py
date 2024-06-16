import datetime

from pydantic import BaseModel, Field


class BookingBase(BaseModel):
    user_id: int
    location: str
    room_number: int
    start_time: datetime.datetime
    end_time: datetime.datetime


class BookingRead(BookingBase):
    id: int = Field(ge=1)


class BookingCreate(BookingBase):
    pass


class IDResponse(BaseModel):
    id: int = Field(ge=1)
