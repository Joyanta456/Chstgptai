# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID", "19580422")
API_HASH = environ.get("API_HASH", "0ea3c25451bfba7c5b69895e3a454463")
BOT_TOKEN = environ.get("BOT_TOKEN", "6939162393:AAENT5n_SgOY1zVJQZjUgxEpt-yOdA2L5rE")
ADMIN = int(environ.get("ADMIN", "5953239864"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002220975470"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1001996681486")
MONGO_URL = environ.get(
    "MONGO_URL", "mongodb+srv://main1564:main1564@cluster0.dnqkxpr.mongodb.net/?retryWrites=true&w=majority")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1001986933012")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
