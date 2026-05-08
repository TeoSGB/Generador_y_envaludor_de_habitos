from app.models.history import (
    HabitPlanHistoryResponse,
    ProgressEvaluationHistoryResponse,
    PromptImprovementHistoryResponse,
)
from app.services.history_repository import HistoryRepository


class HistoryController:
    """Controller for local database history endpoints."""

    def __init__(self, history_repository: HistoryRepository | None = None) -> None:
        self.history_repository = history_repository or HistoryRepository()

    def get_habit_plans(self) -> HabitPlanHistoryResponse:
        return self.history_repository.get_habit_plans()

    def get_progress_evaluations(self) -> ProgressEvaluationHistoryResponse:
        return self.history_repository.get_progress_evaluations()

    def get_prompt_improvements(self) -> PromptImprovementHistoryResponse:
        return self.history_repository.get_prompt_improvements()

