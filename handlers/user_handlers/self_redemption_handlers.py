from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "self_redemption")
async def self_redemption(callback_query: types.CallbackQuery, state: FSMContext):
    """🛍 Самовыкуп"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/self_redemption.json")
    main_menu_keyboard = create_main_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )


class Formedit_self_redemption(StatesGroup):
    text_edit_self_redemption = State()


# Обработчик команды /edit_self_redemption (только для админа)
@router.message(Command("edit_self_redemption"))
async def edit_self_redemption(message: Message, state: FSMContext):
    """Редактирование: 🛍 Самовыкуп"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formedit_self_redemption.text_edit_self_redemption)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_self_redemption.text_edit_self_redemption)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/self_redemption.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_self_redemption_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(self_redemption)
    dp.message.register(edit_self_redemption)
