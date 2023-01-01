# flight-search

This is a flight search engine. which will search flight between the given time period and text you if the price drops.

In this different api's are used like: 
1. sheety,this api connects spreadsheet(where all the prices of flights are stored) with python.
2. tequila, this is a flight search api, which will give details about flight like prices and all.

Modules used:
1. SMTP, which will send email to the user.
2. datetime, which will give us time and date related details.
3. dotenv, which will load the env file where we stored our private details like api key, account_sid, auth token and many more.
4. os, using which we will grab the environment variables.
5. requests, using which we will grab data from websites through api.
6. twilio, using which we will send sms to the user.
