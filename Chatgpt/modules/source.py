# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio
from .. import Mukesh
from ..modules.buttons import *


@Mukesh.on_message(
    filters.command(["sourcrjfhfjrhe", "retkjtjtjtpo"], prefixes=["+", ".", "/", "-", "?", "$"])
)
async def source(_, m):
    await m.reply_photo(
        START_IMG,
        caption=SOURCE_TEXT,
        reply_markup=SOURCE_BUTTONS
    )