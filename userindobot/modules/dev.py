import os
import subprocess
import sys
from time import sleep
from typing import List

from telegram import Bot, Update, TelegramError
from telegram.ext import CommandHandler, run_async

from userindobot import dispatcher
from userindobot.modules.helper_funcs.chat_status import dev_plus


@run_async
@dev_plus
def leave(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
            message.reply_text(
                "Beep boop, I left that soup!.")
        except TelegramError:
            message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho).")
    else:
        message.reply_text("Send a valid chat ID")


LEAVE_HANDLER = CommandHandler("leave", leave, pass_args=True)

dispatcher.add_handler(LEAVE_HANDLER)

__mod_name__ = "Dev"
__handlers__ = [LEAVE_HANDLER]
