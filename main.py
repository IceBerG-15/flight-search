#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime,timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


#dates ka khel
now = datetime.now().strftime("%d")
tomorrow=datetime(year=2022,month=12,day=int(now)+1).strftime("%d/%m/%Y")
end_date=(datetime.now()+timedelta(days = 6*30)).strftime("%d/%m/%Y")
from_city='LON'

#calling of other classes

sms_service=NotificationManager()
sheet_data=DataManager()
search=FlightSearch()



#looking through sheet_data and finding if the price is lower than sheet_data or not
for i in sheet_data.data:
    flight=search.search_flight(from_date=tomorrow,to_date=end_date,fly_from=from_city,fly_to=i['iataCode'])
    if flight != None:
        
        if i['lowestPrice']>flight.price:
            string=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            sms_service.send_message(
                msg=string
            )
            

