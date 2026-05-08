from pathlib import Path

from app.models.prompt import ImprovePromptRequest, ImprovePromptResponse
from app.views.prompt_view import build_improve_prompt_response


class PromptImprovementService:
    """Business logic for improving prompts with clear prompting principles."""

    def __init__(self) -> None:
        self.prompt_template_path = (
            Path(__file__).resolve().parent.parent / "prompts" / "improve_prompt_template.txt"
        )

    def improve_prompt(self, payload: ImprovePromptRequest) -> ImprovePromptResponse:
        prompt_used = self._build_prompt(payload)
        improved_prompt = (
            "Actúa como un coach de hábitos especializado en crear planes claros, realistas y medibles.\n\n"
            f"Contexto: el usuario necesita {payload.objective}.\n"
            f"Prompt original a mejorar: {payload.original_prompt}\n\n"
            "Instrucciones:\n"
            "1. Propón hábitos pequeños y sostenibles.\n"
            "2. Explica cada recomendación en una frase breve.\n"
            "3. Organiza la respuesta por secciones.\n"
            "4. Evita recomendaciones extremas o ambiguas.\n\n"
            "Formato de salida esperado en JSON:\n"
            "{\n"
            '  "habits": [],\n'
            '  "weekly_plan": {},\n'
            '  "recommendations": []\n'
            "}"
        )

        improvements_applied = [
            "Rol claro para orientar el comportamiento del asistente.",
            "Contexto conectado con el objetivo del usuario.",
            "Instrucciones específicas y numeradas.",
            "Formato de salida JSON definido.",
            "Restricciones para evitar respuestas vagas o poco realistas.",
        ]

        explanation = (
            "El prompt mejorado reduce ambigüedad porque indica quién responde, "
            "qué debe lograr, cómo debe organizar la respuesta y qué formato debe devolver."
        )

        # Keep the internal template visible in the service for future LLM integration.
        _ = prompt_used

        return build_improve_prompt_response(
            improved_prompt=improved_prompt,
            improvements_applied=improvements_applied,
            explanation=explanation,
        )

    def _build_prompt(self, payload: ImprovePromptRequest) -> str:
        template = self.prompt_template_path.read_text(encoding="utf-8")
        return template.format(
            original_prompt=payload.original_prompt,
            objective=payload.objective,
        )

