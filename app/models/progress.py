from pydantic import BaseModel, Field, field_validator


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

    @field_validator("goal", "notes")
    @classmethod
    def validate_not_empty(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("This field cannot be empty.")
        return cleaned_value

    @field_validator("completed_habits", "missed_habits")
    @classmethod
    def validate_habit_lists(cls, value: list[str]) -> list[str]:
        cleaned_items = [item.strip() for item in value if item.strip()]
        if len(cleaned_items) != len(value):
            raise ValueError("Habit lists cannot contain empty items.")
        return cleaned_items


class EvaluateProgressResponse(BaseModel):
    score: int = Field(..., ge=0, le=100)
    feedback: str
    strengths: list[str]
    areas_to_improve: list[str]
    next_recommendations: list[str]
    prompt_used: str
