from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    Start = State()
    SharedName = State()
    Authorized = State()
