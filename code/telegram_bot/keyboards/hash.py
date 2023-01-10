from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    md5_btn = InlineKeyboardButton(text='md5', callback_data='hash_md5')
    blake2b_btn = InlineKeyboardButton(text='blake2b', callback_data='hash_blake2b')
    sha128_btn = InlineKeyboardButton(text='sha128', callback_data='hash_sha128')
    sha256_btn = InlineKeyboardButton(text='sha256', callback_data='hash_sha256')
    sha512_btn = InlineKeyboardButton(text='sha512', callback_data='hash_sha512')
    own_btn = InlineKeyboardButton(text='other', callback_data='hash_other')
    markup.row(md5_btn, blake2b_btn)
    markup.row(sha128_btn, sha256_btn, sha512_btn)
    markup.row(own_btn)
    return markup
