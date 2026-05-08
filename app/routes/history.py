from fastapi import APIRouter

from app.controllers.history_controller import HistoryController
from app.models.history import (
    HabitPlanHistoryResponse,
    ProgressEvaluationHistoryResponse,
    PromptImprovementHistoryResponse,
)


router = APIRouter(prefix="/history", tags=["History"])
history_controller = HistoryController()


@router.get("/plans", response_model=HabitPlanHistoryResponse)
def get_habit_plan_history() -> HabitPlanHistoryResponse:
    """Return generated habit plans stored in the local SQLite database."""
    return history_controller.get_habit_plans()


@router.get("/progress", response_model=ProgressEvaluationHistoryResponse)
def get_progress_evaluation_history() -> ProgressEvaluationHistoryResponse:
    """Return progress evaluations stored in the local SQLite database."""
    return history_controller.get_progress_evaluations()


@router.get("/prompts", response_model=PromptImprovementHistoryResponse)
def get_prompt_improvement_history() -> PromptImprovementHistoryResponse:
    """Return prompt improvements stored in the local SQLite database."""
    return history_controller.get_prompt_improvements()

