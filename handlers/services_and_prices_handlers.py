from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import services_and_prices_key, keyboard_to_services_and_prices_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "services_and_prices")
async def services_and_prices(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        # from_user_name = callback_query.from_user.first_name  # Получаем фамилию пользователя
        greeting_message = (f"<b>В данном меню представлена основная информация по услугам и ценам.</b>\n\n"
                            f"• Прайсы на доставку Карго\n"
                            f"• Белая доставка грузов с ГТД и всей документацией\n"
                            f"• Услуга Выкупа товаров\n"
                            f"• Услуга Поиска товаров (производителей в Китае)\n"
                            f"• Инспекция поставщиков по провинциям (выезд на производство)\n"
                            f"• Услуга регистрации WeChat\n"
                            f"• Приобрести базу поставщиков\n"
                            f"• Какие платежи меня ожидают?\n"
                            f"• Как совершается оплата?\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n")
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
        greeting_message = (f"Актуальные прайс-листы CFORB, сохраняйте чтоб не потерять!\n\n"
                            f"Связаться с менеджерами: @cargo_cfb")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "white_cargo_delivery_with_gas_turbine_engine")
async def white_cargo_delivery_with_gas_turbine_engine(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"<b>Поможем перевезти груз и пройти таможню без потерь времени и денег. Сделаем комплексную поставку: "
            f"подберем транспорт, соберем документы, подадим декларацию, оформим и привезем груз на склад. Или "
            f"подключимся на нужном этапе.</b>\n\n"
            f"• Поиск производства\n"
            f"• Выкуп товара\n"
            f"• Логистика\n"
            f"• Таможенное оформление, разрешительные документы\n"
            f"<b>Задать вопрос или передать заявку на расчет специалисту ВЭД: @cargo_cfb</b>\n\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
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
                            f"Вам необходимо предоставить ссылку на поставщика, товар с фото и характеристиками, "
                            f"предполагаемое количество.\n"
                            f"Что дальше?\n"
                            f"•	Мы формируем корзину по вашей заявке, передаём вам на проверку собранную заявку, Вы "
                            f"согласовываете выкуп, оплачиваете необходимую сумму, мы выкупаем!\n\n"
                            f"Комиссия за выкуп товара составит:\n"
                            f"•	Закуп до 3.000 ¥ - комиссия 8%\n"
                            f"•	Закуп 3.000 - 5.000 ¥ - комиссия 5%\n"
                            f"•	Закуп 5.000 - 10.000 ¥ - комиссия 4%\n"
                            f"•	Закуп 10.000 - 50.000 ¥ - комиссия 3%\n"
                            f"•	Закуп свыше 50.000 ¥ - комиссия 2%\n\n"
                            f"Минимальная сумма на выкуп 1000¥, минимальный вес груза на доставку через нас 20 кг.\n\n"
                            f"Что входит в комиссию:\n"
                            f"Формирование, размещение и оплата заказа, общение с поставщиком если есть какие-то "
                            f"трудности с заказом, согласовываем остатки с поставщиком (если поставщик не может "
                            f"выполнить заказ, формируем заявку на возврат), делаем фото и видео (из одной коробки - "
                            f"1 единица товара), хранение товара на складе до момента отправки.\n\n"
                            f"✅ Дополнительная услуга: наклейки со штрих кодами на товар для маркетплейсов от 100-300 "
                            f"шт 1 юань (по курсу).\n"
                            f"✅ Дополнительная услуга: проверка количества товара на соответствие, если выкупаете "
                            f"сами 1-2 юаня за 1 счетную единицу (зависит от упаковки товара).\n\n"
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
                            f"* Бракованный товар - компания не проверяет товар на наличие явных и скрытых дефектов "
                            f"(Данную услугу можно запросить, оплачивается отдельно).\n"
                            f"* Цвет товара - цветопередача фотографии может отличаться от реального цвета товара. \n"
                            f"* Отправку поставщиком не того товара, который был заказан (если не заказана услуга "
                            f"проверки соответствия)\n"
                            f"* Отправку поставщиком товара другого размера\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "product_search_service")
async def product_search_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"✅ Тарифы на поиск:\n"
                            f"Вам необходимо предоставить фото товара, характеристики, предполагаемое количество.\n"
                            f"Срок готовности ответа на запрос поиска, от 3 до 8 рабочих дней (в течение этого времени "
                            f"можем уточнять у Вас детали касающиеся товара, к примеру, если это фабрика, то товар "
                            f"можно будет изготовить прямо под Ваше техзадание).\n"
                            f"Не берем на поиск более двух товарных позиций за один раз, ищем 1-2 позиции, начинаем "
                            f"сотрудничество по ним, далее переходим к поиску других товаров.\n"
                            f"Мы берём с Вас гарантийный платёж в размере: 1500₽\n"
                            f"Для чего это нужно?\n"
                            f"·Гарантийный платёж является нашим вознаграждением за потраченное время на поиски товара "
                            f"и общение с поставщиками в том случае, если Вы передумаете. Ведь в это время мы могли бы "
                            f"помочь другому клиенту с поиском и выкупом товара.\n"
                            f"Что дальше?\n"
                            f"· По результатам поиска мы предоставляем Вам подборку из лучших предложений "
                            f"(1-3 варианта).\n"
                            f"· Если Вы оформляете заказ, то сумма гарантийного платежа учитывается в стоимость "
                            f"оказанных услуг (таким образом, вычитаем из суммы за услуги внесённый ранее гарантийный "
                            f"платёж.).\n"
                            f"Комиссия за поиск и выкуп товара составит:\n"
                            f"· Закуп до 200.000 ₽. - комиссия 7%\n"
                            f"· Выше 200.000 ₽. - комиссия 5%\n"
                            f"· Свыше 1.000.000 ₽. - Комиссия 3%\n"
                            f"· Минимальная сумма заказа 100.000 ₽ и вес товара не менее 100 кг.\n"
                            f"· Доставка товара оплачивается отдельно, исходя из категории товара, определяется тариф "
                            f"на логистику.\n"
                            f"📦 Проверка товара на брак и на количество:\n"
                            f"Одна товарная позиция - одна единица товара фотоотчет, видеоотчет, осуществляется "
                            f"бесплатно по запросу. Всё что необходимо свыше, обговаривается индивидуально.\n"
                            f"✅ Дополнительная услуга: наклейки со штрих кодами на товар для маркетплейсов от 100-300 "
                            f"шт 1 юань (по курсу).\n"
                            f"✅ Дополнительная услуга: проверка количества товара на соответствие, 1-2 юаня за 1 "
                            f"счетную единицу (зависит от упаковки товара)\n"
                            f"Связаться с менеджерами: @cargo_cfb")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "supplier_inspection_by_province")
async def supplier_inspection_by_province(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"✅ Инспекция поставщика по провинциям 1000-1500 юаней (по актуальному курсу) плюс транспортные расходы, "
            f"по необходимости жильё.\n"
            f"Что входит?!\n"
            f"1️⃣Видео связь напрямую или отчёт по вашим вопросам.\n"
            f"Фотографии, видео, документы компании (поставщика).\n"
            f"2️⃣Посещение выставки и сбор каталогов по запросу, 1500 юаней (по курсу).\n"
            f"Оправка каталогов, только авиа. Оплата за доставку по факту прихода посылки в Москву. Также возможна "
            f"пересылка по городу или в другие регионы.\n"
            f"3️⃣Закуп образцов на месте - это услуга входит в стоимость инспекции\n"
            f"- Закуп+фотографии+видео. Без отправки клиенту.\n"
            f"- Доставка образцов платная услуга . Только авиа доставка. Тариф зависит от вида товара.\n"
            f"❇️Оплата за услуги 50%\n"
            f"После чего начинаем отработку и процесс работы.\n"
            f"Связаться с менеджерами: @cargo_cfb\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "wechat_registration_service")
async def wechat_registration_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Мы готовы помочь вам с регистрацией вашего WeChat аккаунта. Отсканируем ваш QR-код мгновенно.\n"
            f"Стоимость услуги 2000₽\n"
            f"Регистрация в WeChat действует по принципу «Приглашение по поручительству».\n"
            f"После прохождения всех процедур, в заключительной стадии верификации WeChat, появляется картинка с "
            f"QR-кодом. Именно этот код необходимо выслать действующему пользователю, чтобы он в разделе "
            f"«Отсканировать QR-код» подтвердил бы Ваше намерение стать новым пользователем, и желательно в пределах "
            f"1 минуты после получения QR.\n"
            f"Однако, не все существующие пользователи WeChat подходят на роль помощника по Qr-коду.\n"
            f"- Должно пройти не менее 6 месяцев со дня активации аккаунта;\n"
            f"- Для граждан Китая необходимо интегрировать платежную карту с приложением;\n"
            f"- Отсутствия нарушений внутренних правил со стороны пользователя;\n"
            f"Существующий пользователь способен отсканировать Qr - только 3-м новым пользователям в год\n"
            f"Связаться с менеджерами: @cargo_cfb\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "purchase_a_supplier_database")
async def purchase_a_supplier_database(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"У нас вы можете приобрести две разные базы поставщиков:\n"
                            f"1. База CFB включает в себя:\n"
                            f"• Более 2000 поставщиков с платформы 1688\n"
                            f"• Более 600 WeChat поставщиков\n"
                            f"• Десятки контактов фабрик и поставщиков лично собранные нашей компанией на выставках и "
                            f"ярмарках.\n"
                            f"Цена 1999 руб.\n"
                            f"2. База Ночных рынков включает в себя:\n"
                            f"• Сотни контактов поставщиков копий брендов: одежда, обувь, сумки и т.д. (Собрана нашей "
                            f"компанией при личном посещение торговых точек)\n"
                            f"Цена 4999 руб.\n"
                            f"Связаться с менеджерами: @cargo_cfb\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "what_payments_await_me")
async def what_payments_await_me(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"В нашей компании нет никаких скрытых платежей, мы максимально честны и открыты перед нашими клиентами.\n"
            f"Чтобы не было недопониманий, мы полностью расскажем за что приходится платить при карго доставке.\n"
            f"• Оплата самого товара и доставки по Китаю к нам на склад ( цена доставки зависит от поставщика, многие "
            f"доставляют бесплатно).\n"
            f"• Оплата комиссии за услуги выкупа или поиска товаров.\n"
            f"Если покупаете товар сами, никаких комиссий нет.\n"
            f"• Упаковка груза.\n"
            f"• Страховка, необязательная, зависит от вашего желания.\n"
            f"• Погрузочно-разгрузочные работы и хранение груза если не забираете груз в день прибытия и оставляете на "
            f"следующий день в Москве/Алматы по местным тарифам.\n"
            f"• Доставка местными Транспортными компаниями до вашего города (если не можете забрать в Москве/Алматы)\n"
            f"Связаться с менеджерами: @cargo_cfb\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "how_is_payment_made")
async def how_is_payment_made(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Вы можете выбрать удобный и необходимый для Вас способ (Здесь указана схема оплаты только по Карго "
            f"перевозкам, по работе в Белую и Белой доставке необходимо связываться со специалистом ВЭД).\n"
            f"Оплата за товар:\n"
            f"• Оплата рублями на банковские карты РФ (Сбербанк, Тинькофф)\n"
            f"• Мы можем помочь вам и принять оплату на Р/C - при оплате на расчётный счёт, +10% к общей сумме. При "
            f"данном виде оплаты работаем по договору, с предоставлением ТОРГ-12, минимальный вес грузов к перевозке "
            f"при таком расчете - 400кг.\n"
            f"• Вы можете оплатить товар сами и любым удобным для вас способом, мы просто доставим его.\n"
            f"Оплата за доставку по курсу:\n"
            f"• Оплата рублями на банковские карты РФ (Сбербанк, Тинькофф)\n"
            f"• Оплата наличными рублями при получении в Москве/Алматы\n"
            f"• Оплата наличными долларами нового образца при получении в Москве/Алматы\n"
            f"• Оплата наличными юанями/долларами у нас в офисе в Китае\n"
            f"Связаться с менеджерами: @cargo_cfb\n")
        main_menu_keyboard = keyboard_to_services_and_prices_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_services_and_prices_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(services_and_prices)
    dp.register_message_handler(cargo_delivery_prices)
    dp.register_message_handler(white_cargo_delivery_with_gas_turbine_engine)
    dp.register_message_handler(goods_redemption_service)
    dp.register_message_handler(product_search_service)
    dp.register_message_handler(supplier_inspection_by_province)
    dp.register_message_handler(wechat_registration_service)
    dp.register_message_handler(purchase_a_supplier_database)
    dp.register_message_handler(what_payments_await_me)
    dp.register_message_handler(how_is_payment_made)
