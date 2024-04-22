from aiogram import F, types

from keyboards.inline.close import close_inline_keyboard
from loader import dp, bot
import logging


@dp.message(F.text == 'Контакты📞')
async def contact(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await message.answer(f"""Контакты: 8(800)555-35-35\n
Найти нас можно по адресу: г. Москва микрорайон Северное Чертаново, 1к1\n
Сайт для записи на процедуры и стрижку можно перейти сюда👇\n
https://myata-salon.ru/""",
                             reply_markup=close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
