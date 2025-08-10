"""
from os import getenv


API_ID = int(getenv("API_ID", "21157244"))
API_HASH = getenv("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")
BOT_TOKEN = getenv("BOT_TOKEN", "8328503898:AAGi2oT7SrEM3U9EWmVJyu1iDzZDLliWL2c")
OWNER_ID = int(getenv("OWNER_ID", "1783306092"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1783306092").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://saraswatisharmapbc:L8aRiWhBbhi8mFwN@cluster0.gxhxgye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002758652479"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002758652479"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "21157244"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8328503898:AAGi2oT7SrEM3U9EWmVJyu1iDzZDLliWL2c")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Gajjukadownloder_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1783306092"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1783306092").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002758652479"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://saraswatisharmapbc:L8aRiWhBbhi8mFwN@cluster0.gxhxgye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002758652479"))

