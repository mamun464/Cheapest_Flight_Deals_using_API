from pprint import pprint

import requests
sheety_endpoint="https://api.sheety.co/58199df9724bf4f2e4054109825787df/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.detinationData={}
    def sheetData(self):
        
        header_sheety = {
            "Authorization": "Bearer mamun&feel_the_trip"
        }
        response=requests.get(url=sheety_endpoint,headers=header_sheety)
        response.raise_for_status()
        prices=response.json()
        self.detinationData=prices["prices"]

        return self.detinationData

    def updateIATA(self,city):
        header_sheety = {
            "Authorization": "Bearer mamun&feel_the_trip"
        }
        #for city in self.detinationData:
        new_data = {
            "price": {

                "iataCode": city["iataCode"]
            }
        }
        sheety_endpoint = "https://api.sheety.co/58199df9724bf4f2e4054109825787df/flightDeals/prices"
        respone = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, headers=header_sheety)
        print(respone.text)
