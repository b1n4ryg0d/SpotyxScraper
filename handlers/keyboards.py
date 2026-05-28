from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

async def menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Профиль",
        callback_data="profile"))
    builder.add(types.InlineKeyboardButton(
        text="Парсер",
        callback_data="parse"))
    return builder.as_markup()

async def back_button():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="menu"
    ))
    return builder.as_markup()