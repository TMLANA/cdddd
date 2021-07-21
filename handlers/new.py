from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only
userbotjoin
@Client.on_message(filters.group & filters.command(["دعوة المساعد"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني أولاً كمسؤول في مجموعتك</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "prince_vcmusic_bot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>بوت المستخدم الخاص بك بالفعل في الدردشة الخاصة بك</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطاء انتظر 🛑 \n لم يتمكن User Bot من الانضمام إلى مجموعتك بسبب طلبات الانضمام الكثيفة لـ userbot!  تأكد من عدم حظر المستخدم في المجموعة."
            "\n\nأو قم بإضافة userbot يدويًا إلى مجموعتك وحاول مرة أخرى</b>",
        )
        return
    await message.reply_text(
            "<b>انضم المستخدم الروبوت الخاص بك إلى الدردشة الخاصة بك</b>",
        )
    
@USER.on_message(filters.group & filters.command(["طرد المساعد"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>لا يمكن للمستخدم مغادرة مجموعتك!  قد يكون الفيضان."
            "\n\nأو اطردني يدويًا من إلى مجموعتك</b>",
        )
        return
