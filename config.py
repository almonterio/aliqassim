## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCT0ciRaXctvA4Ra8ukPgAVJxhiQOFXyUOyNNtarPSN_veUvhnfU1R-JUgKE6zX2MHbMMle-xWppO9aSOi6nrNdcGQ7TgRumf7Uvp_hkq2UEj8OTKDkg07STTYsW_e1fY5839cikXQ_LLXlaDho7BJ_0Gem-T_nqk4hl-ALkPvdh88LI5aO6EYbcyU3T2Babl9FPKhgyLqE-jV9qAe5HGOT8p8tjrgCkrALxb8krQh4CwXv1kKZ06p4OSJ4y7Y-glK3392gy41GEikBxB5aOReOviQ_BvKI874vplZAUzqPnMZeD4kt8juozrgPS4O8kbxyyrYCvBggjNHdC-i7XbGAaOZcMgA")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", "12311076"))
API_HASH = getenv("API_HASH", "15c0be947edb53eda9c81fedbdc34f03")
OWNER_NAME = getenv("OWNER_NAME", "Ali Qassim")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ibv80")
ALIVE_NAME = getenv("ALIVE_NAME", "aliqassim")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_ID = getenv("OWNER_ID", "5494083050")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SPOTIFY")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5494083050").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/1405bf4c95bb63823fb3b.jpg")
