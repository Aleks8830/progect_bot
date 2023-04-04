# создание полноценного приложения внутри нашего бота
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5910177422:AAERxSR2pErvJCsh_TkJBMpFWeYZni7l3Ao')
dp = Dispatcher(bot)


# сделаем так, чтобы при нажатии на команду старт появлялась кнопка
# при нажатии на которую открывалось полноценное веб приложение!!
@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    # создадим кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('открыть caйт гугла 🚚 !!',
                                    web_app=WebAppInfo(url='https://www.google.ru/?client=safari&channel=mac_bm')))
    await message.answer('привет друг', reply_markup=markup)
    # web_app = это


if __name__ == '__main__':
    executor.start_polling(dp)
