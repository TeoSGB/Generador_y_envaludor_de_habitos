from pathlib import Path

from app.exceptions import SimulatedInternalError
from app.models.progress import EvaluateProgressRequest, EvaluateProgressResponse
from app.views.progress_view import build_progress_response


class ProgressEvaluationService:
    """Business logic for evaluating habit progress with a structured prompt."""

    def __init__(self) -> None:
        self.prompt_template_path = (
            Path(__file__).resolve().parent.parent / "prompts" / "evaluate_progress_prompt.txt"
        )

    def evaluate_progress(self, payload: EvaluateProgressRequest) -> EvaluateProgressResponse:
        if "simulate_error" in payload.goal.lower():
            raise SimulatedInternalError("Unable to evaluate progress right now.")

        prompt_used = self._build_prompt(payload)
        completed_count = len(payload.completed_habits)
        missed_count = len(payload.missed_habits)
        score = min(60 + (completed_count * 15) - (missed_count * 10), 100)
        score = max(score, 0)

        feedback = (
            f"Vas por buen camino hacia tu objetivo de {payload.goal}. "
            "La clave ahora es mantener lo que ya funcionó y ajustar los hábitos pendientes."
        )

        strengths = [
            f"Completaste {completed_count} hábito(s), lo que muestra constancia.",
            "Registraste notas sobre tu experiencia, una práctica útil para mejorar.",
        ]

        areas_to_improve = [
            f"Trabajar en los hábitos pendientes: {', '.join(payload.missed_habits)}."
            if payload.missed_habits
            else "Mantener la consistencia sin aumentar demasiado la dificultad.",
            "Organizar un horario fijo para reducir fricción diaria.",
        ]

        next_recommendations = [
            "Elige un horario específico para el hábito más importante.",
            "Reduce el hábito pendiente a una versión de 5 minutos si el día está difícil.",
            "Revisa tu progreso cada domingo y ajusta solo una cosa a la vez.",
        ]

        return build_progress_response(
            score=score,
            feedback=feedback,
            strengths=strengths,
            areas_to_improve=areas_to_improve,
            next_recommendations=next_recommendations,
            prompt_used=prompt_used,
        )

    def _build_prompt(self, payload: EvaluateProgressRequest) -> str:
        template = self.prompt_template_path.read_text(encoding="utf-8")
        return template.format(
            goal=payload.goal,
            completed_habits=", ".join(payload.completed_habits),
            missed_habits=", ".join(payload.missed_habits) or "ninguno",
            notes=payload.notes,
        )
