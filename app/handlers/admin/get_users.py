from aiogram.types import Message, CallbackQuery
from aiogram import Bot

async def get_users(call: CallbackQuery, callback_data: dict):
    await call.message.edit_text("тест")