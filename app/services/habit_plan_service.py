from pathlib import Path

from app.models.plan import GeneratePlanRequest, GeneratePlanResponse
from app.views.plan_view import build_plan_response


class HabitPlanService:
    """Business logic for building prompts and simulating AI responses."""

    def __init__(self) -> None:
        self.prompt_template_path = (
            Path(__file__).resolve().parent.parent / "prompts" / "habit_plan_prompt.txt"
        )

    def generate_plan(self, payload: GeneratePlanRequest) -> GeneratePlanResponse:
        prompt_used = self._build_prompt(payload)

        # This is a deterministic simulation of an AI response.
        # In a future phase, this method can call a real LLM provider.
        habits = [
            f"Dedicar {payload.available_time} a una acción relacionada con: {payload.goal}.",
            "Registrar el avance diario en una nota simple.",
            "Revisar al final del día qué funcionó y qué puede mejorar.",
        ]

        weekly_plan = {
            "lunes": ["Definir una meta pequeña para la semana.", "Realizar la primera sesión."],
            "martes": ["Repetir el hábito principal.", "Registrar energía y dificultad."],
            "miércoles": ["Mantener una sesión ligera.", "Ajustar el plan si fue muy exigente."],
            "jueves": ["Repetir el hábito principal.", "Identificar una barrera común."],
            "viernes": ["Completar una sesión enfocada.", "Celebrar un avance concreto."],
            "sábado": ["Hacer una versión flexible del hábito.", "Preparar el entorno para la próxima semana."],
            "domingo": ["Descansar activamente.", "Revisar aprendizajes de la semana."],
        }

        recommendations = [
            "Empieza con una versión tan sencilla que sea difícil fallar.",
            "Mantén el mismo horario durante la primera semana.",
            "Evalúa el progreso por constancia, no por perfección.",
        ]

        return build_plan_response(habits, weekly_plan, recommendations, prompt_used)

    def _build_prompt(self, payload: GeneratePlanRequest) -> str:
        template = self.prompt_template_path.read_text(encoding="utf-8")
        return template.format(
            goal=payload.goal,
            level=payload.level,
            available_time=payload.available_time,
        )
