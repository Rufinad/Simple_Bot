import operator

from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect, SwitchTo, Next, Radio
from bot_dialogs.handlers import result_getter
from states.statesform import StepsForm, StartSG
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case, Jinja
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column, Group
from bot_dialogs.getters import get_topics, get_zodiac


async def button_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    widget = dialog_manager.find('multi_topics')
    checked_id_btn = widget.get_checked()  # список с id кнопок, которые выбрали
    if '4' in checked_id_btn:
        await dialog_manager.switch_to(StartSG.horo)  # если кнопка с id 4 выбрана, то переходим к выбору знака зодиака
    else:
        await dialog_manager.switch_to(StartSG.res)


info_type_dialog = Dialog(
    Window(
        Const(text='Отметьте, что хотите получать в рассылке 👇'),
        Column(
            Multiselect(
                checked_text=Format('[✔️] {item[0]}'),
                unchecked_text=Format('[  ] {item[0]}'),
                id='multi_topics',
                item_id_getter=operator.itemgetter(1),
                items="topics",
                min_selected=1,
                # on_state_changed=category_filled  # показывает нам какие кнопки нажаты
            ),
            Button(
                text=Const("Далее"),
                id='button_0',
                on_click=button_clicked
            )
        ),
        state=StartSG.start,
        getter=get_topics
    ),
    Window(
        Const(text='Выберите свой знак зодиака 👇'),
        Group(
            Radio(
                checked_text=Format('🔘 {item[0]}'),
                unchecked_text=Format('⚪️ {item[0]}'),
                id='radio_zodiac',
                item_id_getter=operator.itemgetter(1),
                items="zodiacs",
            ),
            width=3
        ),
        Next(Const("Далее")),
        state=StartSG.horo,
        getter=get_zodiac
    ),
    Window(
        Jinja(
            "<b>Установлена рассылка по следующим темам</b>: \n"
            "{% for item in result %}"
            "• {{item}}\n"
            "{% endfor %}"
            "По этим темам ты будешь получать сообщение каждое утро в 7:00\n"
        ),
        Row(
            Button(
                text=Const('Меня устраивает!'),
                id='button_13'
                # on_click=button_clicked)
            ),

            Button(
                text=Const('Поменять время рассылки!'),
                id='button_14'
                # on_click=button_clicked)
            ),
        ),
        state=StartSG.res,
        getter=result_getter,
        parse_mode="html",

    ),
)
