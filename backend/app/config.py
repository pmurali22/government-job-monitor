import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/job_monitor')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'change-me')
    GEMINI_API_KEY: str = os.getenv('GEMINI_API_KEY', '')
    EMAIL_FROM: str = os.getenv('EMAIL_FROM', 'noreply@example.com')
    TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN', '')
    TELEGRAM_CHAT_ID: str = os.getenv('TELEGRAM_CHAT_ID', '')
    class Config:
        env_file = '.env'

settings = Settings()
