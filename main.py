import requests
#import os
from datetime import datetime

api_key = '190978a5103d164a3be997dd11795b10'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


A = "-------------------------------------------------------------"
B = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
C = "-------------------------------------------------------------"

D = "Current temperature is: {:.2f} deg C".format(temp_city)
E = "Current weather desc  :", weather_desc
F = "Current Humidity      :", hmdt, '%'
G = "Current wind speed    :", wind_spd, 'kmph'

with open('WeatherForecasting.txt','w') as out:
    out.writelines('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(A,B,C,D,E,F,G))