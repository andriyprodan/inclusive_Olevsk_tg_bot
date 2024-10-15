import os
from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN = os.environ.get("TG_TOKEN")