from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Krebsville Backend"
    environment: str = "development"
    database_url: str = "sqlite:///./krebsville.db"
    zone_data_path: str = str(Path(__file__).resolve().parents[2] / "data" / "firebase_zones.json")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
