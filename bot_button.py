# научимся создавать кнопки и отправлять разные
# файлы пользователю!!!
#
#
#
import telebot
from telebot import types

bot = telebot.TeleBot('5910177422:AAERxSR2pErvJCsh_TkJBMpFWeYZni7l3Ao')


# создадим кнопки которые будут отображаться возле поля для
# ввода текста!!
@bot.message_handler(commands=['start'])
def start(message):
    button = types.ReplyKeyboardMarkup()
    ibt_1 = types.InlineKeyboardButton('перейти на сайт')
    button.add(ibt_1)
    ibt_2 = types.InlineKeyboardButton('удалить сайт')
    ibt_3 = types.InlineKeyboardButton('удалить часть сайта')
    button.row(ibt_2, ibt_3)
    bot.send_message(message.chat.id, 'привет', reply_markup=button)
    # рассмотрим каким образом пользователю можно
    # отправлять различные файлы!!
    file = open('./cat.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)
    # если хотим обрабатывать нажатие на эти кнопки нужно
    # создать следующую функцию!
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    # функция срабатывает один раз!!
    if message.text == 'перейти на сайт':
        bot.send_message(message.chat.id, 'website is open!!')
    elif message.text == 'удалить сайт':
        bot.send_message(message.chat.id, 'website delete!!')


# создадим инлайн кнопки!
markup = types.InlineKeyboardMarkup()
bt_1 = types.InlineKeyboardButton('переход на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww')
bt_2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
bt_3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
markup.row(bt_1, bt_2, bt_3)
markup.add(types.InlineKeyboardButton('изменить текст', callback_data='edit'))


# callback_data = это параметр указывающий что при нажатии
@bot.message_handler(content_types=['photo'])
# метод сработает если пользователь отправит фото!
def get_photo(message):
    # создадим инлайн кнопки!

    # callback_data = это параметр указывающий что при нажатии
    # на эту кнопку будет вызываться некий callback (функция)
    # которая будет отвечать за действия этой кнопки!!
    # row - добавляет столбцы
    # add - добавляет строки
    bot.reply_to(message, 'какое красивое фото!!',
                 reply_markup=markup)


# создадим функцию которая будет обрабатывать callback_data!!
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('текст изменен!!', callback.message.chat.id, callback.message.message_id)


if __name__ == '__main__':
    bot.polling(non_stop=True)
