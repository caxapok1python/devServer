from loader import bot, dp, types
from keyboards.password_gen import *
from filters import isPrivate
import random
import string


punc = "!#$%&()*+,-./:;<=>?@[\]^_{|}~"
simple_litters = string.ascii_letters + string.digits


def generate_password(level: str):
    if level == 'simple':
        return "".join(random.sample(simple_litters, 6))
    if level == 'medium':
        return "".join(random.sample(simple_litters, 6)) + random.choice(punc)
    return random.choice(punc) + "".join(random.sample(simple_litters, 10)) + random.choice(punc)


@dp.message_handler(isPrivate(), commands='password')
async def password_command(msg: types.Message):
    await bot.send_message(msg.chat.id, "Choose password level", reply_markup=start_keyboard())

