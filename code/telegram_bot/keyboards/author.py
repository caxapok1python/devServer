from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    dev = InlineKeyboardButton(text='🧑🏼‍💻 Developer', callback_data='developer')
    group = InlineKeyboardButton(text='👥 Group', callback_data='group')
    channel = InlineKeyboardButton(text='🖋 Channel', callback_data='channel')
    markup.add(group, channel)
    markup.add(dev)
    return markup
