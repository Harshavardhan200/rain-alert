# import requests
# from twilio.rest import Client
# account_id = 'AC924b47a2ebc71d5f1ebe8bda97013d88'
# authonicated = 'bf6deb4d3aa75bed81859bb0f35d2098'
# while True:
#     website = 'https://api.openweathermap.org/data/2.5/onecall?lat=14.660579&lon=78.172959&appid=a14ee7e46de1ac1634f641e47d926d58'
#     url = requests.get(url=website)
#     weather_data = url.json()['hourly']
#     weather_slices = weather_data[:]
#     for i in weather_slices:
#         if i['weather'][0]['id'] >= 700:
#             client = Client(account_id, authonicated)
#             mess = client.messages.create(body='There will be rainy', from_='+15074787107', to='+918309197541')
#
#             print(mess.sid, mess.status, mess.api_version)

import serial
import time
from twilio.rest import Client as cl
acc = 'AC471fc91ebd33a875ddae0b981d06dde1'
auth = '0b53756ff45d26078a1001866d502c5a'
client = cl(acc, auth)
seri = serial.Serial('COM6', 115200)
while True:
    data = str(seri.readline(), encoding='utf-8')
    print(data)
    if int(data):
        print('hi')
        mess = client.messages.create(body='Accident detected', from_='19707172698', to='+918309197541')
        print("message")
        print(mess.sid, mess.status, mess.api_version)

        print('end')
