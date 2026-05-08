from app.models.health import HealthResponse
from app.views.health_view import build_health_response


def get_health_status() -> HealthResponse:
    """Controller that coordinates the health check response."""
    return build_health_response()

