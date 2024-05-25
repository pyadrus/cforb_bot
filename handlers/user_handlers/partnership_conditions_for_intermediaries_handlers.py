# from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


@router.callback_query(F.data == "partnership_conditions_for_intermediaries_button")
async def partnership_conditions_for_intermediaries(callback_query: types.CallbackQuery, state: FSMContext):
    """Партнерские условия для посредников"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        greeting_message = (f"<b>Если вы являетесь посредником по бизнесу с Китаем,</b> доставляете груз и работаете с "
                            f"другой компанией, блогером, менеджером по WB, у вас есть свой канал, группа или "
                            f"курсы👍\n\n"

                            f"<b>Мы призываем рассмотреть нашу компанию для сотрудничества.</b>\n\n"

                            f"• Обговорим и согласуем особенные условия именно для ВАС\n"
                            f"• Вы станете нашим полноценным партнером, получите первые цены, комфорт и удобство в "
                            f"работе с Китаем.\n"
                            f"• Поделимся знаниями и опытом\n\n"

                            f"<b>Если вы не хотите сами заниматься данной деятельностью, мы можем сотрудничать по "
                            f"системе “Промокод”, условия также обговариваются индивидуально.</b>\n\n "

                            f"<b>Если вы действующий посредник по Китаю, доставляете груз, выкупаете товар и т.д., "
                            f"Мы готовы предоставить Вам условия полноценного партнерства, либо специальный "
                            f"прайс.</b>\n\n"

                            f"Если Вы думаете что сейчас у вас хорошие и честные условия от вашего Китайского "
                            f"партнера, и вы можете ему на 100% доверять, это значит что вы на 90% плохо знаете "
                            f"китайцев!\n\n"

                            f"<b>Свяжитесь с нами, и мы обсудим различные варианты сотрудничества!</b>\n\n"

                            f"<i>В нашей практике есть действующие и реальные кейсы полноценного партнерства с "
                            f"российскими крупными посредниками!</i>\n\n"

                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        main_menu_keyboard = create_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               # parse_mode=types.ParseMode.HTML
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_partnership_conditions_for_intermediaries_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(partnership_conditions_for_intermediaries)
