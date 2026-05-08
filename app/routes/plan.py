from fastapi import APIRouter

from app.models.plan import GeneratePlanRequest, GeneratePlanResponse
from app.services.habit_plan_service import HabitPlanService


router = APIRouter(tags=["Habit Plans"])
habit_plan_service = HabitPlanService()


@router.post("/generate-plan", response_model=GeneratePlanResponse)
def generate_plan(payload: GeneratePlanRequest) -> GeneratePlanResponse:
    """Generate a simulated habit plan from a structured prompt."""
    return habit_plan_service.generate_plan(payload)

