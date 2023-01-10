from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def base64toolkit_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    encode = InlineKeyboardButton(text='🔒 Encode', callback_data='base64_encode')
    decode = InlineKeyboardButton(text='🔓 Decode', callback_data='base64_decode')
    markup.row(encode, decode)
    return markup

