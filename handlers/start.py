from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, an open-source bot that lets you play music in your Telegram groups.For Support Join our group @W2HSupport.\n\n The Assistant must be in your group to play music in the voice chat of your group.\n\n /help to know my commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πππππππβ‘οΈ", url="https://t.me/DOSTI_GROUP_1234"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πππππβ‘οΈ", url="https://t.me/abhinasroy"
                    ),
                    InlineKeyboardButton(
                        "πΎππΌππππβ‘οΈ", url="https://t.me/MOVIE_CHANNEL_1234"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πππππ ππ πΏπΌππβ‘οΈ", url="https://t.me/RANI_MUSIC_BOT?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
