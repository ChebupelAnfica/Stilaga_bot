from aiogram import F, types


from keyboards.inline.close import close_inline_keyboard
from loader import dp, bot
import logging


@dp.message(F.text == "Услуги и прайс💰")
async def send_doc(message: types.Message):
    document_id = "BQACAgIAAxkBAAOTZd0gxuv_GoQQl41GMlKIwpFsB04AAsY_AAJfUulKsdaVQaua7pY0BA"
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await bot.send_document(message.chat.id, document_id, caption=f"""Салон волшебной красоты представляет вашему вниманию изысканный прайс-лист. Наш салон - это невероятное сочетание уединения и элегантности, в котором вы можете расслабиться и позволить нам заботиться о вас.
        
Наши цены указаны четко и прозрачно, чтобы вы могли спланировать свой пребывание у нас без неожиданностей. Мы гордимся безупречным сервисом и высочайшим уровнем обслуживания, который мы предлагаем по очень конкурентоспособным ценам.
""",
                                reply_markup=close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
