from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

style = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1. Иванова Мария Алексеевна", callback_data="style1")
        ],
        [
            InlineKeyboardButton(text="2. Захаров Андрей Петрович", callback_data="style2")
        ],
        [
            InlineKeyboardButton(text="3. Смирнова Екатерина Дмитриевна", callback_data="style3")
        ],
        [
            InlineKeyboardButton(text="4. Петров Василий Игоревич", callback_data="style4")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="cancel")
        ]
    ],
)


back_style = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👈", callback_data="back_to_all_stilags")
        ]
    ]
)


recording_on = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Записаться к специалисту", callback_data="collect_data")
        ]
    ]
)


back_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👈", callback_data="back_to_all_questions")
        ]
    ]
)


questions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Что в канале ❓", callback_data="questions1")
        ],
        [
            InlineKeyboardButton(text="Как можно записаться ❓", callback_data="questions2")
        ],
        [
            InlineKeyboardButton(text="Какие варианты оплаты ❓", callback_data="questions3")
        ],
        [
            InlineKeyboardButton(text="Сколько стоит ❓", callback_data="questions4")
        ],
        [
            InlineKeyboardButton(text="Какого стиля мы придерживаемся ❓", callback_data="questions5")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="cancel")
        ]
    ],
)
