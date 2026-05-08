from fastapi import APIRouter

from app.controllers.progress_controller import ProgressController
from app.models.progress import EvaluateProgressRequest, EvaluateProgressResponse


router = APIRouter(tags=["Progress Evaluation"])
progress_controller = ProgressController()


@router.post("/evaluate-progress", response_model=EvaluateProgressResponse)
def evaluate_progress(payload: EvaluateProgressRequest) -> EvaluateProgressResponse:
    """Route layer: receives progress data and delegates to the controller."""
    return progress_controller.evaluate_progress(payload)

