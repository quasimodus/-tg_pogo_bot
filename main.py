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
response = requests.get(url)              ### Ответ на запрос
# if response.status_code != 200:
#     return 'city not found'
data = json.loads(response.content)        ### Полученные данные

data_temp = data['main']['temp'] - 273      ### Получение температуры из данных
data_city = data['name']                   ### Получение города
data_speed = data['wind']['speed']                   ### Получение города

temp = str(math.ceil(data_temp))
city = data_city
speed = str(math.ceil(data_speed))


print(data)

print(data_city)
print(temp)
print(speed)


# print('hello')


# def parse_weather_data(data):
#     for elem in data['weather']:
#         weather_state = elem['main']
#     temp = round(data['main']['temp'] - 273.15, 2)
#     city = data['name']
#     msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}'
#     return msg
# print(msg)

######  Отправка сообщений
@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, 'Город:   ' + data_city + '\n' + 'Температура:    ' + temp + '\n' + 'Скорость '
                                                                                                          'ветра:   '
                     + speed + ' м/сек')


if __name__ == '__main__':
    bot.polling(none_stop=True)
