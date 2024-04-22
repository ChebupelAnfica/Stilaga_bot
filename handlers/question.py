from aiogram import F, types

from keyboards.inline.inline_keyboard_markup import questions, back_question

from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging


@dp.message(F.text == "Ответы на вопросы❓")
async def question(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await message.answer(f"❓ Часто задаваемые вопросы и ответы на них",
                             reply_markup=questions)
    except:
        pass


@dp.callback_query(lambda call: call.data == 'questions1')
async def process_callback1(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_text('''Что в канале ❓
Мы салон с высококлассными специалистами, который поможет подобрать вам ваш стиль. ''', call.from_user.id,
                                    call.message.message_id, reply_markup=back_question)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(lambda call: call.data == 'questions2')
async def process_callback2(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_text('''Как можно записаться ❓
Вы можете прийти к нам по адресу или запискаться по номеру телефону, который вы можете найти в пункте контакты.''',
                                    call.from_user.id, call.message.message_id, reply_markup=back_question)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(lambda call: call.data == 'questions3')
async def process_callback3(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_text('''Какие варианты оплаты ❓
Можете оплатить как по банковской карте, так и наличными прямо в салоне.''', call.from_user.id, call.message.message_id,
                                    reply_markup=back_question)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(lambda call: call.data == 'questions4')
async def process_callback4(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_text('''Сколько стоит ❓
Это будет зависит от специалиста и услуги с которомы можете ознакомиться в <b>Услуги и прайс</b>.''', call.from_user.id,
                                    call.message.message_id, reply_markup=back_question)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(lambda call: call.data == 'questions5')
async def process_callback5(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_text('''Какого стиля мы придерживаемся ❓
Так как мы тематический салон в стиле PinUp 50-60х годов, мы работаем именно в этом стиле причесок такого времени, но так же мы стрижем и в современных стилях.''',
                                    call.from_user.id, call.message.message_id, reply_markup=back_question)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'back_to_all_questions')
async def process_back(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.edit_message_text('❓ Часто задаваемые вопросы и ответы на них',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=questions)
    except Exception as ex:
        logging.error(ex)
