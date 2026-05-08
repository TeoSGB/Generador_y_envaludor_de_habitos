from pydantic import BaseModel, Field


class GeneratePlanRequest(BaseModel):
    goal: str = Field(
        ...,
        min_length=5,
        max_length=200,
        examples=["quiero mejorar mi condición física"],
    )
    level: str = Field(
        ...,
        min_length=3,
        max_length=50,
        examples=["principiante"],
    )
    available_time: str = Field(
        ...,
        min_length=3,
        max_length=80,
        examples=["20 minutos diarios"],
    )


class GeneratePlanResponse(BaseModel):
    habits: list[str]
    weekly_plan: dict[str, list[str]]
    recommendations: list[str]
    prompt_used: str

