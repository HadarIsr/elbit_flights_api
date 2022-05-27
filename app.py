from app_manager.flight_manager import FlightManager, FailedToGetFlightsException, FlightEnumKey
from fastapi import FastAPI, HTTPException, APIRouter
from models.config_model import load_config

app = FastAPI()
router = APIRouter()
flight_manager = FlightManager(flight_config=load_config())


@app.get('/flights_number/')
def get_number_of_flights(county: str = FlightEnumKey.empty.value):
    try:
        return flight_manager.get_number_of_flights(county, FlightEnumKey.all_flights.value)
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


@app.get('/flights_number/inbound')
def get_inbound_flights(county: str = FlightEnumKey.empty.value):
    try:
        return flight_manager.get_number_of_flights(county, FlightEnumKey.inbound.value)
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


@app.get('/flights_number/outbound')
def get_inbound_flights(county: str = FlightEnumKey.empty.value):
    try:
        return flight_manager.get_number_of_flights(county, FlightEnumKey.outbound.value)
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


@app.get('/flights_delayed')
def get_delayed_flights():
    try:
        return flight_manager.get_delayed_flights()
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


@app.get('/most_popular_destination')
def get_most_popular_destination():
    try:
        return flight_manager.get_popular_destination()
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


@app.get('/flights_soon')
def get_soon_flights():
    try:
        return flight_manager.get_nearest_flight()
    except FailedToGetFlightsException:
        raise HTTPException(status_code=404, detail='Page not found')


app.include_router(router, tags=["TEST"], prefix="/test")

