
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DOLL_IMG = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/33fc93cc2201d10f25f7d.jpg"


Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/Thecchub"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/+OATHrCdJxMsxMzI1")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://t.me/its_Aryaan")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[𝚅 𝙴 𝙽 𝙾 𝙼](https://t.me/its_Aryaan)"
        DOLL_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs 🇦ᴛΔɴᴋɪ 🇸𝙿𝙰𝙼 ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- 𝚅𝙴𝙽𝙾𝙼

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DOLL_IMG, caption=DOLL_ON, buttons=Button)
