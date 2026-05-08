from typing import TypedDict


class GoalContext(TypedDict):
    category: str
    focus: str
    action: str
    metric: str
    starter_habit: str
    support_habit: str
    reflection_habit: str


CONTEXTS: dict[str, GoalContext] = {
    "fitness": {
        "category": "fitness",
        "focus": "condicion fisica",
        "action": "hacer una sesion de movimiento",
        "metric": "minutos activos",
        "starter_habit": "Realizar una caminata ligera o movilidad articular.",
        "support_habit": "Preparar ropa comoda y agua antes de iniciar.",
        "reflection_habit": "Registrar energia, esfuerzo y recuperacion.",
    },
    "nutrition": {
        "category": "nutrition",
        "focus": "alimentacion",
        "action": "preparar una comida o decision saludable",
        "metric": "comidas planificadas",
        "starter_habit": "Agregar una porcion de fruta o verdura a una comida.",
        "support_habit": "Planear una opcion saludable antes de tener hambre.",
        "reflection_habit": "Registrar que comida ayudo a sentir mas energia.",
    },
    "study": {
        "category": "study",
        "focus": "aprendizaje",
        "action": "hacer una sesion de estudio enfocada",
        "metric": "minutos de estudio",
        "starter_habit": "Estudiar un tema pequeno con una meta concreta.",
        "support_habit": "Eliminar distracciones antes de empezar.",
        "reflection_habit": "Anotar una idea aprendida y una duda pendiente.",
    },
    "sleep": {
        "category": "sleep",
        "focus": "descanso",
        "action": "seguir una rutina de descanso",
        "metric": "horas de sueno y calidad",
        "starter_habit": "Apagar pantallas unos minutos antes de dormir.",
        "support_habit": "Preparar una rutina nocturna sencilla y repetible.",
        "reflection_habit": "Registrar hora de dormir y energia al despertar.",
    },
    "productivity": {
        "category": "productivity",
        "focus": "productividad",
        "action": "completar una tarea prioritaria",
        "metric": "tareas terminadas",
        "starter_habit": "Elegir una tarea importante y trabajarla sin interrupciones.",
        "support_habit": "Ordenar el espacio antes de iniciar.",
        "reflection_habit": "Revisar que bloqueo aparecio y como reducirlo.",
    },
    "wellbeing": {
        "category": "wellbeing",
        "focus": "bienestar",
        "action": "hacer una practica breve de autocuidado",
        "metric": "estado de animo y constancia",
        "starter_habit": "Practicar respiracion o pausa consciente.",
        "support_habit": "Reservar un momento tranquilo del dia.",
        "reflection_habit": "Registrar emociones y nivel de tension.",
    },
    "reading": {
        "category": "reading",
        "focus": "lectura",
        "action": "leer con atencion",
        "metric": "paginas o minutos leidos",
        "starter_habit": "Leer unas paginas con una meta pequena.",
        "support_habit": "Dejar el libro visible y listo.",
        "reflection_habit": "Escribir una frase o idea clave.",
    },
    "finance": {
        "category": "finance",
        "focus": "finanzas personales",
        "action": "revisar una decision financiera",
        "metric": "gastos registrados",
        "starter_habit": "Registrar un gasto o ingreso del dia.",
        "support_habit": "Revisar una compra antes de hacerla.",
        "reflection_habit": "Identificar un gasto que se puede ajustar.",
    },
    "generic": {
        "category": "generic",
        "focus": "objetivo personal",
        "action": "hacer una accion pequena relacionada con el objetivo",
        "metric": "acciones completadas",
        "starter_habit": "Realizar una accion pequena y medible.",
        "support_habit": "Preparar el entorno para que el habito sea facil.",
        "reflection_habit": "Registrar avance, obstaculos y siguiente paso.",
    },
}


KEYWORDS: dict[str, tuple[str, ...]] = {
    "fitness": ("ejercicio", "fisica", "fitness", "caminar", "correr", "entrenar", "fuerza"),
    "nutrition": ("alimentacion", "comer", "comida", "agua", "nutricion", "dieta"),
    "study": ("estudiar", "aprender", "ingles", "idioma", "universidad", "curso", "leer mejor"),
    "sleep": ("dormir", "sueno", "descansar", "descanso", "noche"),
    "productivity": ("productividad", "organizar", "tiempo", "trabajo", "tareas", "procrastinar"),
    "wellbeing": ("estres", "ansiedad", "mental", "bienestar", "meditar", "emocion"),
    "reading": ("lectura", "leer", "libro", "paginas"),
    "finance": ("dinero", "ahorrar", "finanzas", "gastos", "presupuesto"),
}


LEVEL_GUIDANCE = {
    "principiante": "Mantener pasos simples, cortos y faciles de repetir.",
    "intermedio": "Aumentar consistencia y agregar seguimiento semanal.",
    "avanzado": "Trabajar con metas mas retadoras y medicion detallada.",
}


def analyze_goal(goal: str) -> GoalContext:
    """Infer a practical context from the user's goal."""
    normalized_goal = goal.lower()
    for category, keywords in KEYWORDS.items():
        if any(keyword in normalized_goal for keyword in keywords):
            return CONTEXTS[category]
    return CONTEXTS["generic"]


def get_level_guidance(level: str) -> str:
    """Return guidance text based on the user's experience level."""
    return LEVEL_GUIDANCE.get(level, LEVEL_GUIDANCE["principiante"])

