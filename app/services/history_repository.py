import json

from app.database import get_connection, init_database
from app.models.history import (
    HabitPlanHistoryItem,
    HabitPlanHistoryResponse,
    ProgressEvaluationHistoryItem,
    ProgressEvaluationHistoryResponse,
    PromptImprovementHistoryItem,
    PromptImprovementHistoryResponse,
)
from app.models.plan import GeneratePlanRequest, GeneratePlanResponse
from app.models.progress import EvaluateProgressRequest, EvaluateProgressResponse
from app.models.prompt import ImprovePromptRequest, ImprovePromptResponse


class HistoryRepository:
    """Persistence layer for the local simulated SQLite database."""

    def save_habit_plan(
        self,
        request: GeneratePlanRequest,
        response: GeneratePlanResponse,
    ) -> None:
        init_database()
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO habit_plans (
                    goal, level, available_time, habits, weekly_plan,
                    recommendations, prompt_used
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    request.goal,
                    request.level,
                    request.available_time,
                    json.dumps(response.habits, ensure_ascii=False),
                    json.dumps(response.weekly_plan, ensure_ascii=False),
                    json.dumps(response.recommendations, ensure_ascii=False),
                    response.prompt_used,
                ),
            )

    def save_progress_evaluation(
        self,
        request: EvaluateProgressRequest,
        response: EvaluateProgressResponse,
    ) -> None:
        init_database()
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO progress_evaluations (
                    goal, completed_habits, missed_habits, notes, score,
                    feedback, strengths, areas_to_improve, next_recommendations,
                    prompt_used
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    request.goal,
                    json.dumps(request.completed_habits, ensure_ascii=False),
                    json.dumps(request.missed_habits, ensure_ascii=False),
                    request.notes,
                    response.score,
                    response.feedback,
                    json.dumps(response.strengths, ensure_ascii=False),
                    json.dumps(response.areas_to_improve, ensure_ascii=False),
                    json.dumps(response.next_recommendations, ensure_ascii=False),
                    response.prompt_used,
                ),
            )

    def save_prompt_improvement(
        self,
        request: ImprovePromptRequest,
        response: ImprovePromptResponse,
    ) -> None:
        init_database()
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO prompt_improvements (
                    original_prompt, objective, improved_prompt,
                    improvements_applied, explanation
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    request.original_prompt,
                    request.objective,
                    response.improved_prompt,
                    json.dumps(response.improvements_applied, ensure_ascii=False),
                    response.explanation,
                ),
            )

    def get_habit_plans(self) -> HabitPlanHistoryResponse:
        init_database()
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM habit_plans ORDER BY id DESC LIMIT 20"
            ).fetchall()
        return HabitPlanHistoryResponse(
            items=[
                HabitPlanHistoryItem(
                    id=row["id"],
                    goal=row["goal"],
                    level=row["level"],
                    available_time=row["available_time"],
                    habits=json.loads(row["habits"]),
                    weekly_plan=json.loads(row["weekly_plan"]),
                    recommendations=json.loads(row["recommendations"]),
                    prompt_used=row["prompt_used"],
                    created_at=row["created_at"],
                )
                for row in rows
            ]
        )

    def get_progress_evaluations(self) -> ProgressEvaluationHistoryResponse:
        init_database()
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM progress_evaluations ORDER BY id DESC LIMIT 20"
            ).fetchall()
        return ProgressEvaluationHistoryResponse(
            items=[
                ProgressEvaluationHistoryItem(
                    id=row["id"],
                    goal=row["goal"],
                    completed_habits=json.loads(row["completed_habits"]),
                    missed_habits=json.loads(row["missed_habits"]),
                    notes=row["notes"],
                    score=row["score"],
                    feedback=row["feedback"],
                    strengths=json.loads(row["strengths"]),
                    areas_to_improve=json.loads(row["areas_to_improve"]),
                    next_recommendations=json.loads(row["next_recommendations"]),
                    prompt_used=row["prompt_used"],
                    created_at=row["created_at"],
                )
                for row in rows
            ]
        )

    def get_prompt_improvements(self) -> PromptImprovementHistoryResponse:
        init_database()
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM prompt_improvements ORDER BY id DESC LIMIT 20"
            ).fetchall()
        return PromptImprovementHistoryResponse(
            items=[
                PromptImprovementHistoryItem(
                    id=row["id"],
                    original_prompt=row["original_prompt"],
                    objective=row["objective"],
                    improved_prompt=row["improved_prompt"],
                    improvements_applied=json.loads(row["improvements_applied"]),
                    explanation=row["explanation"],
                    created_at=row["created_at"],
                )
                for row in rows
            ]
        )

