import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    # метод внесет нового пользователя в бд
    async def add_data(self, user_id, user_name):
        query = f"INSERT INTO data_users (user_id, user_name) VALUES ({user_id}, '{user_name}') " \
                f"ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}'"
        await self.connector.execute(query)

    # метод изменит темы рассылок для конкретного пользователя
    async def change_data(self, user_id, joke, weather, exchange, horoscope):
        query = f"UPDATE data_users SET joke = '{joke}', weather = '{weather}', exchange = '{exchange}'," \
                f" horoscope = '{horoscope}'"\
                f"WHERE user_id = {user_id}"
        await self.connector.execute(query)

    # метод для получения списка тем для рассылки по пользователю
    async def get_data(self):
        query = f"SELECT * FROM data_users;"
        result = await self.connector.fetch(query)  # получили все данные из бд
        # print(result[0]['user_id'])  # 791059676 - id пользователя например
        return result
