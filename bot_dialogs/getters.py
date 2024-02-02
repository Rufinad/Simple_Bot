from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs



async def get_topics(dialog_manager: DialogManager, **kwargs):
    # dialog_manager.dialog_data.clear()
    topics = [
        ("хочу каждый день смеяться 😅", '1'),
        ("хочу знать, что творится за окном ☂️", '2'),
        ("хочу знать курс вражеских валют 💵", '3')
    ]
    dialog_manager.dialog_data['all_button'] = topics
    return {"topics": topics}
