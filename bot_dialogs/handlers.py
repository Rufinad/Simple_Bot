from aiogram import Router
from aiogram_dialog import StartMode, DialogManager
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect
from states.statesform import StepsForm, StartSG
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs


router = Router()



# Хэндлер, обрабатывающий нажатие кнопки в виджете `Checkbox`
async def checkbox_clicked(callback: CallbackQuery, checkbox: ManagedCheckbox, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(is_checked=checkbox.is_checked())

# Это хэндлер, который будет срабатывать на состояние GET_TYPE_INFO
@router.message(Command(commands='change_info'))
async def get_type_info(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)