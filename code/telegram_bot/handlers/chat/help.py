from loader import bot, dp, types
from filters import isPrivate


@dp.message_handler(isPrivate(), commands=['help'])
async def help_command(msg: types.Message):
    await bot.send_message(msg.chat.id, open('./contents/help.html', 'r').read())
