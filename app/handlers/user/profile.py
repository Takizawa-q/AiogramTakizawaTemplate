from aiogram import types
from aiogram.types import FSInputFile
from app.keyboards.inline.constructor import InlineButton, InlineKeyboardConstructor
from app.db.tables import Tables

async def profile(call: types.CallbackQuery) -> None:
    username = call.from_user.username

    kb = InlineKeyboardConstructor([
        InlineButton("🔙 Назад", "back_menu")],
        schema=[1]
    )
    await call.message.edit_text(text="\n".join([
        f"👋 Ваш юзернейм: <b>@{username}</b>",
        f"📅 Подписка активна до: <b>05.03.2024 18:35</b>"
        f"\n\n❗️ Продлить подписку: @takizawa12 "
    ]),
        reply_markup=kb)
