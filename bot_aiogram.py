# работа с библиотекой aiogram позволит лучше понять принцип построения ботов
# в первую очередь ее нужно установить pip install aiogram

from aiogram import Bot, Dispatcher, types, executor

# создадим экземпляр который будет ссылаться на реального бота в телеграмме
bot = Bot('5910177422:AAERxSR2pErvJCsh_TkJBMpFWeYZni7l3Ao')
dp = Dispatcher(bot)


# # отслеживание команды старт
# @dp.message_handler(content_types=['text'])  # commands=['start']
# async def start(message: types.Message):
#     # await bot.send_message(message.chat.id,'Hello world') # первый способ как можно отправить сообщение
#     # await message.answer('Hello world')  # более удобный способ здесь не нужно указывать chat.id
#     # создадим сообщение с ответом
#     await message.reply("hello")
#     # file = open("/some.png", 'rb ') открываем фаил при помощи open
#     # await message.answer_photo(file) отравка фото пользователю


# создание кнопок
@dp.message_handler()
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('site', url='https://www.google.ru'))
    markup.add(types.InlineKeyboardButton('hello', callback_data='hello'))
    await message.reply("привет",reply_markup = markup)

# создадим обработчик событий для них

@dp.callback_query_handler()
async def call():
    await call.message.answer(call.data)
if __name__ == '__main__':
    executor.start_polling(dp)
