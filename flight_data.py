from pprint import pprint

import requests


from datetime import datetime, timedelta


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,departure_airport_code,departure_city,destination_airport_code,
                 destination_city,journey_start_date,journey_return_date="Null"):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.destination_airport_code=destination_airport_code
        self.destination_city = destination_city
        self.journey_start_date=journey_start_date
        self.journey_return_date = journey_return_date




