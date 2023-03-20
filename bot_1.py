import webbrowser  # модуль для перехода на взб

import telebot

bot = telebot.TeleBot('5910177422:AAEDJD_9XRxQCglyQ8wE7q9tH1vHYCdEkCE')


# метод для перехода на сайт
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://pypi.org')


@bot.message_handler(commands=['start', 'hello'])
def com_start(message):
    bot.send_message(message.chat.id, '<b>привет</b><u>world</u>',
                     parse_mode='html')


@bot.message_handler(commands=['start'])
def com_main(message):
    bot.send_message(message.chat.id, f'привет {message.text}')


# обработка обычного текста который будет вписан пользователем
@bot.message_handler()  # ()- говорит нам что будет обработан любой текст
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш id {message.from_user.id}')


# lower() - приведение к нижнему регистру
if __name__ == '__main__':
    bot.polling(none_stop=True)
