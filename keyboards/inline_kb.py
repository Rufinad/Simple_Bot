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
                     [button_3]]
)


# создаем клавиатуру, которая позволит выбрать информацию для рассылки
# Создаем объекты инлайн-кнопок
btn_1 = InlineKeyboardButton(
    text='хочу каждый день смеяться 😅',
    callback_data='joke_everyday'
)
btn_2 = InlineKeyboardButton(
    text='хочу знать, что творится за окном ☂️',
    callback_data='weather_everyday'
)
btn_3 = InlineKeyboardButton(
    text='хочу знать курс вражеских валют 💵',
    callback_data='exchange_everyday'
)

btn_4 = InlineKeyboardButton(
    text='на этом все... жду сообщений',
    callback_data='send_type_info'
)

# Создаем объект инлайн-клавиатуры
type_info_kbr = InlineKeyboardMarkup(
    inline_keyboard=[[btn_1],
                     [btn_2],
                     [btn_3],
                     [btn_4]]
)

