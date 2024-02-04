from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.statesform import StepsForm, StartSG

router = Router()
'''Данная форма позволяет пользователю ввести персональные данные'''

@router.message(Command(commands='form'))  # хендлер зарегистрирован на сообщения по команде form
async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начнем заполнять анкету. Введи свое имя')
    await state.set_state(StepsForm.GET_NAME)  # установим состояние


@router.message(StepsForm.GET_NAME)  # хендлер зарегистрирован на сообщения из состояния GET_NAME
async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твое имя: \r\n{message.text}\r\nТеперь введи свою фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


@router.message(StepsForm.GET_LAST_NAME)  # хендлер зарегистрирован на сообщения из состояния start
async def get_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    contex_data = await state.get_data()  # получаем данные сохраненные в состоянии
    name = contex_data.get('name')
    await message.answer(f'Твое имя: \r\n{name}\r\n'
                         f'Твоя фамилия: \r\n{message.text}\r\n'
                         f'Приятно познакомиться!')
    await state.clear()




