from fastapi import APIRouter

from app.controllers.prompt_controller import PromptController
from app.models.prompt import (
    ImprovePromptRequest,
    ImprovePromptResponse,
    PromptExamplesResponse,
)


router = APIRouter(tags=["Prompting"])
prompt_controller = PromptController()


@router.post("/improve-prompt", response_model=ImprovePromptResponse)
def improve_prompt(payload: ImprovePromptRequest) -> ImprovePromptResponse:
    """Route layer: receives a basic prompt and delegates improvement."""
    return prompt_controller.improve_prompt(payload)


@router.get("/prompt-examples", response_model=PromptExamplesResponse)
def get_prompt_examples() -> PromptExamplesResponse:
    """Route layer: lists prompt templates used by the application."""
    return prompt_controller.get_prompt_examples()

