from aiogram import Bot, Dispatcher
from handlers import menu, parse, profile
from config import Config
from utils import database
import asyncio

async def main():
    bot = Bot(token=Config.bot_token)
    dp = Dispatcher()
    dp.include_router(menu.router)
    dp.include_router(parse.router)
    dp.include_router(profile.router)
    await database.init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())