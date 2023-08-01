from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_start = InlineKeyboardMarkup(row_width=True)
ikb_start.add(InlineKeyboardButton(
    text='Случайный вопрос', callback_data='start'))

ikb = InlineKeyboardMarkup(row_width=True)
ikb.add(InlineKeyboardButton(text='Следуйший вопрос', callback_data='next'))
