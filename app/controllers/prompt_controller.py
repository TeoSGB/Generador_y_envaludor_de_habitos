from app.models.prompt import (
    ImprovePromptRequest,
    ImprovePromptResponse,
    PromptExamplesResponse,
)
from app.services.prompt_examples_service import PromptExamplesService
from app.services.prompt_improvement_service import PromptImprovementService


class PromptController:
    """Controller for prompting-related endpoints."""

    def __init__(
        self,
        improvement_service: PromptImprovementService | None = None,
        examples_service: PromptExamplesService | None = None,
    ) -> None:
        self.improvement_service = improvement_service or PromptImprovementService()
        self.examples_service = examples_service or PromptExamplesService()

    def improve_prompt(self, payload: ImprovePromptRequest) -> ImprovePromptResponse:
        """Coordinate prompt improvement request data with the service layer."""
        return self.improvement_service.improve_prompt(payload)

    def get_prompt_examples(self) -> PromptExamplesResponse:
        """Return prompt examples used by the application."""
        return self.examples_service.get_examples()

