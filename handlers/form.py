from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.statesform import StepsForm
from handlers.apsched import send_message_middleware
from keyboards.inline_kb import type_info_kbr
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


@router.message(StepsForm.GET_LAST_NAME)  # хендлер зарегистрирован на сообщения из состояния GET_LAST_NAME
async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твоя фамилия: \r\n{message.text}\r\nТеперь расскажи какую информацию ты хочешь получать',
                         reply_markup=type_info_kbr)
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_TYPE_INFO)  # установим состояние


@router.message(StepsForm.GET_TYPE_INFO)  # хендлер зарегистрирован на сообщения из состояния GET_TYPE_INFO
async def get_name(message: Message, state: FSMContext, apscheduler: AsyncIOScheduler):
    context_data = await state.get_data()  # получаем словарь
    name = context_data['name']
    last_name = context_data['last_name']
    data_user = f'Вот твои данные:\r\n'\
        f'Имя {name}\r\n'\
        f'Фамилия {last_name}\r\n'
    await message.answer(data_user)
    await state.clear()  # выходим из машины состояний
    apscheduler.add_job(send_message_middleware, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                        kwargs={'chat_id': message.from_user.id})

