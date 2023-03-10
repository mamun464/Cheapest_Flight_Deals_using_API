#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from pprint import pprint

from SmsMechanism import sms_sent
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager=DataManager()
notification_manager=NotificationManager()
sheet_data=data_manager.sheetData()
#pprint(sheet_data)


flight_search = FlightSearch()

# print(sheet_data[0]["iataCode"])
haveToUpdate=False
for each_row in sheet_data:
    if each_row["iataCode"] == "":
        each_row["iataCode"]=flight_search.getCodeIATA(each_row["city"])
        data_manager.updateIATA(each_row)
        haveToUpdate=True
    print(f"sheet_data:\n {sheet_data}")

if haveToUpdate:
    data_manager.detinationData=sheet_data
    #data_manager.updateIATA()
flight_search=FlightSearch()
Destination_Airpot_code="LON"
from_time=1 #How many Day from today
till_time=180 #How many Day from today
for single_sheet_data in sheet_data:
    flight_get=flight_search.Get_flight_data(
                                Destination_Airpot_code,
                                single_sheet_data["iataCode"],
                                from_time,
                                till_time)
    if flight_get != None:
        if single_sheet_data["lowestPrice"] > flight_get.price:
            msg_body=f"\nLowest Price Alert! Only {flight_get.price}$ " \
                     f"to fly from {flight_get.departure_city}-{flight_get.departure_airport_code} " \
                     f"to {flight_get.destination_city}-{flight_get.destination_airport_code}," \
                     f" from {flight_get.journey_start_date} to {flight_get.journey_return_date}\n"

            #notification_manager.sms_sent(msg_body)
            print("Find Cheapest 🔺\n")
        else:
            print("No Cheapest Flight\n")