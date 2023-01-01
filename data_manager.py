import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        sheety_endpoint = 'https://api.sheety.co/0289d983845b630f15a0c98809b02a4d/flightDeals/prices'
        response= requests.get(url=sheety_endpoint)
        self.data=response.json()['prices']
        

    def update(self,object_id,low):
        
        sheety_endpoint = f'https://api.sheety.co/0289d983845b630f15a0c98809b02a4d/flightDeals/prices/{object_id}'
        response= requests.put(url=sheety_endpoint,json={'price':{'lowestPrice':low}})
        

