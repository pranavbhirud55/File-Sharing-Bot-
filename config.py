#(©)CodeXBotz

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7264723971:AAHVLcerGqQpdptUswNL_hOLs2Dd2suRIEI")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29674380"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9a73b874a8e0129ac9eb89e50e64ab9a")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002182852306"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6708627355"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jayeshkunal64:jayeshkunal64@cluster0.tnaquxy.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "file-storage")

# Force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002183430157"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "5490584692").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello Bhai\n\nDekh Agar tuze videos dekhni hai to ye channel join karna padega")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Set true if you want to Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
