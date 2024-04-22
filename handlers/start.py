import logging
import time

from aiogram import types, F, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import VideoNote

import keyboards
from data.config import ADMINS
from database import SessionLocal
from loader import dp, bot
from utils.db.queries import get_user, create_user


@dp.message(Command("start"))
# @dp.message(CommandStart(deep_link=True))
async def cmd_start(message: types.Message,
                    command: CommandObject):
    try:
        async with SessionLocal.begin() as session:
            user = await get_user(session,
                                  message.from_user.id)
            if user is None:
                await create_user(session,
                                  message.from_user.id,
                                  message.from_user.username,
                                  message.from_user.full_name)
            # session.commit()  # БОЛЬШЕ НЕ ИСПОЛЬЗУЕМ. АВТОКОММИТ РАБОТАЕТ
    except Exception as ex:
        logging.error(ex)
        try:
            await bot.send_message(message.from_user.id, '''Произошла ошибка. Начните с начала -> /start''')
        except Exception as ex:
            logging.error(ex)
        return
    if command.args:
        if command.args == '777':
            try:
                await bot.send_message(message.from_user.id, 'XD')
            except Exception as ex:
                logging.error(ex)
            return
    try:
        video_note_id = "DQACAgIAAxkBAAICZmXhxNQeMLkBRd_F053uej3U3m7oAAIFRgACrKYQS9wRrCMPhz2cNAQ"
        await bot.send_video_note(chat_id=message.from_user.id, video_note=video_note_id)
    except:
        pass
    try:
        time.sleep(10)
        await bot.send_message(message.from_user.id, f'''<b>Приветствую, {message.from_user.full_name}👋</b>\n
"PinUp Salon - это не просто салон, это путешествие в золотой век ретро-элегантности. Здесь вы окунетесь в атмосферу стиля pin up 50-х лет прошлого века, где каждый зал, каждый уголок пропитан духом эпохи. Наши мастера-профессионалы обладают искусством воплощения красоты в этом великолепном стиле. PinUp Salon - это возвращение к прославленной эпохе, сохраняющее очарование и гламур прошлых лет."''',
                               reply_markup=keyboards.default.main_menu.main_menu)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.message(F.content_type.in_({'photo', 'video', 'document', 'video_note'}))
async def echo_files(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        if message.photo:
            try:
                await bot.send_message(message.from_user.id, message.photo[0].file_id)
            except:
                pass
        if message.video:
            try:
                await bot.send_message(message.from_user.id, message.video.file_id)
            except:
                pass
        if message.document:
            try:
                await bot.send_message(message.from_user.id, message.document.file_id)
            except:
                pass
        if message.video_note:
            try:
                await bot.send_message(message.from_user.id, message.video_note.file_id)
            except:
                pass
        return



