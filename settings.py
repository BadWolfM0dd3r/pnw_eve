from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
PNW_API_KEY = os.environ.get('PNW_API_KEY')
PNW_BASE_URL = os.environ.get('PNW_BASE_URL')
PNW_ALLIANCE_ID = os.environ.get('PNW_ALLIANCE_ID')
