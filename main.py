from asyncio import run
from logging import basicConfig, INFO
from sys import stdout

import handlers, utils 
from config import BOT_TOKEN
from loader import dp, bot



async def main() -> None:

    await dp.start_polling(bot)

if __name__ == "__main__":
    basicConfig(level=INFO, stream=stdout)
    run(main())