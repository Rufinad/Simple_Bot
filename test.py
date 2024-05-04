import asyncio

from aiogram import Bot
from models.dbconnect import Request
import asyncpg

# Создание пула подключений


# Создание экземпляра класса Request с передачей аргумента connector


async def send_message_time(bot: Bot):
    pool = await asyncpg.create_pool(user='postgres', password='2787424032', database='bot-users',
                                             host='127.0.0.1', port=5432, command_timeout=60)
    request_instance = Request(connector=pool)
    all_data = request_instance.get_data()
    print(all_data)

asyncio.run(send_message_time(Bot))
