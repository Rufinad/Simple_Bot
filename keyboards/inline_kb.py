from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Создаем объекты инлайн-кнопок
button_1 = InlineKeyboardButton(
    text='Давай-ка анекдотик',
    callback_data='joke'
)
button_2 = InlineKeyboardButton(
    text='Что там на улице?',
    callback_data='weather'
)
button_3 = InlineKeyboardButton(
    text='Как себя рубль чувствует?',
    callback_data='exchange'
)
button_4 = InlineKeyboardButton(
    text='Что мне расскажут звезды?',
    callback_data='horoscope'
)


# Создаем объект инлайн-клавиатуры
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],
                     [button_2],
                     [button_3],
                     [button_4]
                     ])

