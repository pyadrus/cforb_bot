from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import types_of_packaging_keyboard, types_of_packaging_keyboard_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "types_of_packaging")
async def types_of_packaging(callback_query: types.CallbackQuery, state: FSMContext):
    """Виды упаковки"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"<b>Здесь вы можете увидеть какие упаковки существуют, как выглядят, и сколько стоят.</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = types_of_packaging_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "bag_tape")
async def bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Вставка видео https://youtube.com/shorts/E2LFiy8iF0g упаковки и текст:\n\n"
                            f"<b>Мешок + скотч:</b> классические упаковка с использованием мешка и упаковочного "
                            f"скотча, подходит для текстиля и мягких товаров.\n\n"
                            f"<b>Стоимость данной упаковки 5$ место</b>\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "box_bag_tape")
async def box_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Коробка + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Вставка видео https://youtube.com/shorts/DX-EFbUkOf8 упаковки и текст:\n\n"
            f"<b>Кробка + мешок + скотч:</b> если у вас много разных товаров в том числе маленькие коробочки, весь "
            f"товар складывается в нашу коробку, далее упаковка в мешок и упаковочный скотч.\n\n"
            f"<b>Стоимость данной упаковки 8$ место</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "wooden_sheathing_bag_tape")
async def wooden_sheathing_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянная обрешетка + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Вставка видео https://youtube.com/shorts/4ogIlLQUipc упаковки и текст:\n\n"
            f"<b>Деревянная обрешетка + мешок + скотч:</b> Каркас из деревянных решеток (досок, брусьев), который "
            f"способствует хорошей фиксации груза и его защите от механических повреждений. Применяется для упаковки "
            f"хрупкого и бьющегося товара. + мешок + скотч\n\n"
            f"<b>Стоимость данной упаковки 10$ место</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "wooden_corners_bag_tape")
async def wooden_corners_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянные уголки + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Вставка видео https://youtube.com/shorts/QcXqjaESW7s упаковки и текст:\n\n"
            f"<b>Уголки + мешок + скотч:</b> Легче чем обрешетка, держит форму коробки, но менее защищенная, т.к "
            f"практически полностью открытая.\n\n"
            f"<b>Стоимость данной упаковки 10$ место</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "pallet_in_crate")
async def pallet_in_crate(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет в обрешетке"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"Вставка видео https://youtube.com/shorts/QcXqjaESW7s упаковки и текст:\n\n"
            f"<b>Паллет в обрешетке:</b> Вид упаковки используется для крупногабаритных или хрупких грузов, "
            f"представляет из себя поддон с деревянными бортами как у обрешетки. Погрузочно-разгрузочные работы "
            f"товаров, упакованных таким образом, осуществляются при помощи вилочного погрузчика.\n\n"
            f"<b>Стоимость данной упаковки 45$ за куб</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "pallet_with_a_solid_wooden_box")
async def pallet_with_a_solid_wooden_box(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет с глухим деревянным коробом"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f"<b>Паллет с глухим деревянным коробом:</b> Вид упаковки используется для крупногабаритных или хрупких "
            f"грузов, представляет из себя поддон с деревянными бортами как у обрешетки. Погрузочно-разгрузочные "
            f"работы товаров, упакованных таким образом, осуществляются при помощи вилочного погрузчика.\n\n"
            f"Фото отсутствует\n\n"
            f"<b>Стоимость данной упаковки 90-100$ за куб</b>\n\n"
            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n")
        types_of_packaging_key = types_of_packaging_keyboard_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(types_of_packaging)
    dp.register_message_handler(bag_tape)
    dp.register_message_handler(box_bag_tape)
    dp.register_message_handler(wooden_sheathing_bag_tape)
    dp.register_message_handler(wooden_corners_bag_tape)
    dp.register_message_handler(pallet_in_crate)
    dp.register_message_handler(pallet_with_a_solid_wooden_box)
