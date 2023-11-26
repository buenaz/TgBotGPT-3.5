#подключение библиотек
from config import * #файл с токенами
import logging
import os
import openai
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
openai.api_key = DPENAI_API_KEY
bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

#функция openai
async def ai(promt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Кто такой бот..."},
            {"role": "user", "content": "Кто такой клиент..."}]
    )
    return completion.choices[0].message.content

#хэндлер старта
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message:types.Message):
    await message.reply("Стартовое сообщение")

#хэндлер сообщения
@dp.message_handler()
async def echo(message: types.Message):
    answer = await ai(message.text)
    if answer != None:
        await message.reply(answer)
    else:
        await message.reply("Неизвестная ошибка, попробуйте еще раз!")

#старт работы бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
