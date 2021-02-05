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


url = config.WEATHER_URL.format(city=config.location, token=config.WEATHER_TOKEN)  ### URL запроса
print(url)
response = requests.get(url)  ### Ответ на запрос
# if response.status_code != 200:
#     return 'city not found'
data = json.loads(response.content)  ### Полученные данные

data_temp = data['main']['temp'] - 273
data_feels_like_temp = data['main']['feels_like'] - 273
data_city = data['name']
data_speed = data['wind']['speed']
data_humidity = data['main']['humidity']

temp = str(math.ceil(data_temp))
feels_like_temp = str(math.ceil(data_feels_like_temp))
city = data_city
speed = str(math.ceil(data_speed))
humidity = str(data_humidity)

print(data)

print(data_city)
print(temp)
print(feels_like_temp)
print(speed)


######  Отправка сообщений
@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id,
                     'Город:    ' + data_city + '\n' + 'Температура:    ' + temp + ' °C' + '\n' + 'Ощущается как:    '
                     + feels_like_temp + ' °C' + '\n' + 'Скорость ветра:    ' + speed + ' м/сек' + '\n'
                     + 'Влажность:    ' + humidity + ' %')


if __name__ == '__main__':
    bot.polling(none_stop=True)
