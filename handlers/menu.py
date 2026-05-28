from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from utils.database import get_user, create_user
from . import keyboards

router = Router()

@router.callback_query(F.data == "menu")
@router.message(CommandStart())
async def start_handler(event: types.Message | types.CallbackQuery):
    user_id = event.from_user.id
    user_data = await get_user(user_id)
    if isinstance(event, types.Message):
        answer_method = event.answer
    else:
        answer_method = event.message.answer
        await event.answer()
    
    if not user_data:
        await answer_method(
            "<b>Добро пожаловать в SpotyxScraper!</b>\n"
            "Для продолжения работы выберите язык.\n\n"
            "<b>Welcome to SpotyxScraper</b>\n"
            "To continue, select language.",
            reply_markup=await keyboards.select_language_keyboard(),
            parse_mode="HTML"
        )
    else:
        if user_data[1] == "ru":
            await answer_method("<b>SpotyxScraper</b>\nДля работы используйте кнопки ниже.",
                                reply_markup=await keyboards.menu_keyboard(),
                                parse_mode="HTML")
        else:
            await answer_method("<b>SpotyxScraper</b>\nTo work use buttons below.",
                                reply_markup=await keyboards.menu_keyboard(),
                                parse_mode="HTML")

@router.callback_query(F.data.startswith("language_"))
async def select_language_handler(callback: types.CallbackQuery):
    language = callback.data.split("_")[1]
    user_id = callback.from_user.id
    first_name = callback.from_user.first_name
    await create_user(user_id=user_id, user_first_name=first_name, user_language=language)
    await callback.message.delete()
    if language == "ru":
        await callback.bot.send_message(chat_id=user_id, text="<b>Был выбран русский язык!</b>\nЧтобы перейти в меню, нажмите кнопку ниже.",
                                    reply_markup=await keyboards.back_button(),
                                    parse_mode="HTML")
    elif language == "en":
        await callback.bot.send_message(chat_id=user_id, text="<b>English language selected</b>\nTo go to the menu, click the button below.",
                                    reply_markup=await keyboards.back_button(),
                                    parse_mode="HTML")
    await callback.answer()