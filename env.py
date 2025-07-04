import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27918253")
API_HASH = os.getenv("API_HASH", "52464e9f32a2c373b7cac0c821edf3d5")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SUDOERS = list(map(int, os.getenv("SUDOERS", "7093899037").split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1002304384234")
MUST_JOIN = os.getenv("MUST_JOIN", "Mrshubh_1227")
DISABLED = os.getenv("DISABLED", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
