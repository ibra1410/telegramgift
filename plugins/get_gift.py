try:
    from telethon.sessions import StringSession
    import asyncio, re, json
    from kvsqlite.sync import Client as uu
    from telethon.tl.types import KeyboardButtonUrl
    from telethon.tl.types import KeyboardButton
    from telethon import TelegramClient, events, functions, types, Button
    import time, datetime
    from datetime import timedelta
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
    from plugins.messages import *
except:
    os.system("pip install telethon kvsqlite")
    try:
        from telethon.sessions import StringSession
        import asyncio, re, json
        from kvsqlite.sync import Client as uu
        from telethon.tl.types import KeyboardButtonUrl
        from telethon.tl.types import KeyboardButton
        from telethon import TelegramClient, events, functions, types, Button
        import time, datetime
        from datetime import timedelta
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
        from plugins import *
    except Exception as errors:
        print('An Erorr with: ' + str(errors))
        exit(0)

from pyrogram import Client, enums
from pyrogram.raw import functions

API_ID = "22256614"
API_HASH = "4f9f53e287de541cf0ed81e12a68fa3b"

async def get_gift(session):
    X =  TelegramClient(StringSession(session), API_ID, API_HASH)
    async for x in X.iter_messages(777000, limit=5):
        try:
            await X.connect()
            if x.action.slug:
                await X.disconnect()
                return x.action.slug
        except:
            pass
            
    return False

async def join_channel(session, channel):
    X = TelegramClient(StringSession(session), API_ID, API_HASH)
    try:
        await X.connect()
        result = await X(functions.channels.JoinChannelRequest(
            channel=channel
        ))
        return True
    except Exception as a:
        return False

async def leave_channel(session, channel):
    X = TelegramClient(StringSession(session), API_ID, API_HASH)
    try:
        await X.connect()
        result = await X(functions.channels.LeaveChannelRequest(
            channel=channel
        ))
        return True
    except Exception as a:
        return False

async def leave_all(session):
    X = TelegramClient(StringSession(session), API_ID, API_HASH)
    try:
        await X.connect()
        async for dialog in X.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                await dialog.delete()
        return True
    except Exception as a:
        return False

async def check(session, bot, user_id):
    try:
        client = Client('::memory::', api_id=22119881, api_hash='95f5f60466a696e33a34f297c734d048', in_memory=True, session_string=session)
    except Exception as a:
        print(a)
    try:
        await client.start()
    except Exception as a:
        print(a)
        await bot.send_message(user_id, str(a))
        return False
        
        
    try:
        await client.get_me()
        await client.send_message("me", ".")
        await client.stop()
        return True
    except Exception as a:
        print(a)
        await bot.send_message(user_id, str(a))
        return False