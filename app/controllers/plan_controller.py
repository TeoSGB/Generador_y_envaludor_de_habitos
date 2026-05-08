from app.models.plan import GeneratePlanRequest, GeneratePlanResponse
from app.services.habit_plan_service import HabitPlanService


class PlanController:
    """Controller for habit plan endpoints."""

    def __init__(self, habit_plan_service: HabitPlanService | None = None) -> None:
        self.habit_plan_service = habit_plan_service or HabitPlanService()

    def generate_plan(self, payload: GeneratePlanRequest) -> GeneratePlanResponse:
        """Coordinate request data with the service layer."""
        return self.habit_plan_service.generate_plan(payload)

