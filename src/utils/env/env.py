import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY_JWT = os.getenv("SECRET_KEY_JWT")
DATABASE_URL = os.getenv("DATABASE_URL")

