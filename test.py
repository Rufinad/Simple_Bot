import operator
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case
from aiogram_dialog.widgets.kbd import Button, Select, Checkbox, ManagedCheckbox, Column, Multiselect
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class StartSG(StatesGroup):
    start = State()
async def category_filled(callback: CallbackQuery, checkbox: ManagedMultiselect, *args, **kwargs):
    print(checkbox.get_checked())


# Геттер
async def get_topics(dialog_manager: DialogManager, **kwargs):
    topics = [
        ("IT", '1'),
        ("Дизайн", '2'),
        ("Наука", '3'),
        ("Общество", '4'),
        ("Культура", '5'),
        ("Искусство", '6'),
    ]
    return {"topics": topics}


start_dialog = Dialog(
    Window(
        Const(text='Отметьте темы новостей 👇'),
        Column(
            Multiselect(
                checked_text=Format('[✔️] {item[0]}'),
                unchecked_text=Format('[  ] {item[0]}'),
                id='multi_topics',
                item_id_getter=operator.itemgetter(1),
                items="topics",
                on_click=category_filled
                #on_state_changed=category_filled #попробуйте так и так
            ),
        ),
        state=StartSG.start,
        getter=get_topics
    ),
)

@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.include_router(start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)