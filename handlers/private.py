from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Κα΄Κ, I'm {bn} π΅

Ιͺ α΄α΄Ι΄ α΄Κα΄Κ α΄α΄κ±Ιͺα΄ ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄'κ± α΄ α΄Ιͺα΄α΄ α΄α΄ΚΚ. α΄α΄α΄ α΄Κα΄α΄α΄α΄ ΚΚ [GJ516](https://t.me/export_gabber).

α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄Ι΄α΄ α΄Κα΄Κ α΄α΄κ±Ιͺα΄ κ°Κα΄α΄ΚΚ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  πππππΎπ πΎππΏπ π ", url="https://github.com/GUABAJA/-ll-ll-G-516_-_-ll-ll-")
                  ],[
                    InlineKeyboardButton(
                        "π¬ πππππ", url="https://t.me/GJ516_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "β¨ππππππ ππππ 2β¨", url="https://github.com/GUABAJA/-ll-ll-G-516_-_-ll-ll-_2"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ππΌππ ππ πππ ππ π ππΌππ πΌππ ππππ ππππΌππ πΎππππΌπΎπ ππ π½πππ ", url="https://t.me/@export_gabber"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**α΄Κα΄ ΚΚΚ α΄ΙͺΙ΄α΄α΄ Κα΄α΄ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β‘ππππππ ππππβ‘", url="https://github.com/GUABAJA/-ll-ll-G-516_-_-ll-ll-")
                ]
            ]
        )
   )


