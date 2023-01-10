from loader import bot, dp, types, FSMContext
from fsm import *
from handlers.chat.password_gen import generate_password
from handlers.chat.random_kit import from_mode


@dp.callback_query_handler(lambda c: c.data, state='*')
async def inline_callback(call: types.CallbackQuery, state: FSMContext):
    if call:
        # BASE64
        if "base64" in call.data:
            if call.data == 'base64_encode':
                await Base64Mem.encode.set()
            else:
                await Base64Mem.decode.set()
            await bot.send_message(call.message.chat.id, "OK, now send me a <b>text</b>")
            return

        # HASH
        if 'hash' in call.data:
            hash_mode = call.data.split('_')[-1]
            if hash_mode == "other":
                await Hash.type.set()
                await bot.send_message(call.message.chat.id, "Please enter a hash type")
                return
            async with state.proxy() as data:
                data['hash_type'] = hash_mode
            if hash_mode == 'blake2b':
                await Hash.size.set()
                await bot.send_message(call.message.chat.id, "Please enter a hash size (must be between 1 and 64)")
                return
            await Hash.text.set()
            await bot.send_message(call.message.chat.id, "Enter a text")

        # Password
        if 'password' in call.data:
            level = call.data.split("_")[-1]
            await bot.send_message(call.message.chat.id, generate_password(level))
            return

        # Currency
        if 'currency' in call.data:
            mode = call.data.split("_")[-1]
            data = get_all_currency(mode)
            text = get_data2text(mode, data)
            await bot.send_message(call.message.chat.id, text)
            return

        # Random
        if 'random' in call.data:
            mode = call.data.split("_")[-1]
            await from_mode(mode, call.message)
            return

        # Card gen
        if call.data[:4] == "card":
            mode = call.data.split("_")[-1]
            await mode2func(mode, call.message)
            return

        # Author
        if call.data == 'developer':
            return
        if call.data == 'group':
            await group_invite(call, state, timeout=10)
            return
        if call.data == 'channel':
            await channel_invite(call, state, timeout=10)
            return

