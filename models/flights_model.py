from pydantic import BaseModel
from datetime import datetime
from enum import Enum

EMPTY = ''
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
EARLY_TIME = 3
LATE_TIME = 4


def inbound_status(check_in: str) -> bool:
    if check_in == EMPTY:
        return False
    return True


def extract_date_from_str(date: str):
    return datetime.strptime(date, DATE_FORMAT)


def calculate_hour_to_second(hour):
        return hour * 60 * 60


def is_flight_soon(estimate_flight_time):
        now = datetime.now()
        diff = estimate_flight_time - now
        diff_in_sec = diff.total_seconds()
        return calculate_hour_to_second(EARLY_TIME) <= diff_in_sec <= calculate_hour_to_second(LATE_TIME)


class ResultEnumFields(Enum):
    flight_code = 'CHOPER'
    flight_number = 'CHFLTN'
    estimated_departure_time = 'CHSTOL'
    destination_airport = 'CHLOC1D'
    city = 'CHLOC1T'
    country = 'CHLOCCT'
    inbound = 'CHCINT'
    status = 'CHRMINE'


class Flight(BaseModel):
    flight_number: str
    estimated_departure_time: datetime
    city: str
    country: str
    inbound: bool
    status: str
    is_flight_soon: bool

    def __init__(self, **kwargs):
        flight_dict = self.flight_helper(kwargs)
        super().__init__(**flight_dict)

    @staticmethod
    def flight_helper(flight):
        estimated_departure_time = extract_date_from_str(flight.get(ResultEnumFields.estimated_departure_time.value))
        return {
            'flight_number': flight.get(ResultEnumFields.flight_code.value)
            + flight.get(ResultEnumFields.flight_number.value),
            'estimated_departure_time': estimated_departure_time,
            'destination_airport': flight.get(ResultEnumFields.destination_airport.value),
            'city': flight.get(ResultEnumFields.city.value),
            'country': flight.get(ResultEnumFields.country.value),
            'inbound': inbound_status(flight.get(ResultEnumFields.inbound.value)),
            'status': flight.get(ResultEnumFields.status.value),
            'is_flight_soon': is_flight_soon(estimated_departure_time)
        }
