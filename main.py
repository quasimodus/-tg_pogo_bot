import json
import math

import telebot
import config
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.token)

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, 'Погода в городе ' + message.text + ' не плохая')
#     # bot.reply_to(message, message)


url = config.WEATHER_URL.format(city=config.location, token=config.WEATHER_TOKEN)
print(url)
response = requests.get(url)
# if response.status_code != 200:
#     return 'city not found'
data = json.loads(response.content)
data_temp = data['main']['temp'] - 273
temp = str(math.ceil(data_temp))
# return parse_weather_data(data)
print(data)
print(temp)


# print('hello')


# def parse_weather_data(data):
#     for elem in data['weather']:
#         weather_state = elem['main']
#     temp = round(data['main']['temp'] - 273.15, 2)
#     city = data['name']
#     msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}'
#     return msg
# print(msg)


@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, 'Температура в городе:    ' + temp)


if __name__ == '__main__':
    bot.polling(none_stop=True)
