from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomEnvVariables(BaseSettings):
    # This class validates environment variables, that are written in pointed file.
    # Pointed file -> model_config
    MODE: str

    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return (f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:"
                f"{self.DATABASE_PORT}/{self.DATABASE_NAME}")
    @property
    def DATABASE_URL_psycopg(self):
        return (f"postgresql+psycopg2://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:"
                f"{self.DATABASE_PORT}/{self.DATABASE_NAME}")

    model_config = SettingsConfigDict(env_file=".test.env")


settings = CustomEnvVariables()
