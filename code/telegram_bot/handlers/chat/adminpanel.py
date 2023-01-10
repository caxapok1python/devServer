from loader import bot, dp, types
from filters import isPrivate
from data.config import ADMINS


@dp.message_handler(isPrivate(), chat_id=ADMINS, commands='adminpanel')
async def adminpanel_command(msg: types.Message):
    await msg.answer("[in process...]")

