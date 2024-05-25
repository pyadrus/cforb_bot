# from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger
import json
from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("media/messages/self_redemption.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "self_redemption")
async def self_redemption(callback_query: types.CallbackQuery, state: FSMContext):
    """🛍 Самовыкуп"""
    # try:
    await state.clear()  # Очищаем состояние
    data = load_bot_info()
    main_menu_keyboard = create_main_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )
    # except Exception as error:
    #     logger.exception(error)


def register_self_redemption_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(self_redemption)
