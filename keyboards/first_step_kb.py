from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

first_step_kb = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True)

sushi = KeyboardButton(text='Sushi')
sets = KeyboardButton(text='Sets')
rolls = KeyboardButton(text='Rolls')

first_step_kb.add(sushi, sets, rolls)
