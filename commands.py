#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @mallum4


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_photo(
            photo="https://telegra.ph/file/0e2cc74172128ce35411f.jpg",
            caption=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup()
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                     ],
                     [
                         InlineKeyboardButton(
                            "⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/Mallum4")
                    ]
                 ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
