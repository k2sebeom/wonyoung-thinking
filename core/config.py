import dotenv

from pydantic_settings import BaseSettings

import os

dotenv.load_dotenv()


class Config(BaseSettings):
    api_prefix: str = '/api'
    port: int = os.getenv('PORT') or 8080

    database_url: str = os.getenv('DATABASE_URL') or ''

    openai_key: str = os.getenv('OPENAI_KEY') or ''

config: Config = Config()
