from aiogram import Router, F
from aiogram_dialog import StartMode, DialogManager
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect, ManagedMultiselect

from models.dbconnect import Request
from states.statesform import StepsForm, StartSG
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button
from bot_dialogs.getters import get_topics
router = Router()


# этот роутер реагирует на команду из main_menu: change_info
@router.message(Command(commands='change_info'))
async def get_type_info(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


# работает если нажать на кнопку которой  callback == change_info
@router.message(F.data == 'change_info')
async def get_type_info(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


# хендлер срабатывает на отправку сообщения "изменить данные рассылки"
# async def category_filled(callback: CallbackQuery, checkbox: ManagedMultiselect, dialog_manager: DialogManager, *args, **kwargs):
#     clicked_button = checkbox.get_checked()
#     # dialog_manager.dialog_data['clicked_button'] = checkbox.get_checked()  # запишем id кнопок на которые нажали
#     print(clicked_button)  # показывает нам какие кнопки нажаты


async def result_getter(dialog_manager: DialogManager, request: Request, **kwargs,):
    widget = dialog_manager.find('multi_topics')
    checked_id_btn = widget.get_checked()  # список с id кнопок, которые выбрали
    data = dialog_manager.dialog_data['all_button']  # тут все кнопки
    # список с выбранными темами рассылки
    result_lst = []
    for el in data:  # бежим по всем кнопкам и добавляем тексты нажатых кнопок в список
        if el[1] in checked_id_btn:
            result_lst.append(el[0])
    # определим какие темы надо отправлять ежедневно и внесем изменения в бд
    joke, weather, exchange, horoscope = False, False, False, False
    if '1' in checked_id_btn:
        joke = True
    if '2' in checked_id_btn:
        weather = True
    if '3' in checked_id_btn:
        exchange = True
    if '4' in checked_id_btn:  # другая логика, необходимо дать клавиатуру
        horoscope = True
    await request.change_data(dialog_manager.event.from_user.id, joke, weather, exchange, horoscope)
    dialog_manager.dialog_data.clear()
    # вернем словарь чтобы Jinja отработала корректно
    return {
        'result':  result_lst
    }



