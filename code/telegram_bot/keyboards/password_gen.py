from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    simple = InlineKeyboardButton(text='👎 Simple', callback_data='password_simple')
    medium = InlineKeyboardButton(text='👌 Medium', callback_data='password_medium')
    strong = InlineKeyboardButton(text='👍 Strong', callback_data='password_strong')
    markup.row(simple, medium, strong)
    return markup
