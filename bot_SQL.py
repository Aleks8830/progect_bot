# подключение к базе данных
import sqlite3  # библиотека для базы данных она встроена

import telebot

bot = telebot.TeleBot('5910177422:AAEDJD_9XRxQCglyQ8wE7q9tH1vHYCdEkCE')

name = None


# создадим обработчик команды старт
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('basa.sql')
    cur = conn.cursor()  # через этот объект мы будем управлять всеми командами

    # создадим в базе данных новую таблицу!
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50)) ')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "привет сейчас тебя зарегестрируем, введите Ваше имя!!")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    # в этой функции мы должны принимать некий текст и
    # записать его в некую переменную!
    # strip()-удаляет все лишние пробелы!
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "введите пароль!")
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    # в этой функции мы должны принимать некий текст и
    # записать его в некую переменную!
    # strip()-удаляет все лишние пробелы!
    password = message.text.strip()
    # далее мы должны зарегестрировать пользователя и в качестве
    # данных для регистрации мы будем использовать имя и пароль!!
    # необходимо подключится к базе данных
    conn = sqlite3.connect('basa.sql')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO users (name, pass) VALUES ("%s","%s")' % (name, password))
    # говорим что будем добавлять новую запись в таблицу users
    # в качестве полей это имя  и pass мы подставляем такие значения
    conn.commit()
    cur.close()
    conn.close()
    # добавим к этому сообщению еще кнопку при нажатии на которую
    # будет отображаться список всех пользователей
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегестрирован', reply_markup=markup)
    # bot.send_message(message.chat.id, "введите !")
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('basa.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users_1 = cur.fetchall()
    # cur.fetchall() - эта функция вернет нам все найденные записи
    info = ''
    for el in users_1:
        info += f'Имя {el[1]}, пароль {el[2]} id {el[0]}\n'

    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id,info)
# при команде старт будет создаваться таблица users с тремя полями и создается только один раз!!!
# CREATE TABLE IF NOT EXISTS - создать таблицу если ее еще не существует
# conn.commit() - команда создания таблицы
# cur.close()    conn.close() - команды закрытия соединения с базой данных
if __name__ == '__main__':
    bot.polling(none_stop=True)
