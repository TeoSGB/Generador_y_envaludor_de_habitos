from pathlib import Path

from app.exceptions import SimulatedInternalError
from app.models.plan import GeneratePlanRequest, GeneratePlanResponse
from app.services.context_analysis_service import GoalContext, analyze_goal, get_level_guidance
from app.services.history_repository import HistoryRepository
from app.views.plan_view import build_plan_response


class HabitPlanService:
    """Business logic for building prompts and simulating contextual AI responses."""

    def __init__(self) -> None:
        self.prompt_template_path = (
            Path(__file__).resolve().parent.parent / "prompts" / "habit_plan_prompt.txt"
        )
        self.history_repository = HistoryRepository()

    def generate_plan(self, payload: GeneratePlanRequest) -> GeneratePlanResponse:
        if "simulate_error" in payload.goal.lower():
            raise SimulatedInternalError("Unable to generate the habit plan right now.")

        prompt_used = self._build_prompt(payload)
        context = analyze_goal(payload.goal)
        level_guidance = get_level_guidance(payload.level)

        response = build_plan_response(
            habits=self._build_contextual_habits(payload, context, level_guidance),
            weekly_plan=self._build_weekly_plan(payload, context),
            recommendations=self._build_recommendations(payload, context, level_guidance),
            prompt_used=prompt_used,
        )
        self.history_repository.save_habit_plan(payload, response)
        return response

    def _build_contextual_habits(
        self,
        payload: GeneratePlanRequest,
        context: GoalContext,
        level_guidance: str,
    ) -> list[str]:
        return [
            f"Dedicar {payload.available_time} a {context['action']} para avanzar en: {payload.goal}.",
            context["starter_habit"],
            context["support_habit"],
            f"Medir el progreso con este indicador: {context['metric']}. {level_guidance}",
        ]

    def _build_weekly_plan(
        self,
        payload: GeneratePlanRequest,
        context: GoalContext,
    ) -> dict[str, list[str]]:
        intensity_by_level = {
            "principiante": "version corta y facil",
            "intermedio": "version completa con seguimiento",
            "avanzado": "version retadora con medicion precisa",
        }
        intensity = intensity_by_level[payload.level]

        return {
            "lunes": [
                f"Definir una meta semanal para {context['focus']}.",
                f"Hacer una {intensity} durante {payload.available_time}.",
            ],
            "martes": [
                context["starter_habit"],
                f"Registrar {context['metric']}.",
            ],
            "miercoles": [
                f"Repetir {context['action']} con menor friccion.",
                context["reflection_habit"],
            ],
            "jueves": [
                context["support_habit"],
                f"Ajustar el entorno para proteger {payload.available_time}.",
            ],
            "viernes": [
                f"Completar una sesion enfocada en {context['focus']}.",
                "Comparar el avance con el inicio de la semana.",
            ],
            "sabado": [
                f"Hacer una practica flexible relacionada con {payload.goal}.",
                "Preparar una mejora pequena para la proxima semana.",
            ],
            "domingo": [
                "Revisar logros, obstaculos y aprendizajes.",
                f"Elegir el siguiente paso para {context['focus']}.",
            ],
        }

    def _build_recommendations(
        self,
        payload: GeneratePlanRequest,
        context: GoalContext,
        level_guidance: str,
    ) -> list[str]:
        return [
            f"Conecta el habito con tu objetivo: {payload.goal}.",
            f"Reserva {payload.available_time} en un horario fijo para reducir decisiones.",
            level_guidance,
            f"Evalua el avance usando {context['metric']}, no solo motivacion.",
        ]

    def _build_prompt(self, payload: GeneratePlanRequest) -> str:
        template = self.prompt_template_path.read_text(encoding="utf-8")
        return template.format(
            goal=payload.goal,
            level=payload.level,
            available_time=payload.available_time,
        )
