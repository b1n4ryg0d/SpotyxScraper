from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

async def select_language_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Русский",
        callback_data="language_ru"
    ))
    builder.add(types.InlineKeyboardButton(
        text="English",
        callback_data="language_en"
    ))
    return builder.as_markup()

async def menu_keyboard_ru():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Профиль",
        callback_data="profile"))
    builder.add(types.InlineKeyboardButton(
        text="Парсер",
        callback_data="scraper"))
    return builder.as_markup()

async def menu_keyboard_en():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Profile",
        callback_data="profile"))
    builder.add(types.InlineKeyboardButton(
        text="Scraper",
        callback_data="scraper"))
    return builder.as_markup()

async def back_button_ru():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="menu"
    ))
    return builder.as_markup()

async def back_button_en():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Back",
        callback_data="menu"
    ))
    return builder.as_markup()

async def scrap_keyboard_ru():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ссылка",
        callback_data="change_link"
    ),
    types.InlineKeyboardButton(
        text="Искомая информация",
        callback_data="search_data"
    ),
    types.InlineKeyboardButton(
        text="Начать парсинг",
        callback_data="start_scraping"
    ))
    builder.adjust(2, 1)
    return builder.as_markup()