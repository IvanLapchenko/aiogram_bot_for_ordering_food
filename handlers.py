from aiogram import types
from aiogram.dispatcher import FSMContext
from states import RegistrationStates
from keyboards import share_phone_keyboard, first_step_kb
from app import dp
from database import create_user_with_name_and_tg_id, add_user_phone, get_all_items_for_category, \
                     is_user_registered


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_tg_id = message.from_user.id
    if is_user_registered(user_tg_id):
        await RegistrationStates.Authorized.set()
        await message.answer(f'Hello, {message.from_user.full_name}. Choose what you\'d want to eat:)',
                             reply_markup=first_step_kb)
    else:
        await RegistrationStates.Start.set()
        await message.answer(f'Hello, {message.from_user.full_name}. To order food you have to register. '
                             f'To proceed, enter your full name')


@dp.message_handler(state=RegistrationStates.Start)
async def get_username_and_id(message: types.Message):
    create_user_with_name_and_tg_id(message.text, message.from_user.id)
    await RegistrationStates.SharedName.set()
    await message.answer(text='Share your phone number', reply_markup=share_phone_keyboard)


@dp.message_handler(state=RegistrationStates.SharedName, content_types=types.ContentType.CONTACT)
async def get_user_phone_number(message: types.Message):
    add_user_phone(message.contact.phone_number, message.from_user.id)
    await RegistrationStates.Authorized.set()
    await message.answer(text='Congrats, you are registered user. Choose what you\'d want to eat:)',
                         reply_markup=first_step_kb)


@dp.message_handler(state=RegistrationStates.Authorized, text=['Sushi', 'Sets', 'Rolls'])
async def choose_category(message: types.Message):
    category_name = message.text.lower()
    list_of_all_products_in_category = await get_all_items_for_category(category_name)
    menu_text = '\n'.join([f"{item[0]} - {item[1]}, Ціна: {item[2]}" for item in list_of_all_products_in_category[0:10]])
    await message.answer(text=menu_text)


@dp.message_handler(state=RegistrationStates.all_states, commands='clear')
async def clear_state(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(text='State has been reset')



