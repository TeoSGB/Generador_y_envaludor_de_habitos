from app.models.plan import GeneratePlanResponse


def build_plan_response(
    habits: list[str],
    weekly_plan: dict[str, list[str]],
    recommendations: list[str],
    prompt_used: str,
) -> GeneratePlanResponse:
    """View helper that formats the generated habit plan response."""
    return GeneratePlanResponse(
        habits=habits,
        weekly_plan=weekly_plan,
        recommendations=recommendations,
        prompt_used=prompt_used,
    )

