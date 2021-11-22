from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**ʜᴇʏ, I'm {bn} 🎵

ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄᴀʟʟ. ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [xᴍᴀʀᴛʏ ꜱᴀʟɪᴍ](https://t.me/Xmartperson).

ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ꜰʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 𝙎𝙊𝙐𝙍𝘾𝙀 𝘾𝙊𝘿𝙀 🛠", url="https://github.com/S780821/XMARTY_MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/XMARTY_Support"
                    ),
                    InlineKeyboardButton(
                        "✨𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄 2✨", url="https://github.com/S780821/XMARTY_MUSIC_2"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝙈𝘼𝙆𝙀 𝙐𝙍 𝙊𝙒𝙉 𝙄𝙁 𝙐 𝙒𝘼𝙉𝙏 𝘼𝙉𝙔 𝙃𝙀𝙇𝙋 𝙋𝙇𝙀𝘼𝙎𝙀 𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝙈𝙔 𝘽𝙊𝙎𝙎 ", url="https://t.me/XMARTPERSON"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀʀᴇ ʏʀʀ ᴊɪɴᴅᴀ ʜᴏᴏ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄⚡", url="https://github.com/S780821/XMARTY_MUSIC")
                ]
            ]
        )
   )


