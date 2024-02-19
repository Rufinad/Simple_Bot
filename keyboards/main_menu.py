from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/change_info',
                   description='Изменить условия рассылки информации'),
        BotCommand(command='/get_horoscope',
                   description='Что мне расскажут звезды?'),
        BotCommand(command='/smile_me',
                   description='Рассмеши меня'),
        BotCommand(command='/get_weather',
                   description='Что по погоде'),
        BotCommand(command='/get_exchange_rate',
                   description='Какой курс валют')
    ]

    await bot.set_my_commands(main_menu_commands)