from aiogram import Bot
from models.dbconnect import Request
from aiogram.types import Message, CallbackQuery

from services.horoscope import get_horoscope
from services.weather import get_weather_data
from services.exchange_rate import get_exchange_rate
from services.joke import get_joke

# async def send_message_time(bot: Bot, request: Request):
#     all_data = await request.get_data()
#     # создадим пустые списки по темам рассылки и добавим туда id пользователей у которых эти темы True
#     joke = []
#     weather = []
#     exchange = []
#     horoscope = []
#     for i in range(len(all_data)):
#         if all_data[i]['joke']:
#             joke.append(all_data[i]['user_id'])
#         if all_data[i]['weather']:
#             weather.append(all_data[i]['user_id'])
#         if all_data[i]['exchange']:
#             exchange.append(all_data[i]['user_id'])
#         if all_data[i]['horoscope']:
#             horoscope.append(all_data[i]['user_id'])
#     # print(joke, weather, exchange, horoscope)
#     for user in joke:
#         res = get_joke()
#         await bot.send_message(user, res)
#     for user in weather:
#         res = get_weather_data()
#         await bot.send_message(user, res)
#     for user in exchange:
#         res = get_exchange_rate()
#         await bot.send_message(user, res)
#     for user in horoscope:
#         horo = await request.get_goro_db(user)  # достанем наименование знака по пользователю
#         res = get_horoscope(horo[0]['horoscope'])  # смотри dbconnect
#         await bot.send_message(user, res)



async def send_message_cron(bot: Bot, request: Request):
    all_data = await request.get_data()
    # создадим пустые списки по темам рассылки и добавим туда id пользователей у которых эти темы True
    joke = []
    weather = []
    exchange = []
    horoscope = []
    for i in range(len(all_data)):
        if all_data[i]['joke']:
            joke.append(all_data[i]['user_id'])
        if all_data[i]['weather']:
            weather.append(all_data[i]['user_id'])
        if all_data[i]['exchange']:
            exchange.append(all_data[i]['user_id'])
        if all_data[i]['horoscope']:
            horoscope.append(all_data[i]['user_id'])
    for user in joke:
        res = get_joke()
        await bot.send_message(user, res)
    for user in weather:
        res = get_weather_data()
        await bot.send_message(user, res)
    for user in exchange:
        res = get_exchange_rate()
        await bot.send_message(user, res)
    for user in horoscope:
        horo = await request.get_goro_db(user)  # достанем наименование знака по пользователю
        res = get_horoscope(horo[0]['horoscope'])  # смотри dbconnect, выдаем гороскоп
        await bot.send_message(user, res)  # отправляем гороскоп пользователям

