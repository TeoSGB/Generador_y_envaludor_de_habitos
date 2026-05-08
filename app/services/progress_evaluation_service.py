from pathlib import Path

from app.exceptions import SimulatedInternalError
from app.models.progress import EvaluateProgressRequest, EvaluateProgressResponse
from app.services.context_analysis_service import GoalContext, analyze_goal
from app.views.progress_view import build_progress_response


class ProgressEvaluationService:
    """Business logic for evaluating habit progress with contextual feedback."""

    def __init__(self) -> None:
        self.prompt_template_path = (
            Path(__file__).resolve().parent.parent / "prompts" / "evaluate_progress_prompt.txt"
        )

    def evaluate_progress(self, payload: EvaluateProgressRequest) -> EvaluateProgressResponse:
        if "simulate_error" in payload.goal.lower():
            raise SimulatedInternalError("Unable to evaluate progress right now.")

        prompt_used = self._build_prompt(payload)
        context = analyze_goal(payload.goal)
        completed_count = len(payload.completed_habits)
        missed_count = len(payload.missed_habits)
        score = min(60 + (completed_count * 15) - (missed_count * 10), 100)
        score = max(score, 0)

        return build_progress_response(
            score=score,
            feedback=self._build_feedback(payload, context, score),
            strengths=self._build_strengths(payload, context),
            areas_to_improve=self._build_areas_to_improve(payload, context),
            next_recommendations=self._build_next_recommendations(payload, context),
            prompt_used=prompt_used,
        )

    def _build_feedback(
        self,
        payload: EvaluateProgressRequest,
        context: GoalContext,
        score: int,
    ) -> str:
        if score >= 80:
            progress_label = "muy buen avance"
        elif score >= 60:
            progress_label = "avance estable"
        else:
            progress_label = "avance inicial que necesita ajustes"

        return (
            f"Tienes un {progress_label} hacia {payload.goal}. "
            f"El foco principal es {context['focus']} y conviene seguir midiendo {context['metric']}."
        )

    def _build_strengths(
        self,
        payload: EvaluateProgressRequest,
        context: GoalContext,
    ) -> list[str]:
        completed = ", ".join(payload.completed_habits)
        return [
            f"Completaste: {completed}. Eso muestra accion real, no solo intencion.",
            f"Tu progreso esta conectado con {context['focus']}, que es el foco de tu objetivo.",
            "Registrar notas permite detectar patrones y mejorar el plan semanal.",
        ]

    def _build_areas_to_improve(
        self,
        payload: EvaluateProgressRequest,
        context: GoalContext,
    ) -> list[str]:
        areas = []
        if payload.missed_habits:
            areas.append(f"Revisar los habitos pendientes: {', '.join(payload.missed_habits)}.")
        else:
            areas.append("Mantener consistencia sin aumentar demasiado la dificultad.")

        areas.append(self._note_based_area(payload.notes))
        areas.append(f"Hacer mas visible el indicador principal: {context['metric']}.")
        return areas

    def _build_next_recommendations(
        self,
        payload: EvaluateProgressRequest,
        context: GoalContext,
    ) -> list[str]:
        recommendations = [
            f"Para la proxima semana, prioriza una accion central: {context['action']}.",
            context["support_habit"],
            context["reflection_habit"],
        ]

        if payload.missed_habits:
            recommendations.append(
                f"Reduce '{payload.missed_habits[0]}' a una version de 5 minutos para evitar abandono."
            )
        else:
            recommendations.append("Sube la dificultad solo un poco para proteger la constancia.")

        return recommendations

    def _note_based_area(self, notes: str) -> str:
        normalized_notes = notes.lower()
        if "tiempo" in normalized_notes or "organizar" in normalized_notes:
            return "Bloquear un horario fijo para que el habito no dependa de improvisar."
        if "energia" in normalized_notes or "cans" in normalized_notes:
            return "Ubicar el habito en el momento del dia con mas energia disponible."
        if "motiv" in normalized_notes:
            return "Usar una meta pequena para depender menos de la motivacion."
        return "Convertir la nota del usuario en un ajuste concreto para la siguiente semana."

    def _build_prompt(self, payload: EvaluateProgressRequest) -> str:
        template = self.prompt_template_path.read_text(encoding="utf-8")
        return template.format(
            goal=payload.goal,
            completed_habits=", ".join(payload.completed_habits),
            missed_habits=", ".join(payload.missed_habits) or "ninguno",
            notes=payload.notes,
        )

