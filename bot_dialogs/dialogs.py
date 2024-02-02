import operator

from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect, SwitchTo, Next
from bot_dialogs.handlers import result_getter, category_filled
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
                on_state_changed=category_filled  # показывает нам какие кнопки нажаты
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
            ),
            state=StartSG.res,
            getter=result_getter,
            parse_mode="html",
        ),
)



