"""
doc url: https://fastapi.tiangolo.com/advanced/settings/
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    sqlalchemy_url: str

    class Config:
        env_file = ".env"


settings = Settings()
