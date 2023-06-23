# (©)Codexbotz
# Recife By @ursickfeeling
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5852789787:AAGgWHVQNbPa-l82fJX13KPdjg74McLT3FU")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001883918193"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "panggil_y")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://bvvcjupm:6u5sqQjOGxFlaarQfBsJDL_JFOqKiPjG@rosie.db.elephantsql.com/bvvcjupm")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "none")
GROUP = os.environ.get("GROUP", " none")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001294277942")
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001139356121")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001771370225")
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1001720661288")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\nJoin aja diem-diem ya, ga usah banyak tanya kalaw mau asupan free\n\nJika bot bermasalah hub @teknisi69_bot.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1856497356").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nJoin aja diem-diem ya, gak usah banyak tanya kalaw mau asupan free\n\nJika bot bermasalah hub @teknisi69_bot. </b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(1856497356)
ADMINS.append(1750080384)
ADMINS.append(5360457944) 
ADMINS.append(0)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
