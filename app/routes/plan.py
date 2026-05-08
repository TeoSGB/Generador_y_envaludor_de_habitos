from fastapi import APIRouter

from app.controllers.plan_controller import PlanController
from app.models.plan import GeneratePlanRequest, GeneratePlanResponse


router = APIRouter(tags=["Habit Plans"])
plan_controller = PlanController()


@router.post("/generate-plan", response_model=GeneratePlanResponse)
def generate_plan(payload: GeneratePlanRequest) -> GeneratePlanResponse:
    """Route layer: receives the request and delegates to the controller."""
    return plan_controller.generate_plan(payload)
