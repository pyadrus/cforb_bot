from aiogram import types
from aiogram.types import ParseMode

from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    """Обработчик команды /start"""

    with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
        data = ("👤 Имя клиент, спасибо что подписались на нашего бота!\n\n"
                "🌐 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!\n"
                "📋 С полным списком услуг вы можете ознакомиться в меню бота.\n\n"
                "🔔 Обязательно подпишитесь, включите уведомления и не удаляйте этого бота из ваших чатов, и у Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, необходимую информацию и т.д.")
        await bot.send_photo(message.from_user.id, caption=data, photo=photo_file, parse_mode=ParseMode.HTML)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
