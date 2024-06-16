from fastapi import APIRouter, Query
from starlette import status

from api.bookings import service
from api.bookings.schemas import BookingCreate, BookingRead, IDResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_booking(creation: BookingCreate) -> IDResponse:
    booking_id = service.write_booking(creation)
    return IDResponse(id=booking_id)


@router.get("/", status_code=status.HTTP_200_OK)
def get_user_bookings(user_id: int = Query()) -> list[BookingRead]:
    return service.get_bookings(user_id)
