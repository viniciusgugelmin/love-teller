from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")
MODE = os.getenv("MODE")
