from app.models.prompt import (
    ImprovePromptResponse,
    PromptExample,
    PromptExamplesResponse,
)


def build_improve_prompt_response(
    improved_prompt: str,
    improvements_applied: list[str],
    explanation: str,
) -> ImprovePromptResponse:
    """View helper that formats the prompt improvement response."""
    return ImprovePromptResponse(
        improved_prompt=improved_prompt,
        improvements_applied=improvements_applied,
        explanation=explanation,
    )


def build_prompt_examples_response(examples: list[PromptExample]) -> PromptExamplesResponse:
    """View helper that formats available prompt examples."""
    return PromptExamplesResponse(examples=examples)

