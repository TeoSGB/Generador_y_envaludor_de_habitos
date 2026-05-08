from typing import Literal

from pydantic import BaseModel, Field, field_validator


class GeneratePlanRequest(BaseModel):
    goal: str = Field(
        ...,
        min_length=5,
        max_length=200,
        examples=["quiero mejorar mi condición física"],
    )
    level: Literal["principiante", "intermedio", "avanzado"] = Field(
        ...,
        examples=["principiante"],
    )
    available_time: str = Field(
        ...,
        min_length=3,
        max_length=80,
        examples=["20 minutos diarios"],
    )

    @field_validator("goal", "available_time")
    @classmethod
    def validate_not_empty(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("This field cannot be empty.")
        return cleaned_value


class GeneratePlanResponse(BaseModel):
    habits: list[str]
    weekly_plan: dict[str, list[str]]
    recommendations: list[str]
    prompt_used: str
