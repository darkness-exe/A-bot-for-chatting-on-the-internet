from aiogram import *
from app.parsing.parsing import questions
from random import choice
from app.key import ikb, ikb_start

import random

TOKEN = 'YOUR TOKEN'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет я бот для общение в телеграмм \nНажми на кнопку или напиши /r что бы увидеть вопрос", reply_markup=ikb_start)


@dp.message_handler(commands=['r'])
async def r_command(message: types.Message):
    await message.answer(choice(questions).text)


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'next':
        await bot.send_message(chat_id=callback_query.from_user.id, text=random.choice(questions).text, reply_markup=ikb)
    if callback_query.data == 'start':
        await bot.send_message(chat_id=callback_query.from_user.id, text=random.choice(questions).text, reply_markup=ikb)


async def onstart(_):
    print('Бот запушен!')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=onstart, skip_updates=True)
