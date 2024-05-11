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
    print(all_data)
    # [<Record user_id=791059676 user_name='𝕊𝕒𝕟' horoscope='scorpio' joke=True weather=True exchange=True>,
    # <Record user_id=923903795 user_name='Екатерина' horoscope=None joke=True weather=True exchange=True>]
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
    day_joke = get_joke()
    for user in joke:
        await bot.send_message(user, day_joke)
    day_weather = get_weather_data()
    for user in weather:
        await bot.send_message(user, day_weather)
    day_rate = get_exchange_rate()
    for user in exchange:
        await bot.send_message(user, day_rate)
    for user in horoscope:
        horo = await request.get_goro_db(user)  # достанем наименование знака по пользователю
        res = get_horoscope(horo[0]['horoscope'])  # смотри dbconnect
        await bot.send_message(user, f'<b>Гороскоп на сегодня:</b> {res}')


async def send_message_cron(bot: Bot):
    pool_connect = await create_pool()
    request = Request(connector=pool_connect)
    all_data = await request.get_data()

    # Создаем словарь для хранения ID пользователей и их флагов
    user_flags = {}
    for user_data in all_data:
        user_id = user_data['user_id']
        user_flags[user_id] = {
            'joke': user_data['joke'],
            'weather': user_data['weather'],
            'exchange': user_data['exchange'],
            'horoscope': user_data['horoscope']
        }

    # Создаем множество для хранения ID пользователей, которым уже были отправлены сообщения
    sent_users = set()

    for user_id, flags in user_flags.items():
        # Проверяем, был ли пользователь уже обработан
        if user_id in sent_users:
            continue

        # Проверяем флаги пользователя и отправляем соответствующие сообщения
        if flags['joke']:
            day_joke = get_joke()
            await bot.send_message(user_id, day_joke)
        if flags['weather']:
            day_weather = get_weather_data()
            await bot.send_message(user_id, day_weather)
        if flags['exchange']:
            day_rate = get_exchange_rate()
            await bot.send_message(user_id, day_rate)
        if flags['horoscope']:
            horo = await request.get_goro_db(user_id)
            res = get_horoscope(horo[0]['horoscope'])
            await bot.send_message(user_id, f'<b>Гороскоп на сегодня:</b> {res}')

        # Добавляем ID пользователя в множество
        sent_users.add(user_id)
