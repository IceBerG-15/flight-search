import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv('projects\\flight-deals-start\\.env')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_endpoint ='https://api.tequila.kiwi.com/v2/search'
        self.header={
            'apikey':os.getenv('TEQUILA_API_KEY')
        }
        
    
    def search_flight(self,from_date,to_date,fly_to,fly_from='LON'):
        params={
            'fly_from':fly_from,
            'fly_to':fly_to,
            'dateFrom':from_date,
            'dateTo':to_date,
            'only_weekends':True,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            'curr':'GBP'
        }
        response=requests.get(url=self.api_endpoint,headers=self.header,params=params)
        
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data


