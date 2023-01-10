from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    daily = InlineKeyboardButton(text="💹 Daily", callback_data='currency_daily')
    latest = InlineKeyboardButton(text="⏱ Latest", callback_data='currency_latest')
    markup.row(daily, latest)
    return markup
