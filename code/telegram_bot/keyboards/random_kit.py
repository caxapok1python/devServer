from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    number = InlineKeyboardButton(text="🔢 Number", callback_data="random_number")
    coin = InlineKeyboardButton(text="🪙 Coin", callback_data="random_coin")
    dice = InlineKeyboardButton(text="🎲 Dice", callback_data="random_dice")
    markup.row(coin, dice)
    markup.row(number)
    return markup

