from app.models.progress import EvaluateProgressResponse


def build_progress_response(
    score: int,
    feedback: str,
    strengths: list[str],
    areas_to_improve: list[str],
    next_recommendations: list[str],
    prompt_used: str,
) -> EvaluateProgressResponse:
    """View helper that formats the progress evaluation response."""
    return EvaluateProgressResponse(
        score=score,
        feedback=feedback,
        strengths=strengths,
        areas_to_improve=areas_to_improve,
        next_recommendations=next_recommendations,
        prompt_used=prompt_used,
    )

