import os
from dotenv import load_dotenv
class Config:
    bot_token = os.getenv("BOT_TOKEN")