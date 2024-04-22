from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обо мне👐"),
            KeyboardButton(text="Наши стилисты💇🏼")
        ],
        [
            KeyboardButton(text="Ответы на вопросы❓"),
            KeyboardButton(text="Услуги и прайс💰")
        ],
        [
            KeyboardButton(text="Наши работы🖼"),
        ],
        [
            KeyboardButton(text="Контакты📞")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт ниже."
)
