from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.types import ParseMode
from loguru import logger
from database.database import recording_data_of_users_who_launched_the_bot
from keyboards.user_keyboards import create_greeting_keyboard
from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"Пользователь {username} ({user_id}) запустил бота в {join_date}")
    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    greeting_keyboard = create_greeting_keyboard()
    with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
        data = (f"👤 {first_name} {last_name}, спасибо что подписались на нашего бота!\n\n"
                "🌐 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!\n"
                "📋 С полным списком услуг вы можете ознакомиться в меню бота.\n\n"
                "🔔 Обязательно подпишитесь, включите уведомления и не удаляйте этого бота из ваших чатов, и у "
                "Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, необходимую "
                "информацию и т.д.")
        await bot.send_photo(message.from_user.id, caption=data, photo=photo_file,
                             reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
