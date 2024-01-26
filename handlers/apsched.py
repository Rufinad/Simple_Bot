from aiogram import Bot

async def send_message_time(bot: Bot):
    await bot.send_message(791059676, f'это сообщение отправлено через несколько секунд после старта бота')


async def send_message_cron(bot: Bot):
    await bot.send_message(791059676, f'это сообщение будет отправлено в указанное время')


async def send_message_interval(bot: Bot):
    await bot.send_message(791059676, f'это сообщение будет отправляться с интервалом в 1 минуту')


async def send_message_middleware(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, f'это сообщение отправлено с помощью сформированной middleware задачей')