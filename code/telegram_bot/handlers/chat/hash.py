import logging

from loader import bot, types, dp
from fsm import Hash
from keyboards.hash import start_keyboard
from loader import FSMContext
import hashlib
import math
from filters import isPrivate


@dp.message_handler(isPrivate(), commands='hash')
async def hash_command(msg: types.Message):
    await bot.send_message(msg.chat.id, "Choose hash type", reply_markup=start_keyboard())


@dp.message_handler(isPrivate(), state=Hash.type)
async def hash_typo(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hash_type'] = msg.text
    await Hash.text.set()
    await bot.send_message(msg.chat.id, "Please enter a hash size")


@dp.message_handler(isPrivate(), state=Hash.size)
async def hash_size(msg: types.Message, state: FSMContext):
    size = msg.text
    if size.isnumeric():
        if 1 <= int(size) <= 64 and str(math.log(int(size), 2)).split('.')[-1] == '0':
            size = int(msg.text)
        else:
            await bot.send_message(msg.chat.id, "Try again")
            return
    else:
        await bot.send_message(msg.chat.id, "Try again")
        return
    async with state.proxy() as data:
        data['hash_size'] = size
    await Hash.text.set()
    await bot.send_message(msg.chat.id, "Please enter a text")


@dp.message_handler(isPrivate(), state=Hash.text)
async def hash_text(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if data['hash_type'] == 'blake2b':
            encoded = hashlib.blake2b(msg.text.encode(), digest_size=data['hash_size']).hexdigest()
        else:
            encoded = hashlib.new(data['hash_type'], msg.text.encode()).hexdigest()
        await msg.reply(encoded)
        await state.reset_state()


