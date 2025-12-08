from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    OPENAI_API_KEY: str = ""
    # Add other keys as needed

    class Config:
        env_file = ".env"

settings = Settings()
