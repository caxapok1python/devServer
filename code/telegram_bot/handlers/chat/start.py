from loader import bot, dp, types


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    chat_id = msg.chat.id
    await bot.send_message(chat_id, f"<b>Hello</b>, {msg.chat.first_name}")
