from loader import dp, bot, types, FSMContext
from keyboards.random_kit import *
from filters import isPrivate
from fsm import Random
import random


@dp.message_handler(isPrivate(), commands=['random'])
async def random_command(msg: types.Message):
    await bot.send_message(msg.chat.id, "Choose mode", reply_markup=start_keyboard())


@dp.message_handler(commands=['dice'])
async def dice_command(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji="🎰")


@dp.message_handler(commands=['coin'])
async def coin_command(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji="🏀")
    # await bot.send_message(msg.chat.id, random.choice(['eagle', 'tails']))


@dp.message_handler(state=Random.number)
async def random_number(msg: types.Message, state: FSMContext):
    await state.reset_state()
    start, stop = map(int, msg.text.split('-'))
    await bot.send_message(msg.chat.id, random.randint(start, stop))


async def from_mode(mode, message: types.Message):
    if mode == 'number':
        await Random.number.set()
        await bot.send_message(message.chat.id, "Enter <b>[start]-[stop]</b>")
        return
    if mode == 'dice':
        await dice_command(message)
        return
    await coin_command(message)
