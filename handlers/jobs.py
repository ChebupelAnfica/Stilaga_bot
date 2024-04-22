from aiogram import F, types
from aiogram.types import InputMediaPhoto
from aiogram.fsm.context import FSMContext
from keyboards.inline.inline_keyboard_markup import recording_on

from loader import dp, bot
import logging


@dp.message(F.text == "Наши работы🖼")
async def jobs(message: types.Message, state: FSMContext):
    photo_id1 = "AgACAgIAAxkBAAIBEmXdRkzG9n1BFOlLBSA9PFNp-gHtAALE1zEbX1LpSirsuMiJJH2mAQADAgADcwADNAQ"
    photo_id2 = "AgACAgIAAxkBAAIBFGXdRmKcTq9hvrP6cQbj9f20WmpmAALF1zEbX1LpSnUgaYbRuG-7AQADAgADcwADNAQ"
    photo_id3 = "AgACAgIAAxkBAAIBFmXdRnIHwP046JF6D8HuwYNPznoLAALH1zEbX1LpSqk2_fVv_NZ8AQADAgADcwADNAQ"
    photo_id4 = "AgACAgIAAxkBAAIBGGXdRn0ISUszlb4GjQ6ULBEZkXarAALI1zEbX1LpSnjAX1LNEFz6AQADAgADcwADNAQ"

    media = [
        InputMediaPhoto(media=photo_id1),
        InputMediaPhoto(media=photo_id2),
        InputMediaPhoto(media=photo_id3),
        InputMediaPhoto(media=photo_id4),
    ]
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await bot.send_media_group(message.chat.id, media)
    except Exception as ex:
        logging.error(ex)

    try:
        await bot.send_message(message.chat.id, text='⬆️ Работы наших стилистов по одной работе от мастера.',
                               reply_markup=recording_on)
    except Exception as ex:
        logging.error(ex)
