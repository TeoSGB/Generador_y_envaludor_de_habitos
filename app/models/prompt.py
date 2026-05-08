from pydantic import BaseModel, Field


class ImprovePromptRequest(BaseModel):
    original_prompt: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        examples=["Actúa como coach y dame hábitos"],
    )
    objective: str = Field(
        ...,
        min_length=10,
        max_length=300,
        examples=["obtener una respuesta más estructurada y en formato JSON"],
    )


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

