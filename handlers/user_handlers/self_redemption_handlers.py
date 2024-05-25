# from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


@router.callback_query(F.data == "self_redemption")
async def self_redemption(callback_query: types.CallbackQuery, state: FSMContext):
    """🛍 Самовыкуп"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        greeting_message = (f"Работаем только от 20 кг!\n\n"
                            f"• Никаких комиссий за хранение товара и консолидацию на складе мы не берем.\n"
                            f"• Вы сами нашли поставщика, договорились о сотрудничестве, узнали у нас адрес и код "
                            f"клиента, оплатили товар, и отправили на наш склад.\n"
                            f"• Перед отправкой груза на наш склад, обязательно необходимо промаркировать груз кодом "
                            f"клиента, который мы вам присвоим, маркировка нужна для идентификации груза на складе. "
                            f"Грузы пришедшие без маркировки не могут быть определены, и могут не уехать в Россию.\n"
                            f"• После отправки поставщиком груза на наш склад, клиент самостоятельно контролирует "
                            f"трек номера и приход товара к нам на склад, когда все трек номера дошли к нам на склад, "
                            f"информирует менеджера об этом и присылает полный список трек номеров для сверки, также "
                            f"на нашем складе ведется собственный учет трек номеров по клиентам, мы фиксируем в "
                            f"таблице каждый трек номер пришедший на склад, мы сверяем список ваших треков с "
                            f"фактически пришедшими на склад, делаем для вас общую фотографию груза, согласовываем "
                            f"отправку и варианты упаковки.\n"
                            f"• После упаковки, груз отправляется в Россию.\n\n"

                            f"Если вам необходимо проверить количество товара на соответствие, мы предоставляем "
                            f"данную услугу, стоимость 1¥ за счетную единицу.\n\n"

                            f"Так же осуществляем проверку на брак, стоимость 1-3¥ за счетную единицу (зависит от "
                            f"вида и упаковки товара)\n\n"

                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        main_menu_keyboard = create_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_self_redemption_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(self_redemption)
