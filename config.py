import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 23699269
API_HASH = "bb463012fd5e9dd2293114a494a16fa2"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", none)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = getenv("BOT_TOKEN", default="7507562002:AAFSz7Rw39uuo5r-cyQ_277XpvwOg6jaXJA")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default="7423778494:AAHd-1diKigc4tfXmH-P5Up8kUnfSwL2ymY")
BOT_TOKEN3 = getenv("BOT_TOKEN3", default="7347890396:AAHuf6IRXj_Z1vzMlvFB9MpS-dXvqQg4OYM")
BOT_TOKEN4 = getenv("BOT_TOKEN4", default="7437959645:AAGmY9fFjDhDFsuvXwKFcXlPYLaUkVd96pM")
BOT_TOKEN5 = getenv("BOT_TOKEN5", default="7325675339:AAFRXj0UwOObgLUxIggRWM38Z1QbUzc1q1U")
BOT_TOKEN6 = getenv("BOT_TOKEN6", default="7006936943:AAETRLzoeCG0rYpqZo5BQx1eXhk_-ZUGKEQ")
BOT_TOKEN7 = getenv("BOT_TOKEN7", default="7493058564:AAH9IexkMgT_WO-EOvTq2mRTrhZLKFonREY")
BOT_TOKEN8 = getenv("BOT_TOKEN8", default="7532621253:AAF5ti8vGCZ02FKhp40EQFdNrqq7wjlJYKg")
BOT_TOKEN9 = getenv("BOT_TOKEN9", default="7394984131:AAGUrJ5LQT6Kamuz16gLrDc0ySoYX_4-1W4")
BOT_TOKEN10 = getenv("BOT_TOKEN10", default="7218398498:AAFoXyu0LdTT55UofUb0iJXOR81tnOMtg1I")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7233676524", "7496704336", "7095028493").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7189651838"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
