from app.models.api_info import ApiInfoResponse


def build_api_info_response() -> ApiInfoResponse:
    """View helper that formats general API information."""
    return ApiInfoResponse(
        name="Habit Coach API",
        version="1.0.0",
        description=(
            "API for generating and evaluating personalized habit plans "
            "using prompt engineering principles"
        ),
        docs="/docs",
    )

