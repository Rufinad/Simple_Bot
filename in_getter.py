from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Format
from environs import Env
from pprint import pprint

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class StartSG(StatesGroup):
    start = State()


async def username_getter(**kwargs):
    pprint(kwargs)
    return {'username': 'Mikhail'}


start_dialog = Dialog(
    Window(
        Format('Привет, {username}!'),
        getter=username_getter,
        state=StartSG.start
    ),
)


@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.include_router(start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)


"""{'aiogd_context': Context(_intent_id='sFHEZ6',
                          _stack_id='',
                          state=<State 'StartSG:start'>,
                          start_data=None,
                          dialog_data={},
                          widget_data={}),
 'aiogd_stack': Stack(_id='',
                      intents=['sFHEZ6'],
                      last_message_id=None,
                      last_reply_keyboard=False,
                      last_media_id=None,
                      last_media_unique_id=None,
                      last_income_media_group_id=None),
 'aiogd_storage_proxy': <aiogram_dialog.context.storage.StorageProxy object at 0x7f8b507c1f00>,
 'bot': <aiogram.client.bot.Bot object at 0x7f8b53f219f0>,
 'bots': (<aiogram.client.bot.Bot object at 0x7f8b53f219f0>,),
 'command': CommandObject(prefix='/', command='start', mention=None),
 'dialog_bg_factory': <aiogram_dialog.manager.bg_manager.BgManagerFactoryImpl object at 0x7f8b50797370>,
 'dialog_manager': <aiogram_dialog.manager.manager.ManagerImpl object at 0x7f8b507c2f20>,
 'dispatcher': <Dispatcher '0x7f8b50770940'>,
 'event_chat': Chat(id=791059676, type='private', title=None, username='rufinadus', first_name='𝕊𝕒𝕟', last_name='𝔾𝕣𝕚𝕥𝕤', is_forum=None, photo=None, active_usernames=None, available_reactions=None, accent_color_id=None, background_custom_emoji_id=None, profile_accent_color_id=None, profile_background_custom_emoji_id=None, emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None, bio=None, has_private_forwards=None, has_restricted_voice_and_video_messages=None, join_to_send_messages=None, join_by_request=None, description=None, invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, message_auto_delete_time=None, has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_protected_content=None, has_visible_history=None, sticker_set_name=None, can_set_sticker_set=None, linked_chat_id=None, location=None),
 'event_from_user': User(id=791059676, is_bot=False, first_name='𝕊𝕒𝕟', last_name='𝔾𝕣𝕚𝕥𝕤', username='rufinadus', language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None),
 'event_router': <Dispatcher '0x7f8b50770940'>,
 'event_update': Update(update_id=529244399, message=Message(message_id=1960, date=datetime.datetime(2024, 2, 13, 20, 1, 10, tzinfo=TzInfo(UTC)), chat=Chat(id=791059676, type='private', title=None, username='rufinadus', first_name='𝕊𝕒𝕟', last_name='𝔾𝕣𝕚𝕥𝕤', is_forum=None, photo=None, active_usernames=None, available_reactions=None, accent_color_id=None, background_custom_emoji_id=None, profile_accent_color_id=None, profile_background_custom_emoji_id=None, emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None, bio=None, has_private_forwards=None, has_restricted_voice_and_video_messages=None, join_to_send_messages=None, join_by_request=None, description=None, invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, message_auto_delete_time=None, has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_protected_content=None, has_visible_history=None, sticker_set_name=None, can_set_sticker_set=None, linked_chat_id=None, location=None), message_thread_id=None, from_user=User(id=791059676, is_bot=False, first_name='𝕊𝕒𝕟', last_name='𝔾𝕣𝕚𝕥𝕤', username='rufinadus', language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None), sender_chat=None, forward_origin=None, is_topic_message=None, is_automatic_forward=None, reply_to_message=None, external_reply=None, quote=None, via_bot=None, edit_date=None, has_protected_content=None, media_group_id=None, author_signature=None, text='/start', entities=[MessageEntity(type='bot_command', offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None)], link_preview_options=None, animation=None, audio=None, document=None, photo=None, sticker=None, story=None, video=None, video_note=None, voice=None, caption=None, caption_entities=None, has_media_spoiler=None, contact=None, dice=None, game=None, poll=None, venue=None, location=None, new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, message_auto_delete_timer_changed=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None, users_shared=None, chat_shared=None, connected_website=None, write_access_allowed=None, passport_data=None, proximity_alert_triggered=None, forum_topic_created=None, forum_topic_edited=None, forum_topic_closed=None, forum_topic_reopened=None, general_forum_topic_hidden=None, general_forum_topic_unhidden=None, giveaway_created=None, giveaway=None, giveaway_winners=None, giveaway_completed=None, video_chat_scheduled=None, video_chat_started=None, video_chat_ended=None, video_chat_participants_invited=None, web_app_data=None, reply_markup=None, forward_date=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None, forward_sender_name=None, forward_signature=None, user_shared=None), edited_message=None, channel_post=None, edited_channel_post=None, message_reaction=None, message_reaction_count=None, inline_query=None, chosen_inline_result=None, callback_query=None, shipping_query=None, pre_checkout_query=None, poll=None, poll_answer=None, my_chat_member=None, chat_member=None, chat_join_request=None, chat_boost=None, removed_chat_boost=None),
 'fsm_storage': <aiogram.fsm.storage.memory.MemoryStorage object at 0x7f8b50772710>,
 'handler': HandlerObject(callback=<function command_start_process at 0x7f8b50790550>,
                          awaitable=True,
                          params={'message', 'dialog_manager'},
                          varkw=False,
                          filters=[FilterObject(callback=<aiogram.filters.command.CommandStart object at 0x7f8b508998a0>,
                                                awaitable=True,
                                                params={'bot',
                                                        'message',
                                                        'self'},
                                                varkw=False,
                                                magic=None)],
                          flags={'commands': [<aiogram.filters.command.CommandStart object at 0x7f8b508998a0>]}),
 'raw_state': None,
 'state': <aiogram.fsm.context.FSMContext object at 0x7f8b507c2140>}
"""