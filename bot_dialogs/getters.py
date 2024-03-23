from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs



async def get_topics(dialog_manager: DialogManager, **kwargs):
    # dialog_manager.dialog_data.clear()
    topics = [
        ("хочу каждый день смеяться 😅", '1'),
        ("хочу знать, что творится за окном ☂️", '2'),
        ("хочу знать курс вражеских валют 💵", '3'),
        ("хочу знать будущее (но это не точно) 💫", '4'),
    ]
    dialog_manager.dialog_data['all_button'] = topics
    return {"topics": topics}


async def get_zodiac(dialog_manager: DialogManager, **kwargs):
    zodiacs = [
        ('♈️Овен', 1, 'aries'),
        ('♉️Телец', 2, 'taurus'),
        ('♊️Близнецы', 3, 'gemini'),
        ('♋️Рак', 4, 'cancer'),
        ('♌️Лев', 5, 'leo'),
        ('♍️Дева', 6, 'virgo'),
        ('♎️Весы', 7, 'libra'),
        ('♏️Скорпион', 8, 'scorpio'),
        ('♐️Стрелец', 9, 'sagittarius'),
        ('♑️Козерог', 10, 'capricorn'),
        ('♒️Водолей', 11, 'aquarius'),
        ('♓️Рыбы', 12, 'pisces')
    ]
    dialog_manager.dialog_data['all_zodiacs'] = zodiacs
    return {"zodiacs": zodiacs}
