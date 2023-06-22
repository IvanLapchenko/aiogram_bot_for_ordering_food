from aiogram.dispatcher import FSMContext

from config import BOT_TOKEN
from aiogram import executor
from service import set_default_commands
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# default startup function
async def on_startup(dispatcher):
    # set default commands
    print('Bot launched')
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)



