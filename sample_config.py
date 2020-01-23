import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("9cf64d2e-9c70-439e-a66e-8cbb0b524d79", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("990921094:AAGalaghfDF_NuUUJUvbu5cFP-VObllTIJc", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("1104007", 12345))
    API_HASH = os.environ.get("4ed43d52342463ad74846b57a28bdc4e")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(str(x) for x in os.environ.get("749293934", "").split())
    # reg: Procedures
    UTUBE_BOT_USERS = set(str(x) for x in os.environ.get("UTUBE_BOT_USERS", "").split())
    SUPER_DLBOT_USERS = set(str(x) for x in os.environ.get("SUPER_DLBOT_USERS", "").split()) 
    SUPER3X_DLBOT_USERS = set(str(x) for x in os.environ.get("SUPER3X_DLBOT_USERS", "").split())
    SUPER7X_DLBOT_USERS = set(str(x) for x in os.environ.get("SUPER7X_DLBOT_USERS", "").split())
    BANNED_USERS = set(str(x) for x in os.environ.get("BANNED_USERS", "").split())
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("128", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # for storing the user details
    DB_SQLALCHEMY = "USERS.session"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("180.179.98.22:3128", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = os.environ.get("OUO_IO_API_KEY", None)
    # for Google Custom Search Engine
    GCS_API_KEY = os.environ.get("GCS_API_KEY", None)
    GCS_SE_ID = os.environ.get("GCS_SE_ID", None)
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # dict to hold Google Drive SignIns
    G_DRIVE_AUTH_DRQ = {}
