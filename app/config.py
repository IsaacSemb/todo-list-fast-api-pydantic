import os
from typing import Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_DB_PATH = os.path.join(BASE_DIR, "app.db")
SQLITE_DB_URL = f"sqlite:///{SQLITE_DB_PATH}"

class Settings(BaseSettings):
    SECRET_KEY: str = "fueling-is-key!"
    DEBUG: bool = True
    DATABASE_URL: str = SQLITE_DB_URL
    
    class Config:
        env_file = ".env"

CONFIG = Settings()
