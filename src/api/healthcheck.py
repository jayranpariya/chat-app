""" Service Status Endpoint"""
from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter(tags=["Healthcheck"])


@router.get("/healthcheck", status_code=HTTPStatus.OK)
def health_check():
    """returns the service status"""
    return HTTPStatus.OK
