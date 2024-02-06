import operator

from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect, SwitchTo, Next
from bot_dialogs.handlers import result_getter
from states.statesform import StepsForm, StartSG
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case, Jinja
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column
from bot_dialogs.getters import get_topics


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
            Next(Const("Далее"))
        ),
        state=StartSG.start,
        getter=get_topics
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
                    id='button_1'
                    # on_click=button_clicked)
                ),

                Button(
                    text=Const('Поменять время рассылки!'),
                    id='button_2'
                    # on_click=button_clicked)
                ),
            ),
            state=StartSG.res,
            getter=result_getter,
            parse_mode="html",

        ),
)



