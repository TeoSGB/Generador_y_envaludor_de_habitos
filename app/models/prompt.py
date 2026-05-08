from pydantic import BaseModel, Field, field_validator


class ImprovePromptRequest(BaseModel):
    original_prompt: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        examples=["Actúa como coach y dame hábitos"],
    )
    objective: str = Field(
        ...,
        min_length=3,
        max_length=300,
        examples=["obtener una respuesta más estructurada y en formato JSON"],
    )

    @field_validator("original_prompt", "objective")
    @classmethod
    def validate_not_empty(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("This field cannot be empty.")
        return cleaned_value


class ImprovePromptResponse(BaseModel):
    improved_prompt: str
    improvements_applied: list[str]
    explanation: str


class PromptExample(BaseModel):
    name: str
    description: str
    prompt: str


class PromptExamplesResponse(BaseModel):
    examples: list[PromptExample]
