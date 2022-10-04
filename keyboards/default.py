from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Tavsiya olish')
        ]
    ]
)

goal_for_using = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton('Dasturlash'),
            KeyboardButton('Grafik dizayn'),
        ],
        [
            KeyboardButton('O\'yin uchun'),
            KeyboardButton('Ofis uchun')
        ]
    ]
)


computer_or_back = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Kompyuter ko\'rish')
        ],
        [
            KeyboardButton(text='Orqaga')
        ]
    ]
)
