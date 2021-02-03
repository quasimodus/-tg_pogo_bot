import telebot
import config
import requests
from bs4 import BeautifulSoup

# r = requests.get('http://gismeteo.ru/weather-tula-4392')
# content = r.content
# html = BeautifulSoup(content, 'html.parser')
bot = telebot.TeleBot(config.token)

# for elem in html.select('.tab-content'):
#     y_data = elem.select('.date ')[0].text
#     print(y_data)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Я могу показать погоду ")


if __name__ == '__main__':
    bot.polling(none_stop=True)
