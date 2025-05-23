from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_main_menu_keyboard
from states.states import BotContentEditStates
from system.dispatcher import ADMIN_USER_ID, bot, router
from system.working_with_files import save_bot_info, load_bot_info


@router.callback_query(F.data == "how_is_payment_made")
async def handle_payment_info_request(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Как совершается оплата?”"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/how_is_payment_made.json"),
        reply_markup=create_services_and_prices_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_how_is_payment_made (только для админа)
@router.message(Command("edit_how_is_payment_made"))
async def prompt_for_new_payment_info(message: Message, state: FSMContext):
    """Редактирование: Как совершается оплата?"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(BotContentEditStates.edit_payment_text)


@router.message(BotContentEditStates.edit_payment_text)
async def update_payment_info(message: Message, state: FSMContext):
    """Обработчик текстовых сообщений (для админа, чтобы обновить информацию)"""
    save_bot_info(message.html_text, file_path='media/messages/how_is_payment_made.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_how_is_payment_made():
    """Регистрируем handlers для бота"""
    router.message.register(handle_payment_info_request)  # Как совершается оплата?
    router.message.register(prompt_for_new_payment_info)  # Редактирование: Как совершается оплата?
    router.message.register(update_payment_info)  # Обновление: Как совершается оплата?
