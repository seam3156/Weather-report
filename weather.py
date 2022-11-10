#! /bin/python

from bs4 import BeautifulSoup
import requests

def select(city):
    if city == 'G':
        url = 'https://weather.com/en-GB/weather/today/l/5a88f118aa4d4ed2e88e87e88f8a8986b20bbbbe8f0beabe18b7237697887197'
        WriteChoise(city)
    elif city == 'E':
        url = 'https://weather.com/en-GB/weather/today/l/2fd3c9b1901c4eecdc602f924198e20d06a46e923422b87cd8ff352a307b810d'
        WriteChoise(city)
    elif city == 'I':
        url = 'https://weather.com/en-GB/weather/today/l/6efa618cb046f59f6b77c464d5dc2002ac6b9a608572b340894f662022ef4253'
        WriteChoise(city)
    elif city == 'A':
        url = 'https://weather.com/en-GB/weather/today/l/e1942718b11091398bcda9453ef6096c408f9691135c2945b9ee17565bf8fbd4'
        WriteChoise(city)
    elif city == 'D':
        url = 'https://weather.com/en-GB/weather/today/l/8b384d5dd7c6fe44db8af65b4d9507ad3fa65a35153e1fa4f85fbde1767ddaa8'
        WriteChoise(city)
    else:
        try:
            with open('lastchoise.txt', 'r') as file:
                city = file.read()
                url = select(city)
        except:
            print('\ninvalid city')
            quit()
    return url

def WriteChoise(choise):
    with open('lastchoise.txt', 'w') as file:
        file.write(choise)

city = input('\nWhat city do you want to know the current weather for\nGlasgow[G], Edinburgh[E], Inverness[I], Aberdeen[A], Dundee[D]: ')
url = select(city)
site = requests.get(url)

doc = BeautifulSoup(site.text, 'html.parser')

print('')
weather_description = doc.find_all("div", {"data-testid": "wxPhrase"})[0]
print(f'the condition is: {weather_description.string}')

temp = doc.find_all('span', {'data-testid': "TemperatureValue"})[0]
print(f'the temperature is: {temp.string}\n')
