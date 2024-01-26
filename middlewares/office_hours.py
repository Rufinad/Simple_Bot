from datetime import datetime
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in ([i for i in range(6, 23)])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # используем функцию office_hours, чтобы понять в рабочее время или нет было написано сообщение
        if office_hours():
            return await handler(event, data)
        await event.answer(f'Время работы бота: \r\nПн-пт с 8 до 18. Я же тоже должен отдыхать!!!')


