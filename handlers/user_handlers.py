from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from services.weather import get_weather_data
from services.exchange_rate import get_exchange_rate
from services.joke import get_joke
from keyboards.inline_kb import start_keyboard
from models.dbconnect import Request


router = Router()

''' 3 инлайн кнопки ведут себя по-разному, алерты, сообщение, всплывающее на 2-3 сек окно'''


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, request: Request, state: FSMContext):
    await request.add_data(message.from_user.id, message.from_user.first_name)  # когда пользователь нажимает старт его имя и id заносятся в бд
    await state.clear()
    await message.answer(text='Привет! каждый день буду присылать тебе погоду на новый день,'
                              ' курс валют и новый анекдот, если хочешь от чего отказаться, '
                              'нажми "изменить условия рассылки"',
                         reply_markup=start_keyboard)


# @router.message(Command(commands='get_weather'))  # эта хрень работает если руками прописать /get_weather
@router.callback_query(F.data == 'weather')  # работает если нажать на кнопку которой  callback == weather
async def send_weather(callback: CallbackQuery):
    weather_data = get_weather_data()
    await callback.answer(weather_data)


# @router.message(Command(commands='get_exchange_rate'))
@router.callback_query(F.data == 'exchange')  # работает если нажать на кнопку которой  callback == exchange
async def send_rate(callback: CallbackQuery):
    exchange_rate = get_exchange_rate()
    await callback.answer(exchange_rate, show_alert=True)


# Этот хэндлер срабатывает на команду /smile_me
# @router.message(Command(commands='smile_me'))
@router.callback_query(F.data == 'joke')  # работает если нажать на кнопку которой  callback == joke
async def send_joke(callback: CallbackQuery):
    joke = get_joke()
    await callback.message.answer(joke, ParseMode.HTML)



'''Тут мы обработаем получение текстовых команд, либо через главное меню бота, либо при написании команд вручную'''

@router.message(Command(commands='get_weather'))  # эта хрень работает, если руками прописать /get_weather
async def send_weather(message: Message):
    weather_data = get_weather_data()
    await message.answer(weather_data, ParseMode.HTML)


@router.message(Command(commands='get_exchange_rate'))
async def send_rate(message: Message):
    exchange_rate = get_exchange_rate()
    await message.answer(exchange_rate, show_alert=True)


# Этот хэндлер срабатывает на команду /smile_me
@router.message(Command(commands='smile_me'), )
async def send_joke(message: Message):
    joke = get_joke()
    await message.answer(joke, ParseMode.HTML)


