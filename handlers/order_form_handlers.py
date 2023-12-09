from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import keyboard_to_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "order_form")
async def order_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Бланк заказа"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"<b>Скачайте и заполните наш фирменный бланк заказа, если возникнут какие-то вопросы, "
                            f"вы всегда можете обратиться к менеджеру @cargo_cfb.</b>\n\n"
                            f"Пароль к бланку - cforb\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n"
                            f"ПРИКРЕПЛЯЕТСЯ ФАЙЛ БЛАНК ЗАКАЗА")
        main_menu_keyboard = keyboard_to_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_order_form_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(order_form)
