from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from src.core.config import get_app_settings

settings = get_app_settings()

router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN


@router.post("/register", status_code=status.HTTP_200_OK)
async def register(request: Request):
