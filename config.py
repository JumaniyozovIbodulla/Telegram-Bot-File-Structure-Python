from dotenv import load_dotenv
from os import getenv
load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
ADMINS = getenv("ADMINS")
ADMINS = ADMINS.split(", ")
DB_URL = getenv("DB_URL")
DB_NAME = getenv("DB_NAME")
DB_PASS = getenv("DB_PASS")
DB_USER = getenv("DB_USER")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")

# You can write another configs from .env file