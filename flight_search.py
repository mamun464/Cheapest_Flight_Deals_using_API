from datetime import datetime as dt, timedelta
from pprint import pprint

from flight_data import FlightData

FLIGHT_API_KEY="WQchViXZoNPEshdn7yEaoE_vPB_3vjle"
FILGHT_SEARCH_ENDPOINT="https://tequila-api.kiwi.com/v2/search"

import requests

SEARCH_API_Locations="https://api.tequila.kiwi.com/locations/query"
API_KEY_Locations="WQchViXZoNPEshdn7yEaoE_vPB_3vjle"
class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def getCodeIATA(self, city_name):
        #self.cityName = city_name
        header={
            "apikey":API_KEY_Locations,
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response=requests.get(url=SEARCH_API_Locations,headers=header,params=query)
        response.raise_for_status()
        code=(response.json())["locations"][0]["code"]
        #print(location)


        return code
    def Get_flight_data(self,fly_from_airport_code,fly_to_airortCode,date_from,date_to):

        # Specify the search parameters
        params = {
            "fly_from":fly_from_airport_code,
            "fly_to": fly_to_airortCode,
            "date_from": self.GenerateFlight_Search_TimeInerval(day=date_from),
            "date_to": self.GenerateFlight_Search_TimeInerval(day=date_to),
            "adults": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        header={
            "apikey": FLIGHT_API_KEY
        }
        # Make the request and include your API key in the request header
        response = requests.get(url=FILGHT_SEARCH_ENDPOINT, headers=header, params=params)
        #print(response.text)
        response.raise_for_status()
        result=response.json()

        # x=resultData
        # pprint(resultData)
        # print(len(x))

        try:
            resultData = result["data"][0]
        except IndexError:
            print(f"No Flight Found to {fly_to_airortCode}")
            return None

        flight_data = FlightData(
            price=resultData["price"],
            departure_airport_code =resultData["route"][0]["flyFrom"],
            departure_city =resultData["route"][0]["cityFrom"],
            destination_airport_code =resultData["route"][0]["flyTo"],
            destination_city =resultData["route"][0]["cityTo"],
            journey_start_date =resultData["route"][0]["local_departure"].split("T")[0],
            journey_return_date =resultData["route"][1]["local_departure"].split("T")[0]
        )

        print(f"From {flight_data.departure_city} to {flight_data.destination_city} : {flight_data.price}$")
        return flight_data




    def GenerateFlight_Search_TimeInerval(self,day):
        now=dt.now()

        # add 6 months from current date
        six_months_ago = now + timedelta(days=day)

        # print the result in a specific format
        return (six_months_ago.strftime('%Y-%m-%d'))

