from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram import types
from loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    
    await message.answer(f"Hi Dear, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
