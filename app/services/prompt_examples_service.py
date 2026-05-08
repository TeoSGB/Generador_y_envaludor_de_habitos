from pathlib import Path

from app.models.prompt import PromptExample, PromptExamplesResponse
from app.views.prompt_view import build_prompt_examples_response


class PromptExamplesService:
    """Business logic for listing prompt templates used by the API."""

    def __init__(self) -> None:
        self.prompts_path = Path(__file__).resolve().parent.parent / "prompts"

    def get_examples(self) -> PromptExamplesResponse:
        examples = [
            PromptExample(
                name="Generate habit plan",
                description="Prompt para crear un plan semanal de hábitos personalizado.",
                prompt=self._read_prompt("habit_plan_prompt.txt"),
            ),
            PromptExample(
                name="Evaluate progress",
                description="Prompt para evaluar el avance del usuario y sugerir próximos pasos.",
                prompt=self._read_prompt("evaluate_progress_prompt.txt"),
            ),
        ]
        return build_prompt_examples_response(examples)

    def _read_prompt(self, filename: str) -> str:
        return (self.prompts_path / filename).read_text(encoding="utf-8")

