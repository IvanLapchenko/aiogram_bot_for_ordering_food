from aiogram import types
from aiogram.dispatcher import FSMContext

from states import RegistrationStates
from auth_kb import share_phone_keyboard
from app import dp


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await RegistrationStates.Start.set()
    await message.answer(f'Hello, {message.from_user.full_name}. To order food you have to register. '
                         f'To proceed, enter your full name')


@dp.message_handler(state=RegistrationStates.Start)
async def get_username_and_id(message: types.Message):
    print(message.text, ' - is user\'s text')
    print(message.chat.id, ' - is user\'s chat id')
    await RegistrationStates.SharedName.set()
    await message.answer(text='Share your phone number', reply_markup=share_phone_keyboard)


@dp.message_handler(state=RegistrationStates.SharedName, content_types=types.ContentType.CONTACT)
async def get_user_phone_number(message: types.Message):
    print(message.contact.phone_number)
    await RegistrationStates.Authorized.set()
    await message.answer(text='Congrats, you are registered user')


@dp.message_handler(state=RegistrationStates.all_states, commands='clear')
async def clear_state(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(text='State has been reset')
