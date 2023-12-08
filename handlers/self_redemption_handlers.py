from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import keyboard_to_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "self_redemption")
async def self_redemption(callback_query: types.CallbackQuery, state: FSMContext):
    """🛍 Самовыкуп"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Работаем только от 20 кг!\n\n"
                            
                            f"• Никаких комиссий за хранение товара и консолидацию на складе мы не берем.\n"
                            f"• Вы сами нашли поставщика, договорились о сотрудничестве, узнали у нас адрес и код клиента, оплатили товар, и отправили на наш склад.\n\n"

                            f"• Перед отправкой груза на наш склад, обязательно необходимо промаркировать груз кодом клиента, который мы вам присвоим, маркировка нужна для идентификации груза на складе. Грузы пришедшие без маркировки не могут быть определены, и могут не уехать в Россию.\n"
                            f"• После отправки поставщиком груза на наш склад, клиент самостоятельно контролирует трек номера и приход товара к нам на склад, когда все трек номера дошли к нам на склад, информирует менеджера об этом и присылает полный список трек номеров для сверки, также на нашем складе ведется собственный учет трек номеров по клиентам, мы фиксируем в таблице каждый трек номер пришедший на склад, мы сверяем список ваших треков с фактически пришедшими на склад, делаем для вас общую фотографию груза, согласовываем отправку и варианты упаковки.\n\n"

                            f"• После упаковки, груз отправляется в Россию.\n\n"

                            f"Если вам необходимо проверить количество товара на соответствие, мы предоставляем данную услугу, стоимость 1¥ за счетную единицу.\n\n"

                            f"Так же осуществляем проверку на брак, стоимость 1-3¥ за счетную единицу (зависит от вида и упаковки товара)\n\n"

                            f"Связаться с менеджерами: @cargo_cfb")
        main_menu_keyboard = keyboard_to_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_self_redemption_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(self_redemption)