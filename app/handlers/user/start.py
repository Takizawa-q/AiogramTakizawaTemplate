from aiogram import types
from app.keyboards.inline.constructor import InlineKeyboardConstructor, InlineButton
from aiogram import F
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from app.states.user import Menu


async def start(update: types.Update, state: FSMContext) -> None:
    await state.set_state(Menu.menu)
    if isinstance(update, types.CallbackQuery):
        method = update.message.edit_text
    else:
        method = update.answer
    # await state.clear() - ОЧИСТИТЬ STATE
    # await state.update_data(main_message_id=main_message_id.message_id) ЗАПИСАТЬ ЛЮБЫЕ ДАННЫЕ В STATE
    # data = await state.get_data() ЧТОБЫ ПОЛУЧИТЬ ДАННЫЕ ИЗ СТЕЙТА
    kb = InlineKeyboardConstructor([
        InlineButton("💼 Личный Кабинет", "user_profile"),
        InlineButton("⚙️ Настройки", "user_settings"),
        InlineButton("🚀 Запуск парсера", "user_start"),
    ], schema=[1, 1, 1])

    await method("\n".join(
        ["Бот успешно запущен!👍",
                     "\n<b>⚙️ Настройки</b> - настройки для цены, кешбека",
                     "<b>💼 Личный кабинет</b> - дата окончания подписки"]),
                     reply_markup=kb)
    

