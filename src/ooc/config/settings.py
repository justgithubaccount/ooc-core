from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Object-Oriented Consciousness"
    log_level: str = "DEBUG"

    class Config:
        env_file = ".env"

settings = Settings()
