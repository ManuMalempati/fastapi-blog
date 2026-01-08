from typing import Optional
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "blog"
    PROJECT_VERSION: str = "0.1.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

    if DATABASE_URL is None:
        POSTGRES_USER = os.getenv("POSTGRES_USER")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
        POSTGRES_DB = os.getenv("POSTGRES_DB")

        DATABASE_URL = (
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
            f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
        )

settings = Settings()
