from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs



async def get_topics(dialog_manager: DialogManager, **kwargs):
    # dialog_manager.dialog_data.clear()
    topics = [
        ("хочу каждый день смеяться 😅", '1'),
        ("хочу знать, что творится за окном ☂️", '2'),
        ("хочу знать курс вражеских валют 💵", '3'),
        ("хочу знать будущее (но это не точно) 🤡", '4'),
    ]
    dialog_manager.dialog_data['all_button'] = topics
    return {"topics": topics}


async def get_zodiac(dialog_manager: DialogManager, **kwargs):
    zodiacs = [
        ('♈️Овен', 1),
        ('♉️Телец', 2),
        ('♊️Близнецы', 3),
        ('♋️Рак', 4),
        ('♌️Лев', 5),
        ('♍️Дева', 6),
        ('♎️Весы', 7),
        ('♏️Скорпион', 8),
        ('♐️Стрелец', 9),
        ('♑️Козерог', 10),
        ('♒️Водолей', 11),
        ('♓️Рыбы', 12)
    ]
    dialog_manager.dialog_data['all_zodiacs'] = zodiacs
    return {"zodiacs": zodiacs}
