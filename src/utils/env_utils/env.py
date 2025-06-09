from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY_JWT = os.getenv("SECRET_KEY_JWT")
