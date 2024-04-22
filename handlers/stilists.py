from aiogram import F, types

from keyboards.inline.inline_keyboard_markup import style, back_style

from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging

photo_id1 = "AgACAgIAAxkBAAIB32Xf1NWpIRAnfnMQPO5U-jxSHWDWAAL00DEbk9kAAUs8CUgIudPyMAEAAwIAA3MAAzQE"
photo_id2 = "AgACAgIAAxkBAAICFGXf2x6ucJHOKRX-eyw4sPPUAefEAAID0TEbk9kAAUszOc6MAYXFeQEAAwIAA3MAAzQE"
photo_id3 = "AgACAgIAAxkBAAICEmXf2qcYyltkEMdOqjBprekWg1-nAAIB0TEbk9kAAUtXxWPiCgenygEAAwIAA3MAAzQE"
photo_id4 = "AgACAgIAAxkBAAICFmXf20gm6_onAulkkmL9eVTk39yfAAIE0TEbk9kAAUvZHSVXSlJ0agEAAwIAA3MAAzQE"


@dp.message(F.text == "Наши стилисты💇🏼")
async def styliga(message: types.Message, state: FSMContext):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        new_message = await message.answer(
            text="Здесь вы можете ознокомиться с нашими стилисты и выбрать того, который вам больше подходит:",
            reply_markup=style
        )
        await state.update_data(menu_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex


@dp.callback_query(lambda call: call.data == 'style1')
async def styliga1(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    menu_message_id = data.get('menu_message_id')
    try:
        await bot.delete_message(call.message.chat.id, menu_message_id)
        new_message = await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo_id1,
            caption='''1. Иванова Мария Алексеевна - энергичная и целеустремленная женщина, всегда готова помочь и прийти на выручку. Она является профессором в университете, специализируясь на истории искусств.''',
            reply_markup=back_style
        )
        await state.update_data(stylist_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex


@dp.callback_query(lambda call: call.data == 'style2')
async def styliga1(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    menu_message_id = data.get('menu_message_id')
    try:
        await bot.delete_message(call.message.chat.id, menu_message_id)
        new_message = await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo_id2,
            caption='''2. Захаров Андрей Петрович - пунктуальный и ответственный, он всегда доводит начатое дело до конца. Властелин ресторанного бизнеса, Андрей прославился своими уникальными концепциями кулинарных заведений.''',
            reply_markup=back_style
        )
        await state.update_data(stylist_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex


@dp.callback_query(lambda call: call.data == 'style3')
async def styliga1(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    menu_message_id = data.get('menu_message_id')
    try:
        await bot.delete_message(call.message.chat.id, menu_message_id)
        new_message = await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo_id3,
            caption='''3. Смирнова Екатерина Дмитриевна - осторожная и талантливая девушка, работает преподавателем балета в театре. Её мягкость и природная грация всегда вызывают восхищение у её учеников.''',
            reply_markup=back_style
        )
        await state.update_data(stylist_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex


@dp.callback_query(lambda call: call.data == 'style4')
async def styliga1(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    menu_message_id = data.get('menu_message_id')
    try:
        await bot.delete_message(call.message.chat.id, menu_message_id)
        new_message = await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo_id4,
            caption='''4. Петров Василий Игоревич - настоящий проработник, никогда не устает учиться и совершенствоваться в своем мастерстве. Василий является известным мастером и ювелиром, создающим неповторимые украшения.''',
            reply_markup=back_style
        )
        await state.update_data(stylist_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex


@dp.callback_query(F.data == 'back_to_all_stilags')
async def process_back(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    stylist_message_id = data.get('stylist_message_id')
    try:
        await bot.delete_message(call.message.chat.id, stylist_message_id)
        new_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text="Здесь вы можете ознокомиться с нашими стилисты и выбрать того, который вам больше подходит:",
            reply_markup=style
        )
        await state.update_data(menu_message_id=new_message.message_id)
    except Exception as ex:
        logging.error(ex)
        raise ex
