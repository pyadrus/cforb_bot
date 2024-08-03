from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_main_menu_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "supplier_inspection")
async def handle_supplier_inspection(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Инспекция поставщиков по провинциям (выезд на производство)”"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/services_prices_messages/supplier_inspection.json")
    main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard,
        parse_mode="HTML"
    )


class EditSupplierInspectionState(StatesGroup):
    edit_text = State()


# Обработчик команды /edit_supplier_inspection (только для админа)
@router.message(Command("edit_supplier_inspection"))
async def cmd_edit_supplier_inspection(message: Message, state: FSMContext):
    """Редактирование: Инспекция поставщиков по провинциям (выезд на производство)"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(EditSupplierInspectionState.edit_text)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(EditSupplierInspectionState.edit_text)
async def update_supplier_inspection_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/services_prices_messages/supplier_inspection.json')
    await message.reply("Информация обновлена.")
    await state.clear()


def register_handle_supplier_inspection():
    """Регистрируем handlers для бота"""
    dp.message.register(handle_supplier_inspection)
    dp.message.register(cmd_edit_supplier_inspection)
