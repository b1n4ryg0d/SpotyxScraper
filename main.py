from aiogram import Bot, Dispatcher
from handlers import menu, parse, profile
from config import Config
import asyncio

async def main():
    bot = Bot(token=Config.bot_token)
    dp = Dispatcher()
    dp.include_router(menu.router, parse.router, profile.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())