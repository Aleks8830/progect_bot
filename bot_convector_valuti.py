# для конвертации валют мы будем использовать библиотеку currencyConverter
from datetime import date

import telebot
# подключим библиотеку currencyConverter
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('5910177422:AAERxSR2pErvJCsh_TkJBMpFWeYZni7l3Ao')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    # пропишим обработчик исключения!
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'неверный формат!!!')
        bot.register_next_step_handler(message, summa)
        return
    # проветка на положительность и ноль!!
    if amount > 0:
        # сдесь же создадим набор кнопок при нажатии на которые
        # можно выбрать пару
        # row_width=2 - количество кнопок в ряду
        markup = types.InlineKeyboardMarkup(row_width=2)
        # теперь соэдаем кнопки
        btn_1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn_2 = types.InlineKeyboardButton('eur/usd', callback_data='eur/usd')
        btn_3 = types.InlineKeyboardButton('usd/gbp', callback_data='usd/gbp')
        btn_4 = types.InlineKeyboardButton('другое значение', callback_data='else')

        markup.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id, 'выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'неверное значение ')
        bot.register_next_step_handler(message, summa)


#  создадим метод для обработки callback_data!!


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # разберемся с кнопкой "другое значение"
    if call.data != "else":
        # здесь внутри функции мы должны понять какую кнопку выбрал пользователь!
        values = call.data.upper().split('/')  # переменная хранит список из двух валют
        res = currency.convert(amount, values[0], values[1],
                               date=date(2000, 10, 31))  # функция convert позволяет сделать конверцию!
        bot.send_message(call.message.chat.id, f'получается{round(res, 2)}. Можете заново ввести данные')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, "введите пару значений через /")
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        val = message.text.upper().split('/')
        res = currency.convert(amount, val[0], val[1])
        bot.send_message(message.chat.id, f'получаем{round(res, 2)}')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'неверный формат,! !!!')
        bot.register_next_step_handler(message, summa)

if __name__ == '__main__':
    bot.polling(none_stop=True)
