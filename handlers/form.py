from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.statesform import StepsForm, StartSG

router = Router()


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
    await message.answer(f'Твоя фамилия: \r\n{message.text}\r\nТеперь расскажи какую информацию ты хочешь получать')
    await state.clear()




