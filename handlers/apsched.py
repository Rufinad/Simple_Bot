import asyncpg
from aiogram import Bot
from models.dbconnect import Request
from aiogram.types import Message, CallbackQuery

from services.horoscope import get_horoscope
from services.weather import get_weather_data
from services.exchange_rate import get_exchange_rate
from services.joke import get_joke


async def create_pool():
    return await asyncpg.create_pool(user='postgres', password='2787424032', database='bot-users',
                                             host='127.0.0.1', port=5432, command_timeout=60)


async def send_message_time(bot: Bot):
    pool_connect = await create_pool()
    request = Request(connector=pool_connect)
    all_data = await request.get_data()
    # print(all_data)
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
    print(joke, weather, exchange, horoscope)
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
        res = get_horoscope(horo[0]['horoscope'])  # смотри dbconnect
        await bot.send_message(user, f'<b>Гороскоп на сегодня:</b> {res}')


