from fastapi import APIRouter

from app.controllers.api_info_controller import get_api_info
from app.models.api_info import ApiInfoResponse


router = APIRouter(tags=["API Info"])


@router.get("/", response_model=ApiInfoResponse)
def api_info() -> ApiInfoResponse:
    """Route layer: exposes general API information."""
    return get_api_info()

