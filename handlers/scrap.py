from aiogram import Router, F, types
from handlers.keyboards import scrap_keyboard_ru

router = Router()

@router.callback_query(F.data == "scraper")
async def scraper_handler(callback: types.CallbackQuery):
    await callback.message.answer("Парсер", reply_markup=await scrap_keyboard_ru())