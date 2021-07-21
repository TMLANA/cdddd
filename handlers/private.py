from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا **{bn}** 🎵

بامكاني تشغيل الاغاني في المكالمات الجماعيه 
قم قم برفعي  مشرف في قناتك مع البوت المساعد [MusicTelethon](https://t.me/MUSICEDL).

قم باضافتي الى مجموعتك لتبدأ الحفله 🎶**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 لطلب المساعده 🛠", url="https://t.me/cDDDD")
                  ],[
                    InlineKeyboardButton(
                        "💬 المطور الثاني ", url="https://t.me/MS_SS"
                    ),
                    InlineKeyboardButton(
                        "🔊 قناتي", url="https://t.me/vvvvisn"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕  اضفني الى مجموعتك ➕", url="https://t.me/SERRVBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي الخاصه", url="https://t.me/vvvvisn")
                ]
            ]
        )
   )


@Client.on_message(filters.command("اوامر") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** ░يمتاز هذا البوت بالبحث والتحميل░

اكتب معرف البوت مع اسم الاغنيه للبحث ıllı♬

↜مثال↝: 

 《 @SERRVBOT كاظم الساهر 》

░تستطيع تحميل اي اغنيه ايضا 💞

بالاوامر التاليه░ :

 ¹↜اغنية↝ıllı رابط الاغنيه من اليوتيوب 

 ²↜بحث↝ıllı رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه ✆

³↜تشغيل↝ıllı بالرد على الاغنيه او الرابط للتشغيل

⁴↜ايقاف↝ıllı لايقاف الاغنيه موقتا داخل المكالمه

⁵↜استئناف↝ıllı لتكمله الاغنيه المتوقفه

⁶↜انهاء↝ıllı لانهاء البوت عن تشغيل الاغنيه

⁷↜تخطي↝ıllı لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه

⁸↜دعوة المساعد↝ıllı لدعوة البوت المساعد للمجموعة 

#ملاحظه↝: تستطيع ان تقوم بتشغيل اغنيه اخرى فتضاف الى الدور بعد الاغنيه الحاليه فتتنقل بينها وبين الاغاني الباقيه باستخدام امر ↜تخطي↝ıllı 🔖 **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي الخاصه", url="https://t.me/vvvvisn")
                ],[
                    InlineKeyboardButton(
                        "🎶 الحساب المساعد", url="https://t.me/MUSICEDL"
                    )
                ]
            ]
        )
   )
