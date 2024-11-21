from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from aiogram.types import CallbackQuery
from pyexpat.errors import messages

from data.config import ADMINS
from keyboards.inline.admin import keyboard
from loader import dp, db, bot
@dp.message_handler(commands='admin')
async def user_count(message:types.Message):
    if str(message.from_user.id)==ADMINS[0]:
        await message.answer(text='.',reply_markup=keyboard)
    else:
        await message.answer("Siz admin emassiz.")

@dp.callback_query_handler(text='stats')
async def statistika(call:CallbackQuery):
    await call.message.delete()
    count = db.count_users()
    await call.message.answer(f"Bazada <b>{count[0]}</b>  ta foydalanuvchi bor")
@dp.callback_query_handler(text='ad')
async def reklama(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Reklama videosi yoki rasmini yoziv bilan yuboring.")

    @dp.message_handler(content_types=['photo', 'video', 'text'])
    async def handle_ad_message(ad_message: types.Message):
        not_sent=0
        sent=0
        for user_id in db.select_all_user_ids():
            try:
                await ad_message.forward(user_id)
                sent+=1
            except Exception as e:
                print(f"ERR: {e}")
                not_sent+=1
        if not_sent!=0:
            await ad_message.answer(f"Reklama {sent}ta odamga yuborildi")
            await ad_message.answer(f"{not_sent}ta odamga yuborilmadi")
        else:
            await ad_message.answer("Reklama hammaga yuborildi")














