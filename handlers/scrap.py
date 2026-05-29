from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from fastapi.datastructures import StatesGroup, State
from handlers.keyboards import scrap_keyboard_ru
from utils.database import get_user_language

router = Router()

class ScrapFSM(StatesGroup):
    waiting_for_link = State()
    waiting_for_search_data = State()

@router.callback_query(F.data == "scraper")
async def scraper_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    if lang[0] == "ru":
        await callback.message.answer("Настройки парсера", reply_markup=scrap_keyboard_ru())
    else:
        await callback.message.answer("Parser settings", reply_markup=scrap_keyboard_ru())

@router.callback_query(F.data == "change_link")
async def change_link_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    await ScrapFSM.waiting_for_link.set()
    if lang[0] == "ru":
        await callback.message.answer("Введите ссылку для парсинга:")
    else:
        await callback.message.answer("Enter the link for parsing:")

@router.message(ScrapFSM.waiting_for_link)
async def process_link(message: types.Message, state: FSMContext):
    url = message.text
    await state.update_data(url=url)
    await ScrapFSM.waiting_for_search_data.set()
    await message.answer("Введите искомую информацию для парсинга:")

@router.message(ScrapFSM.waiting_for_search_data)
async def process_search_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    url = data.get("url")
    search_data = message.text
    #взять функцию парсера и передать ей url и искомую информацию, а потом вывести результат пользователю
    await message.answer(f"Вы ввели ссылку: {url}\nИскомая информация: {search_data}")
    await state.clear()