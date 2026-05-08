from app.models.api_info import ApiInfoResponse
from app.views.api_info_view import build_api_info_response


def get_api_info() -> ApiInfoResponse:
    """Controller that returns general API information."""
    return build_api_info_response()

