import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode
from loguru import logger

from database.database import recording_data_of_users_who_launched_the_bot
from keyboards.user_keyboards import create_greeting_keyboard
from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"Пользователь {username} ({user_id}) запустил бота в {join_date}")
    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
    if user_exists:
        greeting_keyboard = create_greeting_keyboard()
        reply_markup = types.ReplyKeyboardRemove()
        await message.reply("/start", reply_markup=reply_markup)
        with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
            data = (f"<b>{first_name} {last_name}, спасибо что подписались на нашего бота!</b>\n\n"
                    "<b>🇨🇳 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!</b>\n\n"
                    "• С полным списком услуг Вы можете ознакомиться в меню бота.\n\n"
                    "Обязательно включите уведомления и не удаляйте этого бота из своих чатов!\n\n"
                    "• У Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, необходимую информацию по обновлениям и т.д.\n\n"
                    "<i>Сайт: www.cforb.ru</i>\n"
                    "<i>Telegram: https://t.me/cforb_tg</i>\n"
                    "<i>Вконтакте: https://vk.com/cforb</i>\n"
                    "<i>Instagram: https://www.instagram.com/cforb_in</i>\n"
                    "<i>YouTube: https://www.youtube.com/@cforb_tube</i>")
            await bot.send_photo(message.from_user.id, caption=data, photo=photo_file,
                                 reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)
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
                               parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True)


def create_my_details_keyboard():
    """Создает клавиатуру для кнопки 'Мои данные'"""
    my_details_keyboard = InlineKeyboardMarkup()
    my_details_button = InlineKeyboardButton(text='Регистрация', callback_data='my_details')

    my_details_keyboard.row(my_details_button)  # Связаться с оператором
    return my_details_keyboard


def check_user_exists_in_db(user_id):
    # Подключитесь к вашей базе данных
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    # Выполните SQL-запрос для проверки наличия пользователя в базе данных по его user_id
    cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (user_id,))
    # Извлеките результат запроса
    user_count = cursor.fetchone()[0]
    conn.close()
    # Если пользователь с указанным user_id найден (user_count больше 0), верните True, иначе верните False
    return user_count > 0


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
