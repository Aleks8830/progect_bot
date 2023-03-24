# получать информацию относительно погоды будем при помощи отдельного
# стороннего сервиса!! https://openweathermap.org
#            !!!!принцип работы!!
# через нашу программу (бота) отправлять запрос по определенному URL адресу
# подставлять мы должны город и API ключ. Далее мы будем получать json ответ
# мы этот json ответ будем обрабатывать и выводить пользователю понятную инфу!!
# Для этого необходимо установить библиотеку requests!!
# данная библиотека позволит нам отправлять запрос по некому URL адресу и получать ответ!
#
# что бы нам обрабатывать json объекты мы подключим модуль jsom
#
import json

import requests
import telebot

bot = telebot.TeleBot('5910177422:AAEDJD_9XRxQCglyQ8wE7q9tH1vHYCdEkCE')
API = "ef4e5b952e3bdc662c41774d40d12ed0"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет, введите название города!!")


# создадим функцию которая будет срабатывать когда пользователь
# будет вводить некий текст!!
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    # обработаем исключение если города не существует!!
    if res.status_code ==200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"температура за окном :{temp} градусов С")
        # внизу записан содуль без json обработки!
        # bot.reply_to(message, f"Сейчас погода :{res.json()}")

        # теперь добавим фото в зависимости от погоды!
        image = 'images_1.jpeg' if temp > 5.0 or temp < 0.0 else "images_2.jpeg"
        # далее необходимо открыть это изображение
        file = open('./' + image, 'rb')
        # далее мы отправляем пользователю фото
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f"города {city} не существует!!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
