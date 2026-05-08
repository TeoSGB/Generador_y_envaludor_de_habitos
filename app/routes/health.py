from fastapi import APIRouter

from app.models.health import HealthResponse


router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return the current API status."""
    return HealthResponse(status="ok", message="Habit Coach API running")

