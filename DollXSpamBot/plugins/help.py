from DollXSpamBot import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DollXSpamBot import CMD_HNDLR as hl
    
HELP_PIC = "https://graph.org/file/33fc93cc2201d10f25f7d.jpg"

DOLL_Help = "🇦ᴛΔɴᴋɪ 🇸𝙿𝙰𝙼\n\n"

DOLL_Help = "**𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - @ite_Aryaan**\n"
 
DOLL_Help += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ 🇦ᴛΔɴᴋɪ 🇸𝙿𝙰𝙼 𝙱𝙾𝚃__\n\n"

DOLL_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

DOLL_Help += f" `!ping` - to check ping\n `!alive` , `!doll` - to check bot alive/version (only main userbot will reply)\n\n !`restart` - to restart all spam bots \n\n `!addecho` - to addecho \n\n `!rmecho` - To remove Echo \n\n `!addsudo` - To add sudo user using spam bot \n\n"
 
DOLL_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

DOLL_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DOLL_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

DOLL_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n\n `!dreplyraid` - to de-active reply raid\n\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n\n `!uspam` - this cmd use for unlimited Spam until You restart the bots!!\n\n `!delayspam` - this cmd use for delay spam\n\n"

DOLL_Help += f" `!pornspam` - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

DOLL_Help += f" `!hang` - 😂 ↧\n\n"

DOLL_Help += f" `!bspam` - 𝗕𝗜𝗥𝗧𝗛𝗗𝗔𝗬 𝗦𝗣𝗔𝗠 ↧\n\n"

DOLL_Help += f"© @Dollx_spambot\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DOLL_Help,
                                  buttons=[
        [
        Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", "https://t.me/THECCHUB")
        ] 
        ]
        )
