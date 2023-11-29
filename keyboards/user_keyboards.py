from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_greeting_keyboard():
    """Создает клавиатуру для приветственного сообщения 👋"""
    greeting_keyboard = InlineKeyboardMarkup()
    ask_anonymous_question_button = InlineKeyboardButton(text='🤔 Услуги и цены', callback_data='services_and_prices')
    sign_up_button = InlineKeyboardButton(text='📝 Бланк заказа', callback_data='order_form')
    contacts_and_address_button = InlineKeyboardButton(text='📍 Виды упаковки', callback_data='types_of_packaging')
    contact_operator_button = InlineKeyboardButton(text='👩‍💼 Самовыкуп', callback_data="self_redemption")
    current_promotions_button = InlineKeyboardButton(text='🎁 Отзывы', callback_data='reviews')
    leave_review_button = InlineKeyboardButton(text="📞 Связаться с менеджером", callback_data='contact_the_manager')

    greeting_keyboard.row(ask_anonymous_question_button)  # Задать анонимный вопрос
    greeting_keyboard.row(sign_up_button)  # Записаться
    greeting_keyboard.row(contacts_and_address_button,  # Контакты и адрес
                          current_promotions_button)  # Текущие акции
    greeting_keyboard.row(contact_operator_button)  # Связаться с оператором
    greeting_keyboard.row(leave_review_button)  # Оставить отзыв

    return greeting_keyboard


if __name__ == '__main__':
    create_greeting_keyboard()
