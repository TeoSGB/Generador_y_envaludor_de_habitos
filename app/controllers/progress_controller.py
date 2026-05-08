from app.models.progress import EvaluateProgressRequest, EvaluateProgressResponse
from app.services.progress_evaluation_service import ProgressEvaluationService


class ProgressController:
    """Controller for progress evaluation endpoints."""

    def __init__(self, progress_service: ProgressEvaluationService | None = None) -> None:
        self.progress_service = progress_service or ProgressEvaluationService()

    def evaluate_progress(self, payload: EvaluateProgressRequest) -> EvaluateProgressResponse:
        """Coordinate progress request data with the service layer."""
        return self.progress_service.evaluate_progress(payload)

