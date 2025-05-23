import os

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards.user_keyboards import (create_services_and_prices_keyboard,
                                                     create_services_and_prices_main_menu_keyboard,
                                                     get_price_lists_keyboard)
from states.states import (FileStates, FormeditMainMenu)
from system.dispatcher import ADMIN_USER_ID, bot, dp, router
from system.working_with_files import load_bot_info, save_bot_info


@router.callback_query(F.data == "services_and_prices")
async def services_and_prices(callback_query: types.CallbackQuery, state: FSMContext):
    """Услуги и цены"""
    try:
        await state.clear()  # Очищаем состояние
        await bot.edit_message_media(
            media=InputMediaPhoto(media=FSInputFile('media/photos/services_and_prices.jpg'),
                                  caption=load_bot_info(
                                      messages="media/messages/services_prices_messages/services_and_prices.json"),
                                  parse_mode="HTML"),
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=create_services_and_prices_keyboard(),
        )
    except Exception as error:
        logger.exception(error)


# Обработчик команды /edit_services_and_prices (только для админа)
@router.message(Command("edit_services_and_prices"))
async def edit_services_and_prices(message: Message, state: FSMContext):
    """Редактирование: Услуги и цены"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_services_and_prices)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_services_and_prices)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/services_prices_messages/services_and_prices.json')
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@dp.message(Command("get_price_lists_file"))
async def get_price_lists_photo_1(message: types.Message, state: FSMContext):
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новый файл 'Прейскурант CFORB.xlsx'.")
    await state.set_state(FileStates.waiting_for_file)


@dp.message(FileStates.waiting_for_file, F.document)
async def replace_photo_1(message: types.Message, state: FSMContext):
    document = message.document

    if document.file_name.endswith('.xlsx'):
        file_info = await bot.get_file(document.file_id)
        new_file_path = os.path.join("media/document", 'Прейскурант CFORB.xlsx')
        await bot.download_file(file_info.file_path, new_file_path)
        await message.answer("Файл 'Прейскурант CFORB.xlsx' успешно заменен!")
        await state.clear()
    else:
        await message.answer("Пожалуйста, отправьте файл в формате .xlsx.")


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "cargo_delivery_prices")
async def cargo_delivery_prices(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Прайсы на доставку Карго”"""
    try:
        await state.clear()  # Очищаем состояние
        await bot.send_document(chat_id=callback_query.message.chat.id,
                                document=FSInputFile('media/document/Прейскурант CFORB.xlsx'),
                                reply_markup=get_price_lists_keyboard(),
                                caption=load_bot_info(messages="media/messages/cargo_delivery_prices.json"),
                                parse_mode="HTML")
    except Exception as error:
        logger.exception(error)


# Обработчик команды /edit_cargo_delivery_prices (только для админа)
@router.message(Command("edit_cargo_delivery_prices"))
async def edit_cargo_delivery_prices(message: Message, state: FSMContext):
    """Редактирование: Прайсы на доставку Карго"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_cargo_delivery_prices)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_cargo_delivery_prices)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/cargo_delivery_prices.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "goods_redemption_service")
async def goods_redemption_service(callback_query: types.CallbackQuery, state: FSMContext):
    """Услуга Выкупа товаров"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/goods_redemption_service.json"),
        reply_markup=create_services_and_prices_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_goods_redemption_service (только для админа)
@router.message(Command("edit_goods_redemption_service"))
async def edit_goods_redemption_service(message: Message, state: FSMContext):
    """Редактирование: Услуга Выкупа товаров"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_goods_redemption_service)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_goods_redemption_service)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/goods_redemption_service.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "product_search_service")
async def product_search_service(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Услуга Поиска товаров (производителей в Китае)”"""
    try:
        await state.clear()  # Очищаем состояние
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=load_bot_info(messages="media/messages/product_search_service.json"),
            reply_markup=create_services_and_prices_main_menu_keyboard(),
            parse_mode="HTML"
        )
    except Exception as error:
        logger.exception(error)


# Обработчик команды /edit_product_search_service (только для админа)
@router.message(Command("edit_product_search_service"))
async def edit_product_search_service(message: Message, state: FSMContext):
    """Редактирование: Услуга Поиска товаров (производителей в Китае)"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_product_search_service)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_product_search_service)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/product_search_service.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "wechat_registration_service")
async def wechat_registration_service(callback_query: types.CallbackQuery, state: FSMContext):
    """Услуга регистрации на WeChat"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/wechat_registration_service.json"),
        reply_markup=create_services_and_prices_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_wechat_registration_service (только для админа)
@router.message(Command("edit_wechat_registration_service"))
async def edit_wechat_registration_service(message: Message, state: FSMContext):
    """Редактирование: Услуга регистрации на WeChat"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_wechat_registration_service)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_wechat_registration_service)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/wechat_registration_service.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "purchase_a_supplier_database")
async def purchase_a_supplier_database(callback_query: types.CallbackQuery, state: FSMContext):
    """Приобрести базу данных поставщиков"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/purchase_a_supplier_database.json"),
        reply_markup=create_services_and_prices_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_purchase_a_supplier_database (только для админа)
@router.message(Command("edit_purchase_a_supplier_database"))
async def edit_purchase_a_supplier_database(message: Message, state: FSMContext):
    """Редактирование: Приобрести базу данных поставщиков"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_purchase_a_supplier_database)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_purchase_a_supplier_database)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/purchase_a_supplier_database.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "what_payments_await_me")
async def what_payments_await_me(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Какие платежи меня ожидают?”"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/what_payments_await_me.json"),
        reply_markup=create_services_and_prices_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_what_payments_await_me (только для админа)
@router.message(Command("edit_what_payments_await_me"))
async def edit_what_payments_await_me(message: Message, state: FSMContext):
    """Редактирование: Какие платежи меня ожидают?"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_what_payments_await_me)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_what_payments_await_me)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/what_payments_await_me.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_services_and_prices_handler():
    """Регистрируем handlers для бота"""
    router.message.register(services_and_prices)
    router.message.register(cargo_delivery_prices)
    router.message.register(goods_redemption_service)
    router.message.register(product_search_service)
    router.message.register(wechat_registration_service)
    router.message.register(purchase_a_supplier_database)
    router.message.register(what_payments_await_me)

    router.message.register(edit_what_payments_await_me)  # Редактирование: Какие платежи меня ожидают?
    router.message.register(edit_purchase_a_supplier_database)  # Редактирование: Приобрести базу данных поставщиков
    router.message.register(edit_wechat_registration_service)  # Редактирование: Услуга регистрации на WeChat
    router.message.register(
        edit_product_search_service)  # Редактирование: Услуга Поиска товаров (производителей в Китае)
    router.message.register(edit_goods_redemption_service)  # Редактирование: Услуга Выкупа товаров
    router.message.register(edit_cargo_delivery_prices)  # Редактирование: Прайсы на доставку Карго
    router.message.register(edit_services_and_prices)  # Редактирование: Услуги и цены

    """Редактирование фото"""
    router.message.register(get_price_lists_photo_1)
