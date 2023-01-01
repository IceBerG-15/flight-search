from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv('projects\\flight-deals-start\\.env')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_auth_token=os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_acc_sid=os.getenv('TWILIO_ACCOUNT_SID')
        self.twilio_no=os.getenv('TWILIO_NO')
        self.my_number=os.getenv('MY_NUMBER')

    def send_message(self,msg):
        client=Client(self.twilio_acc_sid,self.twilio_auth_token)
        message = client.messages \
                .create(
                    body=msg,
                    from_=self.twilio_no,
                    to=self.my_number
                )
        print(message.sid)
