from pydantic import BaseModel


class HabitPlanHistoryItem(BaseModel):
    id: int
    goal: str
    level: str
    available_time: str
    habits: list[str]
    weekly_plan: dict[str, list[str]]
    recommendations: list[str]
    prompt_used: str
    created_at: str


class ProgressEvaluationHistoryItem(BaseModel):
    id: int
    goal: str
    completed_habits: list[str]
    missed_habits: list[str]
    notes: str
    score: int
    feedback: str
    strengths: list[str]
    areas_to_improve: list[str]
    next_recommendations: list[str]
    prompt_used: str
    created_at: str


class PromptImprovementHistoryItem(BaseModel):
    id: int
    original_prompt: str
    objective: str
    improved_prompt: str
    improvements_applied: list[str]
    explanation: str
    created_at: str


class HabitPlanHistoryResponse(BaseModel):
    items: list[HabitPlanHistoryItem]


class ProgressEvaluationHistoryResponse(BaseModel):
    items: list[ProgressEvaluationHistoryItem]


class PromptImprovementHistoryResponse(BaseModel):
    items: list[PromptImprovementHistoryItem]

