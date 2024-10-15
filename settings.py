import os
from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN = os.getenv("TG_TOKEN")
