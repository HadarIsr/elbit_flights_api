import requests
import json
import random
import operator

from enum import Enum
from models.config_model import Configurations
from models.flights_model import Flight
from typing import List, Union
from collections import Counter


class FailedToGetFlightsException(Exception):
    pass


class FlightEnumKey(Enum):
    empty = ''
    all_flights = 'all_flights'
    inbound = 'inbound'
    outbound = 'outbound'
    limit = 'limit'
    filter_index = 'q'
    delayed_status = 'DELAYED'
    resource_id = 'resource_id'


class FlightConfigException(Exception):
    pass


class FlightManager:

    def __init__(self, flight_config: Configurations):
        self.config = flight_config
        self.flights: Union[List[Flight], None] = None

    def get_flights(self, query_str):
        result = requests.get(
            url=self.config.url, params={
                FlightEnumKey.limit.value: self.config.limit,
                FlightEnumKey.filter_index.value: query_str,
                FlightEnumKey.resource_id.value: self.config.resource_id
            }
        )

        result = json.loads(result.text)
        if result.get(ApiEnumKeys.success.value):
            self.flights = [Flight(**flight) for flight in
                            result[ApiEnumKeys.result.value][ApiEnumKeys.records.value]]
            return
        raise FailedToGetFlightsException(result[ApiEnumKeys.error.value])

    def filter_flight_type(self, inbound: bool) -> List[Flight]:
        return list(filter(lambda flight: flight.inbound == inbound, self.flights))

    def get_delayed_flights(self):
        self.get_flights(query_str=FlightEnumKey.delayed_status.value)
        return len(self.flights)

    def get_number_of_flights(self, country: str, status: str):
        self.get_flights(country)
        if status == FlightEnumKey.outbound.value:
            self.flights = self.filter_flight_type(False)
        if status == FlightEnumKey.inbound.value:
            self.flights = self.filter_flight_type(True)
        return len(self.flights)

    def get_popular_destination(self):
        self.get_flights(query_str=FlightEnumKey.empty.value)
        cities = [flight.city for flight in self.flights]
        cities = Counter(cities)
        return max(cities.items(), key=operator.itemgetter(1))[0]

    def get_nearest_flight(self):
        self.get_flights(FlightEnumKey.empty.value)
        inbound_flights = self.filter_flight_type(inbound=True)
        quick_inbound = self.quick_getaway(inbound_flights)
        outbound_flights = self.filter_flight_type(inbound=False)
        quick_outbound = self.quick_getaway(outbound_flights)
        return {'departure': quick_inbound, 'arrival': quick_outbound}

    @staticmethod
    def quick_getaway(flights: List[Flight]):
        relevant_flight = list(filter(lambda flight: flight.is_flight_soon, flights))
        if relevant_flight:
            return random.choice(relevant_flight).flight_number
        return None


class ApiEnumKeys(Enum):
    success = 'success'
    result = 'result'
    records = 'records'
    error = 'error'

