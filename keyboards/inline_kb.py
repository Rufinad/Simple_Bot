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
button_4 = InlineKeyboardButton(
    text='Изменить условия рассылки',
    callback_data='change_info'
)

# Создаем объект инлайн-клавиатуры
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],
                     [button_2],
                     [button_3],
                     [button_4]])



