import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
import yt_dlp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 18000)
    seconds %= 18000
    minutes = seconds // 300
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"ᴛɪᴛʟᴇ: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"ᴅᴜʀᴀᴛɪᴏɴ: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"ᴠɪᴇᴡs: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"α∂∂є∂ ϐγ: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")




@Client.on_message(command("play") 
                   & filters.group
                   & ~filters.edited 
                   & ~filters.forwarded
                   & ~filters.via_bot)
async def play(_, message: Message):

    lel = await message.reply("🔄 **⚡𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜⚡**")
    
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Xmarty"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>𝘼𝙙𝙙 𝙢𝙚 𝙖𝙨 𝙖𝙙𝙢𝙞𝙣 𝙤𝙛 𝙪𝙧 𝙜𝙧𝙤𝙪𝙥 𝙛𝙞𝙧𝙨𝙩!</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**ϰмαяτγ мυѕιϲ αѕѕιѕταиτ נοιиє∂ τнιѕ gяουρ ƒοя ρℓαγ мυѕιϲ🎵**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>🛑 𝙁𝙡𝙤𝙤𝙙 𝙒𝙖𝙞𝙩 𝙀𝙧𝙧𝙤𝙧 🛑</b> \n\𝙃𝙚𝙮 {user.first_name}, 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙪𝙨𝙚𝙧𝙗𝙤𝙮 𝙘𝙤𝙪𝙡𝙙𝙣'𝙩 𝙟𝙤𝙞𝙣 𝙪𝙧 𝙜𝙧𝙥 𝙙𝙪𝙚 2 𝙝𝙚𝙖𝙫𝙮 𝙟𝙤𝙞𝙣 𝙧𝙚𝙦𝙪𝙚𝙨𝙩𝙨. 𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙪𝙨𝙚𝙧𝙗𝙤𝙩 𝙣𝙤𝙩 𝙗𝙖𝙣𝙣𝙚𝙙 𝙞𝙣 𝙜𝙧𝙥 𝙖𝙣𝙙 𝙩𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 𝙡𝙩𝙧 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 @xmarty_support!")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i>𝙃𝙚𝙮 {user.first_name}, 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙪𝙨𝙚𝙧𝙗𝙤𝙩 𝙣𝙤𝙩 𝙞𝙣 𝙩𝙝𝙞𝙨 𝙘𝙝𝙖𝙩, 𝙖𝙨𝙠 𝙖𝙙𝙢𝙞𝙣 𝙩𝙤 𝙨𝙚𝙣𝙙 /play 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙛𝙤𝙧 𝙛𝙞𝙧𝙨𝙩 𝙩𝙞𝙢𝙚 𝙩𝙤 𝙖𝙙𝙙 𝙞𝙩 .</i>")
        return
    
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 300) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ 𝙎𝙤𝙣𝙜𝙨 𝙡𝙤𝙣𝙜𝙚𝙧 𝙩𝙝𝙖𝙣 {DURATION_LIMIT} 𝙢𝙞𝙣𝙪𝙩𝙚𝙖 𝙖𝙧𝙚𝙣'𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮!"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/caeb50039026a746e7252.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 300)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝘾𝙝𝙖𝙣𝙣𝙚𝙡 🔊",
                        url="https://t.me/Xmarty_support")
                   
                ]
            ]
        )
        
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")
            
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 300
                
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᎽϴႮͲႮᏴᎬ",
                            url=f"{url}"),
                        InlineKeyboardButton(
                            text="ՏႮᏢᏢϴᎡͲ ᏀᎡϴႮᏢ",
                            url=f"https://t.me/Xmarty_Support")

                    ]
                ]
            )
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/638c20c44ca418c8b2178.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ᎽϴႮͲႮᏴᎬ",
                                url=f"https://youtube.com")

                        ]
                    ]
                )
        if (dur / 300) > DURATION_LIMIT:
             await lel.edit(f"❌ 𝙑𝙞𝙙𝙚𝙤𝙨 𝙡𝙤𝙣𝙜𝙚𝙧 𝙩𝙝𝙖𝙣 {DURATION_LIMIT}𝙢𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙧𝙚𝙣'𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮!")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)     
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit("🧐 **𝙒𝙝𝙖𝙩'𝙨 𝙩𝙝𝙚 𝙨𝙤𝙣𝙜 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙥𝙡𝙖𝙮?**")
        await lel.edit("🔎 **❤️ƒเɳ∂เɳɠ ƭɦε รσɳɠ❤️**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit(" **❤️ρɾσcεรรเɳɠ รσµɳ∂ร❤️**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
        except Exception as e:
            await lel.edit(
                "❌ ѕοиg иοτ ƒουи∂.\n\nτяγ αиοτнєя ѕοиg οя мαγϐє ѕρєℓℓ ιτ ρяορєяℓγ."
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="γουτυϐє 🎬",
                            url=f"{url}"),
                        InlineKeyboardButton(
                            text="∂οωиℓοα∂ 📥",
                            url=f"{durl}")

                    ]
                ]
            )
        
        if (dur / 300) > DURATION_LIMIT:
             await lel.edit(f"❌ ѵíժҽօs lօղցҽɾ Եհαղ {DURATION_LIMIT} ตíղմԵҽs αɾҽղ'Ե αllօաҽժ Եօ թlαվ!")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="final.png", 
        caption="**🎵 ѕοиg:** {}\n**🕒 ᴅᴜʀᴀᴛɪᴏɴ:** {} min\n**👤 α∂∂є∂ ϐγ :** {}\n\n**#⃣ գυєυє∂ ροѕιτιοи:** {}".format(
        title, duration, message.from_user.mention(), ροѕιτιοи
        ),
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption="**🎵 ѕοиg:** {}\n**🕒 ᴅᴜʀᴀᴛɪᴏɴ:** {} min\n**👤 α∂∂є∂ ϐγ:** {}\n\n**▶️ иοω ρℓαγιиg ατ `{}`...**".format(
        title, duration, message.from_user.mention(), message.chat.title
        ), )
        os.remove("final.png")
        return await lel.delete()
