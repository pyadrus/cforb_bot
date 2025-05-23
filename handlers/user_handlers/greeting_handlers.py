import os
from datetime import datetime

from aiogram import types, F
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from database.database import check_user_exists_in_db
from database.database import get_user_data_from_db
from database.database import insert_user_data_to_database
from database.database import recording_data_of_users_who_launched_the_bot
from database.database import update_city_in_db
from database.database import update_name_in_db
from database.database import update_phone_in_db
from database.database import update_surname_in_db
from keyboards.user_keyboards.user_keyboards import create_contact_keyboard
from keyboards.user_keyboards.user_keyboards import create_data_modification_keyboard
from keyboards.user_keyboards.user_keyboards import create_greeting_keyboard
from keyboards.user_keyboards.user_keyboards import create_my_details_keyboard
from keyboards.user_keyboards.user_keyboards import create_sign_up_keyboard
from states.states import FormeditMainMenu, ChangingData, MakingAnOrder
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.message(Command("greeting_photo"))
async def greeting_photo(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате jpg")


@router.message(F.photo)
async def replace_photo(message: types.Message):
    # Получаем файл фотографии
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    new_photo_path = os.path.join("media/photos/", 'greeting.jpg')
    # Загружаем файл на диск
    await message.bot.download_file(file_info.file_path, new_photo_path)
    await message.answer("Фото успешно заменено!")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_date = message.date.strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"{user_id} {user_name} {user_first_name} {user_last_name} {user_date}")
    recording_data_of_users_who_launched_the_bot(user_id, user_name, user_first_name, user_last_name, user_date)

    user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
    if user_exists:
        main_menu_key = create_greeting_keyboard()

        document = FSInputFile('media/photos/greeting.jpg')
        data = load_bot_info(messages="media/messages/main_menu_messages.json")
        await message.answer_photo(photo=document, caption=data,
                                   reply_markup=main_menu_key,
                                   parse_mode="HTML")
    else:
        # Если пользователя нет в базе данных, предлагаем пройти регистрацию
        sign_up_text = ("⚠️ <b>Вы не зарегистрированы в нашей системе</b> ⚠️\n\n"
                        "Для доступа к этому разделу, пожалуйста, <b>зарегистрируйтесь</b>.\n\n"
                        "Для перехода в начальное меню нажмите /start")

        # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
        my_details_key = create_my_details_keyboard()
        # Отправляем сообщение с предложением зарегистрироваться и клавиатурой
        await bot.send_message(message.from_user.id, sign_up_text,
                               reply_markup=my_details_key,
                               disable_web_page_preview=True)


# Обработчик команды /edit_main_menu (только для админа)
@router.message(Command("edit_main_menu"))
async def edit_main_menu(message: Message, state: FSMContext):
    """Редактирование: Бланк заказа"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.text_edit_main_menu)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.text_edit_main_menu)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/main_menu_messages.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


@router.callback_query(F.data == "main_menu")
async def send_start(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    try:
        await state.clear()  # Очищаем состояние
        # Получаем информацию о пользователе
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username

        logger.info(f"Пользователь {username} ({user_id}) вернулся в начальное меню")

        user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
        if user_exists:
            greeting_keyboard = create_greeting_keyboard()
            document = FSInputFile('media/photos/greeting.jpg')
            data = load_bot_info(messages="media/messages/main_menu_messages.json")
            media = InputMediaPhoto(media=document, caption=data, parse_mode="HTML")
            await bot.edit_message_media(media=media,
                                         chat_id=callback_query.message.chat.id,
                                         message_id=callback_query.message.message_id,
                                         reply_markup=greeting_keyboard,
                                         )
        else:
            # Если пользователя нет в базе данных, предлагаем пройти регистрацию
            sign_up_text = ("⚠️ <b>Вы не зарегистрированы в нашей системе</b> ⚠️\n\n"
                            "Для доступа к этому разделу, пожалуйста, <b>зарегистрируйтесь</b>.\n\n"
                            "Для перехода в начальное меню нажмите /start")

            # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
            my_details_key = create_my_details_keyboard()
            # Отправляем сообщение с предложением зарегистрироваться и клавиатурой
            await bot.send_message(callback_query.from_user.id, sign_up_text,
                                   reply_markup=my_details_key,
                                   disable_web_page_preview=True)
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "my_details")
async def call_us_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id  # Получаем ID текущего пользователя
    user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных

    if user_data:
        # Если данные о пользователе найдены в базе данных, отобразите их
        name = user_data.get('name', 'не указано')
        surname = user_data.get('surname', 'не указано')
        city = user_data.get('city', 'не указано')
        phone_number = user_data.get('phone_number', 'не указано')
        registration_date = user_data.get('registration_date')

        text_mes = (f"🤝 Добро пожаловать, {name} {surname}!\n"
                    "Ваши данные:\n\n"
                    f"✅ <b>Имя:</b> {name}\n"
                    f"✅ <b>Фамилия:</b> {surname}\n"
                    f"✅ <b>Город:</b> {city}\n"
                    f"✅ <b>Номер телефона:</b> {phone_number}\n"
                    f"✅ <b>Дата регистрации:</b> {registration_date}\n\n")
        edit_data_keyboard = create_data_modification_keyboard()
        await bot.send_message(callback_query.from_user.id, text_mes,
                               reply_markup=edit_data_keyboard,
                               )
    else:
        # Если данные о пользователе не найдены, предложите пройти регистрацию
        keyboards_sign_up = create_sign_up_keyboard()
        sign_up_text = ("👋 Предлагаем нам с Вами познакомиться!\n\n"
                        "Информация о Ваших Ф.И.О., городе и номере телефона нужны для оптимизации и персонализации "
                        "работы нашего бота под наших клиентов.\n\n"
                        "Для возврата нажмите /start")
        await bot.send_message(callback_query.from_user.id, sign_up_text,
                               reply_markup=keyboards_sign_up,
                               disable_web_page_preview=True)


@router.callback_query(F.data == "edit_name")
async def edit_name_handler(callback_query: types.CallbackQuery, state: FSMContext):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новое имя:")
    await state.set_state(ChangingData.changing_name)


@router.message(ChangingData.changing_name)
async def process_entered_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    new_name = message.text
    if update_name_in_db(user_id, new_name):
        text_name = f"✅ Имя успешно изменено на {new_name} ✅\n\n" \
                    "Для возврата нажмите /start"
        await bot.send_message(user_id, text_name)
    else:
        text_name = "❌ Произошла ошибка при изменении имени ❌\n\n" \
                    "Для возврата нажмите /start"
        await bot.send_message(user_id, text_name)
    # Завершаем состояние после изменения имени
    await state.clear()


@router.callback_query(F.data == "edit_surname")
async def edit_surname_handler(callback_query: types.CallbackQuery, state: FSMContext):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новую фамилию:")
    await state.set_state(ChangingData.changing_surname)


@router.message(ChangingData.changing_surname)
async def process_entered_edit_surname(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    new_surname = message.text
    if update_surname_in_db(user_id, new_surname):
        text_surname = f"✅ Фамилия успешно изменена на {new_surname} ✅\n\n" \
                       "Для возврата нажмите /start"
        await bot.send_message(user_id, text_surname)
    else:
        text_surname = "❌ Произошла ошибка при изменении фамилии ❌\n\n" \
                       "Для возврата нажмите /start"
        await bot.send_message(user_id, text_surname)
    # Завершаем состояние после изменения имени
    await state.clear()


@router.callback_query(F.data == "edit_city")
async def edit_city_handler(callback_query: types.CallbackQuery, state: FSMContext):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новый город:")
    await state.set_state(ChangingData.changing_city)


@router.message(ChangingData.changing_city)
async def process_entered_edit_city(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    new_city = message.text
    if update_city_in_db(user_id, new_city):
        text_city = f"✅ Город успешно изменен на {new_city} ✅\n\n" \
                    "Для возврата нажмите /start"
        await bot.send_message(user_id, text_city)
    else:
        text_city = "❌ Произошла ошибка при изменении города ❌\n\n" \
                    "Для возврата нажмите /start"
        await bot.send_message(user_id, text_city)
    # Завершаем состояние после изменения имени
    await state.clear()


@router.callback_query(F.data == "edit_phone")
async def edit_city_handler(callback_query: types.CallbackQuery, state: FSMContext):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новый номер телефона:")
    await state.set_state(ChangingData.changing_phone)


@router.message(ChangingData.changing_phone)
async def process_entered_edit_city(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    new_phone = message.text
    if update_phone_in_db(user_id, new_phone):
        text_phone = f"✅ Номер телефона успешно изменен на {new_phone} ✅\n\n" \
                     "Для возврата нажмите /start"
        await bot.send_message(user_id, text_phone)
    else:
        text_phone = "❌ Произошла ошибка при изменении номера телефона ❌\n\n" \
                     "Для возврата нажмите /start"
        await bot.send_message(user_id, text_phone)
    # Завершаем состояние после изменения имени
    await state.clear()


@router.callback_query(F.data == "agree")
async def agree_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()  # Очищаем состояние
    await state.set_state(MakingAnOrder.write_surname)
    text_mes = ("👥 Введите вашу фамилию (желательно кириллицей):\n"
                "Пример: Петров, Иванова, Сидоренко")
    await bot.send_message(callback_query.from_user.id, text_mes)


@router.message(MakingAnOrder.write_surname)
async def write_surname_handler(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await state.set_state(MakingAnOrder.write_name)
    text_mes = ("👤 Введите ваше имя (желательно кириллицей):\n"
                "Пример: Иван, Ольга, Анастасия")
    await bot.send_message(message.from_user.id, text_mes)


@router.message(MakingAnOrder.write_name)
async def write_city_handlers(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(MakingAnOrder.write_city)
    text_mes = ("🏙️ Введите ваш город (желательно кириллицей):\n"
                "Пример: Москва, Санкт-Петербург")
    await bot.send_message(message.from_user.id, text_mes)


@router.message(MakingAnOrder.write_city)
async def write_name_handler(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    sign_up_texts = (
        "Для ввода номера телефона вы можете поделиться номером телефона, нажав на кнопку или ввести его вручную.\n\n"
        "Чтобы ввести номер вручную, просто отправьте его в текстовом поле.")
    contact_keyboard = create_contact_keyboard()
    await bot.send_message(message.from_user.id, sign_up_texts,
                           reply_markup=contact_keyboard,  # Установить пользовательскую клавиатуру
                           disable_web_page_preview=True)
    await state.set_state(MakingAnOrder.phone_input)


@router.message(StateFilter(MakingAnOrder.phone_input), F.contact)
async def handle_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


@router.message(StateFilter(MakingAnOrder.phone_input), lambda message: message.text and not message.contact)
async def handle_phone_text(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


async def handle_confirmation(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardRemove(selective=False)  # Remove the keyboard
    await message.answer("Спасибо за предоставленные данные.", reply_markup=markup)
    # Извлечение пользовательских данных из состояния
    user_data = await state.get_data()
    surname = user_data.get('surname', 'не указан')
    name = user_data.get('name', 'не указан')
    phone_number = user_data.get('phone_number', 'не указан')
    city = user_data.get('city', 'не указан')
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Получение ID аккаунта Telegram
    user_id = message.from_user.id
    # Составьте подтверждающее сообщение
    text_mes = (f"🤝 Рады познакомиться {name} {surname}! 🤝\n"
                "Ваши регистрационные данные:\n\n"
                f"✅ <b>Ваше Имя:</b> {name}\n"
                f"✅ <b>Ваша Фамилия:</b> {surname}\n"
                f"✅ <b>Ваш Город:</b> {city}\n"
                f"✅ <b>Ваш номер телефона:</b> {phone_number}\n"
                f"✅ <b>Ваша Дата регистрации:</b> {registration_date}\n\n"
                "Вы можете изменить свои данные в меню \"Мои данные\".\n\n"
                "Для возврата нажмите /start")
    insert_user_data_to_database(user_id, name, surname, city, phone_number, registration_date)
    await state.clear()
    # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
    await bot.send_message(message.from_user.id, text_mes)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(send_start)  # Обработчик команды /start, он же пост приветствия 👋
    dp.message.register(command_start_handler)  # Обработчик команды /start, он же пост приветствия 👋

    dp.message.register(edit_main_menu)  # редактирование меню бота

    """Редактирование фото"""
    dp.message.register(greeting_photo)  # редактирование меню бота
