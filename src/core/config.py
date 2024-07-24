from typing import Any, Dict, List
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"
    TITLE: str = "Chat Application"
    ALLOWED_ORIGIN: str = "http://localhost:3000"
    EXPOSE_HEADER: str = ""
    DATABASE_URL: str = ""
    MONGO_INITDB_DATABASE: str = ""

    JWT_PUBLIC_KEY: str = ""
    JWT_PRIVATE_KEY: str = ""
    REFRESH_TOKEN_EXPIRES_IN: int = 0
    ACCESS_TOKEN_EXPIRES_IN: int = 0
    JWT_ALGORITHM: str = ""

    class Config:
        env_file = ".env"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "docs_url": self.API_PREFIX + self.DOCS_URL,
            "title": self.TITLE,
            "openapi_url": self.API_PREFIX + self.OPENAPI_URL,
            "redoc_url": self.API_PREFIX + self.REDOC_URL,
        }

    @property
    def get_allowed_origin(self) -> List[str]:
        return [x.strip() for x in self.ALLOWED_ORIGIN.split(",") if x]

    @property
    def get_expose_header(self) -> List[str]:
        return [x.strip() for x in self.EXPOSE_HEADER.split(",") if x]


def get_app_settings():
    """
    This function is a factory function that
    returns an instance of the AppSettings class.
    :return: A instance of the AppSettings
    """
    return AppSettings()
