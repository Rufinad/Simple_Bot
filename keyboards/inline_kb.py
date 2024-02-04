from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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


# Создаем объект инлайн-клавиатуры
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],
                     [button_2],
                     [button_3]
                     ])



