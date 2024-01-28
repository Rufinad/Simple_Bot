import operator
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect
from states.statesform import StepsForm, StartSG
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column
from bot_dialogs.getters import get_topics



info_type_dialog = Dialog(
    Window(
        Const(text='Отметьте что хотите получать в рассылке 👇'),
        Column(
            Multiselect(
                checked_text=Format('[✔️] {item[0]}'),
                unchecked_text=Format('[  ] {item[0]}'),
                id='multi_topics',
                item_id_getter=operator.itemgetter(1),
                items="topics",
                min_selected=1
            ),
        ),
        state=StartSG.start,
        getter=get_topics
    ),
)