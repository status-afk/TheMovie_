from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        telegram_id = message.from_user.id
        username = message.from_user.username

        if not db.select_user(telegram_id=telegram_id):
            db.add_user(telegram_id=telegram_id, username=username)
            logging.INFO(f"Foydalanuvchi qo'shildi telegram_id:{telegram_id} username: {username}")
            await message.answer("Siz yangi foydalanuvchisiz!")

            count = db.count_users()
            for admin in ADMINS:
                await dp.bot.send_message(
                    admin,
                    f"Telegram ID: {telegram_id}\n"
                    f"Username : {username}\n"
                    f"Toliq ismi :{message.from_user.full_name}\n"
                    f"Foydalanuvchi bazaga qo'shildi\n\n"
                    f"Bazada <b>{count[0]}</b>  ta foydalanuvchi bor"
                )

        text = "Assalomu alaykum xush kelibsiz"
        await message.answer(text)

    except Exception as err:
        logging.exception(err)
