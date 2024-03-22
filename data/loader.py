from data.config import BOT_TOKEN
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode

video = Router()  # you can replace video to another name

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
dp.include_router(video)