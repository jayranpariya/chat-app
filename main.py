
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from src.api import healthcheck
from src.core.config import get_app_settings

app_settings = get_app_settings()

app = FastAPI(**app_settings.fastapi_kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.get_allowed_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=app_settings.get_expose_header,
)

app.include_router(healthcheck.router, prefix=app_settings.API_PREFIX)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
