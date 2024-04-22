from aiogram import F, types

from keyboards.inline.close import close_inline_keyboard
from loader import dp, bot
import logging


@dp.message(F.text == "Обо мне👐")
async def send_photo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAMhZdzmGNf34Z4d2pF1ktx-thrKffQAAvzWMRtfUulKXpmO4sDo4g0BAAMCAANzAAM0BA"
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await bot.send_photo(message.chat.id, photo_id, caption=f"""Добро пожаловать в PinUp Salon - где классические стили встречаются с современным подходом к красоте. Это уникальное место, обладающее особенной атмосферой и настроем, переносит вас в середину 20-го века и подарит вам незабываемый опыт.

Наш салон вдохновлен поп-культурой 50-х годов, всемирно известной эпохой pin up, когда женственность и игривость были главными элементами стиля. Интерьер выполнен в яркой и живой цветовой палитре, воссоздающей сияющую энергию того времени. Прихожая встречает вас ретро-стилизованной мебелью и уникальными декоративными элементами, создающими атмосферу шика и роскоши.

PinUp Salon - больше, чем просто салон красоты, это место, где эстетика прошлого и современности встречается, создавая бесподобную смесь красоты, элегантности и утонченности. Опыт, который оживляет прошлое, празднует настоящее и вдохновляет будущее.""",
                             reply_markup=close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
