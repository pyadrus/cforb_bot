from aiogram import types, F
from aiogram.fsm.context import FSMContext

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info


@router.callback_query(F.data == "reviews")
async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    """💌 Отзывы"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/reviews.json")
    main_menu_keyboard = create_main_menu_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )


def register_reviews_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(reviews)
