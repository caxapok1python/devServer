from loader import bot, dp, types, FSMContext
from fsm import Base64Mem
from keyboards import base64toolkit
from filters import isPrivate
import base64


@dp.message_handler(isPrivate(), commands=['base64'], state='*')
async def base64_command(msg: types.Message):
    print('base64')
    await bot.send_message(msg.chat.id, "Choose option", reply_markup=base64toolkit.base64toolkit_keyboard())


@dp.message_handler(isPrivate(), state=Base64Mem.encode)
async def base64_encode(msg: types.Message, state: FSMContext):
    await state.finish()
    text = base64.b64encode(msg.text.encode())
    await bot.send_message(msg.chat.id, text.decode())


@dp.message_handler(isPrivate(), state=Base64Mem.decode)
async def base64_decode(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    try:
        text = base64.b64decode(msg.text.encode())
        await bot.send_message(msg.chat.id, text.decode())
    except:
        await bot.send_message(msg.chat.id, "ERROR. Try again")
