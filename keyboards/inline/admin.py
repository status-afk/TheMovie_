from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Statistika 💹",callback_data='stats'),
            InlineKeyboardButton(text="Reklama 🎫",callback_data='ad'),
        ]
    ]
)