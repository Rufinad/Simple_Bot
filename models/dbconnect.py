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
    async def change_data(self, user_id, joke, weather, exchange):
        query = f"UPDATE data_users SET joke = '{joke}', weather = '{weather}', exchange = '{exchange}'"\
                f"WHERE user_id = {user_id}"
        await self.connector.execute(query)

    # метод для получения списка тем для рассылки по пользователю
    async def get_data(self, user_id):
        query = f"SELECT * FROM data_users WHERE user_id = {user_id};"
        await self.connector.execute(query)