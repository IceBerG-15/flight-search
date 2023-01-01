import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os

class Customer:
    def __init__(self):
        self.emails=[]        
        self.api_endpoint = 'https://api.sheety.co/0289d983845b630f15a0c98809b02a4d/flightDeals/users'
        response=requests.get(url=self.api_endpoint)
        data=response.json()['users']
        for i in data:
            self.emails.append(i['email'])

    def entry(self):
        print(
        'Welcome to Our Flight Club\nWe find the best flight deals for you and email you'
        )
        first_name = input('Whats your first name? \n').title()
        last_name = input('Whats your last name? \n')
        email = input('Whats your email id?\n')
        e = input('Enter your email again\n')
        if email==e:
            body = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
            }

            if email in self.emails:
                print('Email is already registered in our sheet. We will send you email regarding the flight details.')
            else:
                response = requests.post(url=self.api_endpoint, json=body)
                print('Welcome to Flight Club ')

        else:
            print('ERROR!!!!!  Email not matched')

    def send_email(self,to_email,message):
        my_email=os.getenv('MY_EMAIL')
        password=os.getenv('MY_EMAIL_PASS')
        with SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f'Subject:Price drop Alert\n\n{message}'
            )

