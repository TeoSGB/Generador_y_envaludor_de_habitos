from fastapi import APIRouter

from app.controllers.health_controller import get_health_status
from app.models.health import HealthResponse


router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Route layer: exposes the health endpoint."""
    return get_health_status()
