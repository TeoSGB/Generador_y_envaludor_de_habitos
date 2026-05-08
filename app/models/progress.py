from pydantic import BaseModel, Field


class EvaluateProgressRequest(BaseModel):
    goal: str = Field(
        ...,
        min_length=5,
        max_length=200,
        examples=["mejorar mi condición física"],
    )
    completed_habits: list[str] = Field(
        ...,
        min_length=1,
        examples=[["caminar 20 minutos", "tomar agua"]],
    )
    missed_habits: list[str] = Field(
        default_factory=list,
        examples=[["dormir 7 horas"]],
    )
    notes: str = Field(
        ...,
        min_length=3,
        max_length=300,
        examples=["me costó organizar mi tiempo"],
    )


class EvaluateProgressResponse(BaseModel):
    score: int = Field(..., ge=0, le=100)
    feedback: str
    strengths: list[str]
    areas_to_improve: list[str]
    next_recommendations: list[str]
    prompt_used: str

