from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import keyboard_to_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "useful_information")
async def useful_information(callback_query: types.CallbackQuery, state: FSMContext):
    """📚 Полезная информация"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"<b>Специально для Вас, наша компанию подготовила статьи с полезной информацией, это облегчит наше сотрудничество, и поможет вам разобраться в некоторых вопросах!\n\n</b>"

                            f"Как принимать груз в России - переводит на сайт со статьей\n"
                            f"Путь товара из Китая в Россию - переводит на сайт со статьей\n"
                            f"Информация для Самовыкупов - переводит на сайт со статьей\n"
                            f"Информация если Выкуп делаем Мы - переводит на сайт со статьей\n"
                            f"Плюсы самостоятельного поиска товара - переводит на сайт со статьей\n"
                            f"Какие могут быть претензии по работе? - переводит на сайт со статьей\n"
                            f"Как выбирать товары и не ошибиться? - переводит на сайт со статьей\n"
                            f"Документы на товар - переводит на сайт со статьей\n"
                            f"Заказ и проверка образцов - переводит на сайт со статьей\n\n"
                            f"Связаться с менеджерами: @cargo_cfb")
        main_menu_keyboard = keyboard_to_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_useful_information_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(useful_information)