import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

SD = Client("anymouse sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

STICKER = "2_5217577170838241432.webm"

START_TEXT = """🌷 ʜᴇʏ ᴅᴇᴀʀ, ɪ ᴀᴍ  𝙻ᴀᴡʟᴇss 𝙰ɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ. 

ᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴍᴇ sᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴏʀ ᴍᴇᴅɪᴀ ᴀɴᴅ ᴛʜᴇɴ I ᴡɪʟʟ 𝙰ɴᴏɴʏᴍᴏᴜs ᴛʜᴀᴛ!
𝙸 ᴄᴀɴ ᴀʟsᴏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ🪽

🛠 **Server** : [Heroku](Heroku.com)
🛠 **Library** : [Pyrogram](https://github.com/pyrogram/pyrogram)

𝙼ᴀᴅᴇ 𝙱ʏ » [ꜰᴇʀᴅɪ](https://t.me/fsyrl)"""

REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="https://t.me/fsyrl"),
        InlineKeyboardButton(
            text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url=f"https://t.me/BestieVirtual")],
    [InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/filmlk21kw"),
        InlineKeyboardButton(
            text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://t.me/BestieVirtual")]])

@SD.on_message(filters.command('start') & filters.private)
async def start(client, message):    
    await message.reply_sticker(STICKER)
    await message.reply_text(START_TEXT,
                             reply_markup=REPLY_MARKUP,
                             disable_web_page_preview=True)

@SD.on_message(filters.caption & filters.private)
async def addorno(client, message):
    msg = message.message._id
    await message.reply_text('start bot go to the option', quote=True,
    reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text="yes",
    callback_data=f"yes-{msg}"),
    InlineKeyboardButton(text="No",
    callback_data=f"no-{msg}")])
    )

@SD.on_message(filters.private & filters.text | filters.media)
async def SDBot(client, message):
    await message.copy(message.chat.id)

print("YourBot is Started")
print("Join @BestieVirtual.")
SD.run()
