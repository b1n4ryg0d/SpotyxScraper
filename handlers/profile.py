from aiogram import Router, F, types
from handlers import keyboards
from utils.database import get_user_language

router = Router()

@router.callback_query(F.data == "profile")
async def profile_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_first_name = callback.from_user.user_first_name
    lang = await get_user_language(user_id)
    scraps_count = "В разработке.."
    if lang[0] == "ru":
        await callback.message.answer("<b>Профиль:</b>\n\n"
                                      f"<b>ID: {user_id}</b>\n"
                                      f"<b>Имя пользователя:</b> <code>{user_first_name}</code>\n"
                                      "------------------------------"
                                      f"Количество парсов: {scraps_count}", 
                                      parse_mode="HTML")
    else:
        await callback.message.answer("<b>Profile:</b>\n\n"
                                      f"<b>ID: {user_id}</b>\n"
                                      f"<b>User name:</b> <code>{user_first_name}</code>\n"
                                      "------------------------------"
                                      f"Scraps count: {scraps_count}",
                                      parse_mode="HTML")