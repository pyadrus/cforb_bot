from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import services_and_prices_key
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "services_and_prices")
async def services_and_prices(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        from_user_name = callback_query.from_user.first_name  # Получаем фамилию пользователя
        greeting_message = f"{from_user_name}, ознакомьтесь с нашими услугами и ценами!\n\n"
        services_and_prices_keyboard = services_and_prices_key()  # Клавиатуры поста приветствия 👋
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=services_and_prices_keyboard,  # Клавиатура приветствия 👋
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)

@dp.callback_query_handler(lambda c: c.data == "cargo_delivery_prices")
async def cargo_delivery_prices(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = f"после нажатия следует сообщение с фотографиями прайс-листов. И подпись: Минимальный вес на грузоперевозку 20 кг.\n\n"
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)

@dp.callback_query_handler(lambda c: c.data == "white_cargo_delivery_with_gas_turbine_engine")
async def white_cargo_delivery_with_gas_turbine_engine(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Поможем перевезти груз и пройти таможню без потерь времени и денег. Сделаем комплексную поставку: подберем транспорт, соберем документы, подадим декларацию, оформим и привезем груз на склад. Или подключимся на нужном этапе.\n\n"
                            f"• Поиск производства\n"
                            f"• Выкуп товара\n"
                            f"• Логистика\n"
                            f"• Таможенное оформление, разрешительные документы\n"
                            f"Задать вопрос или передать заявку на расчёт специалисту ВЭД : В данный момент услуга недоступна!)\n\n")
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               # reply_markup=services_and_prices_keyboard,  # Клавиатура приветствия 👋
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)

@dp.callback_query_handler(lambda c: c.data == "goods_redemption_service")
async def goods_redemption_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Работаем только от 20 кг!\n\n"
                            f"✅ Выкуп товара (условия и комиссии)\n"
                            f"Вам необходимо предоставить ссылку на поставщика, товар с фото и характеристиками, предполагаемое количество.\n"
                            f"Что дальше?\n"
                            f"•	Мы формируем корзину по вашей заявке, передаём вам на проверку собранную заявку, Вы согласовываете выкуп, оплачиваете необходимую сумму, мы выкупаем!\n\n"
                            f"Комиссия за выкуп товара составит:\n"
                            f"•	Закуп до 3.000 ¥ - комиссия 8%\n"
                            f"•	Закуп 3.000 - 5.000 ¥ - комиссия 5%\n"
                            f"•	Закуп 5.000 - 10.000 ¥ - комиссия 4%\n"
                            f"•	Закуп 10.000 - 50.000 ¥ - комиссия 3%\n"
                            f"•	Закуп свыше 50.000 ¥ - комиссия 2%\n\n"
                            f"Минимальная сумма на выкуп 1000¥, минимальный вес груза на доставку через нас 20 кг.\n\n"
                            f"Что входит в комиссию:\n"
                            f"Формирование, размещение и оплата заказа, общение с поставщиком если есть какие-то трудности с заказом, согласовываем остатки с поставщиком (если поставщик не может выполнить заказ, формируем заявку на возврат), делаем фото и видео (из одной коробки - 1 единица товара), хранение товара на складе до момента отправки.\n\n"
                            f"✅ Дополнительная услуга: наклейки со штрих кодами на товар для маркетплейсов от 100-300 шт 1 юань (по курсу).\n"
                            f"✅ Дополнительная услуга: проверка количества товара на соответствие, если выкупаете сами 1-2 юаня за 1 счетную единицу (зависит от упаковки товара).\n\n"
                            f"Если выкупаем Мы 0.5 - 1 юань (зависит от упаковки товара)\n"
                            f"❗️ Мы отвечаем за:\n"
                            f"* Выкуп товара согласно заявке\n"
                            f"* Доставку груза по всем трек-номерам на наш склад в Китае\n"
                            f"* Консолидацию груза\n"
                            f"* Упаковку груза согласно требованиям\n"
                            f"* Доставку груза в РФ (г. Москва)\n\n"
                            f"❗️ Работая с вашим поставщиком мы не несем ответственности за:\n"
                            f"* Качество его продукции\n"
                            f"* Срок обработки, изготовления и отправки товара поставщиками на наш склад в Китае\n"
                            f"* Бракованный товар - компания не проверяет товар на наличие явных и скрытых дефектов (Данную услугу можно запросить, оплачивается отдельно).\n"
                            f"* Цвет товара - цветопередача фотографии может отличаться от реального цвета товара. \n"
                            f"* Отправку поставщиком не того товара, который был заказан (если не заказана услуга проверки соответствия)\n"
                            f"* Отправку поставщиком товара другого размера\n")
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)

def register_services_and_prices_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(services_and_prices)
    dp.register_message_handler(cargo_delivery_prices)
    dp.register_message_handler(white_cargo_delivery_with_gas_turbine_engine)
    dp.register_message_handler(goods_redemption_service)
