from loader import dp, bot, types
from keyboards.author import keyboard
from filters import isPrivate


@dp.message_handler(isPrivate(), commands=['author'])
async def author_command(msg: types.Message):
    await bot.send_message(msg.chat.id, "Author Page", reply_markup=keyboard())

