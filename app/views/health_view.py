from app.models.health import HealthResponse


def build_health_response() -> HealthResponse:
    """View helper that formats the health endpoint response."""
    return HealthResponse(status="ok", message="Habit Coach API running")

