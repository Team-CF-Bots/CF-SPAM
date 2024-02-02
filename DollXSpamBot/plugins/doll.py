import os
import asyncio
import sys
import git
import heroku3
# Changed root to DOLLSPAM
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from DollXSpamBot import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from DollXSpamBot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from DollXSpamBot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

DOLL_PIC = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/33fc93cc2201d10f25f7d.jpg"


DOLL = "✯ 🇦ᴛΔɴᴋɪ 🇸𝙿𝙰𝙼 ✯\n\n"
DOLL += f"**𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - @its_Aryaan**\n"
DOLL += f"━───────╯•╰───────━\n"
DOLL += f"• **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `3.10.1`\n"
DOLL += f"• **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `{version.__version__}`\n"
DOLL += f"• **🇦ᴛΔɴᴋɪ 🇸𝙿𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**  : `{deadlyversion}`\n"
DOLL += f"• **𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻** : [Join.](https://t.me/Thecchub)\n"
DOLL += f"• **𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴** : [•𝚁𝙴𝙿𝙾•](https://t.me/+OATHrCdJxMsxMzI1)\n"
DOLL += f"━───────╮•╭───────━\n\n"   
                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdoll(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await BOT0.send_file(event.chat_id,
                                  DOLL_PIC,
                                  caption=DOLL,
                                  buttons=[
        [
        Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", "https://t.me/Thecchub"),
        Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿", "https://t.me/+OATHrCdJxMsxMzI1")
        ],
        [
        Button.url("𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴", "https://t.me/+OATHrCdJxMsxMzI1")
        ]
        ]
        )
