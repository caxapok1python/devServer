from loader import bot, dp, types
from fsm import Base64Mem
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(startswith='/'), content_types=['text'])
async def receive_some_text(msg: types.Message):
    await msg.answer("Unknown command")


@dp.message_handler(content_types=['text'])
async def receive_some_text(msg: types.Message):
    await bot.send_message(msg.chat.id, msg.text)
    return
