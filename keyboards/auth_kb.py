from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True)

share_phone_button = KeyboardButton(text='Share your phone number', request_contact=True)

share_phone_keyboard.add(share_phone_button)
