import json
import math
import telebot
import config
import requests

bot = telebot.TeleBot(config.token)


######## Start // Help Commands #######################

@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, 'Чтобы узнать погоду, введите назавние города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    location = message.text.lower()

    ######## URL request #######################
    url = config.WEATHER_URL.format(city=location, token=config.WEATHER_TOKEN)
    print(url)

    ######### Response from URL #################
    response = requests.get(url)

    ######### Bad input Test ##################
    if response.status_code != 200:
        return 'city not found'

    ######### Получение данных #################
    data = json.loads(response.content)

    ######### Parser
    data_temp = data['main']['temp'] - 273
    data_feels_like_temp = data['main']['feels_like'] - 273
    data_city = data['name']
    data_wind_speed = data['wind']['speed']
    data_humidity = data['main']['humidity']
    description = data['weather'][0]['main']

    ###### Attention block description_temp ####################
    description_temp = str(math.ceil(data_feels_like_temp))
    if data_feels_like_temp <= -25:
        description_temp = '⚠⚠⚠'
    elif data_feels_like_temp <= -20:
        description_temp = '⚠⚠'
    elif data_feels_like_temp <= -15:
        description_temp = '⚠'
    elif data_feels_like_temp > -15:
        description_temp = ''

    ###### Attention block description_windy ####################
    description_wind = str(math.ceil(data_wind_speed))
    if data_wind_speed >= 15:
        description_wind = '🌬🌬🌬'
    elif data_wind_speed >= 20:
        description_wind = '🌬🌬'
    elif data_wind_speed >= 10:
        description_wind = '🌬'
    elif data_wind_speed >= 5:
        description_wind = ''

    ###### Data Preparation
    temp = str(math.ceil(data_temp))
    feels_like_temp = str(math.ceil(data_feels_like_temp))
    city = data_city
    wind_speed = str(math.ceil(data_wind_speed))
    humidity = str(data_humidity)

    ###### Test in Console
    print(data)

    print(data_city)
    print(temp)
    print(feels_like_temp)
    print(wind_speed)
    print(description)

    ######## Description Weather
    if description == 'Clear':
        description = 'Ясно ☀️️'
        print('Ясно')
    elif description == 'Clouds':
        description = 'Облачно ☁️️'
        print('Облачно')
    elif description == 'Snow':
        description = 'Снег ❄️'
        print('Снег')
    elif description == 'Rain':
        description = 'Дождь  🌧'
        print('Дождь')

        ######  Send messages to the user

    bot.send_message(message.chat.id, '\n'
                     + 'Город:  ' + city + '\n'
                     + description + '\n'
                     + 'Температура:  ' + temp + ' °C ' + '\n'
                     + 'Ощущается как:  '
                     + feels_like_temp + ' °C ' + description_temp + '\n'
                     + 'Скорость ветра:  ' + wind_speed + ' м/сек ' + description_wind + '\n'
                     + 'Влажность:  ' + humidity + ' %' + '\n'
                     + 'Источник: https://openweathermap.org', disable_web_page_preview=True)


##### '\n' + 'Источник: https://openweathermap.org',disable_web_page_preview=True


if __name__ == '__main__':
    bot.polling(none_stop=True)
