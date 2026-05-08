# Habit Coach API

## Descripción

Habit Coach API es una API REST desarrollada con Python y FastAPI para generar, evaluar y mejorar planes de hábitos personalizados usando principios de prompt engineering.

El proyecto trabaja con respuestas simuladas. No usa base de datos, interfaz gráfica, autenticación ni conexión real con servicios externos de inteligencia artificial.

## Objetivo académico

El objetivo del proyecto es demostrar buenas prácticas de desarrollo backend en una API sencilla, modular y evaluable. La aplicación evidencia uso de FastAPI, modelos Pydantic, validaciones, manejo de errores, pruebas automatizadas y prompts estructurados.

## Tecnologías usadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX

## Estructura del proyecto

```text
app/
  controllers/
  models/
  prompts/
  routes/
  services/
  views/
  errors.py
  exceptions.py
  main.py
tests/
  test_main.py
COMMITS.md
PROMPTING.md
README.md
requirements.txt
```

La arquitectura sigue una versión simple de MVC adaptada a una API REST:

- `models/`: contratos de entrada y salida usando Pydantic.
- `views/`: funciones para construir respuestas.
- `controllers/`: coordinación entre rutas y servicios.
- `services/`: lógica de negocio y simulación de respuestas.
- `routes/`: endpoints HTTP.
- `prompts/`: plantillas de prompts reutilizables.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

Documentación automática:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints disponibles

| Método | Endpoint | Descripción |
| --- | --- | --- |
| GET | `/` | Información general de la API |
| GET | `/health` | Verifica que la API esté activa |
| POST | `/generate-plan` | Genera un plan semanal de hábitos |
| POST | `/evaluate-progress` | Evalúa progreso del usuario |
| POST | `/improve-prompt` | Mejora un prompt básico |
| GET | `/prompt-examples` | Lista ejemplos de prompts usados |

## Ejemplos curl

### Información general

```bash
curl http://127.0.0.1:8000/
```

### Health check

```bash
curl http://127.0.0.1:8000/health
```

### Generar plan de hábitos

```bash
curl -X POST http://127.0.0.1:8000/generate-plan \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "quiero mejorar mi condición física",
    "level": "principiante",
    "available_time": "20 minutos diarios"
  }'
```

Valores válidos para `level`: `principiante`, `intermedio`, `avanzado`.

### Evaluar progreso

```bash
curl -X POST http://127.0.0.1:8000/evaluate-progress \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "mejorar mi condición física",
    "completed_habits": ["caminar 20 minutos", "tomar agua"],
    "missed_habits": ["dormir 7 horas"],
    "notes": "me costó organizar mi tiempo"
  }'
```

### Mejorar prompt

```bash
curl -X POST http://127.0.0.1:8000/improve-prompt \
  -H "Content-Type: application/json" \
  -d '{
    "original_prompt": "Actúa como coach y dame hábitos",
    "objective": "obtener una respuesta más estructurada y en formato JSON"
  }'
```

### Ver ejemplos de prompts

```bash
curl http://127.0.0.1:8000/prompt-examples
```

## Estrategia de prompting

La API usa prompts dinámicos construidos desde plantillas guardadas en `app/prompts/`. Cada prompt combina rol, contexto del usuario, instrucciones específicas, formato esperado y restricciones.

- Roles: se define quién debe actuar, por ejemplo un coach de hábitos responsable.
- Contexto: se agregan datos como objetivo, nivel, tiempo disponible, hábitos completados y notas.
- Formato JSON: se solicita una salida estructurada para que la respuesta sea fácil de consumir.
- Mejora iterativa: `/improve-prompt` convierte un prompt básico en uno más claro, específico y útil.
- Respuestas contextuales: los servicios detectan el tipo de objetivo y adaptan hábitos, plan semanal, feedback y recomendaciones.

## Personalización contextual

La API mantiene respuestas simuladas, pero ahora analiza el objetivo del usuario para ajustar el contenido. Puede reconocer contextos como actividad física, alimentación, estudio, sueño, productividad, bienestar, lectura y finanzas personales.

Ejemplos:

- Si el objetivo es `quiero aprender ingles`, la respuesta prioriza estudio, sesiones cortas y registro de aprendizaje.
- Si el objetivo es `quiero dormir mejor`, la respuesta prioriza rutina nocturna, descanso y seguimiento del sueño.
- Si el objetivo es `quiero ahorrar dinero`, la evaluación de progreso usa lenguaje relacionado con gastos y presupuesto.

Si no se detecta una categoría clara, la API usa una respuesta genérica pero sigue incorporando el objetivo, nivel y tiempo disponible del usuario.

Más detalle en `PROMPTING.md`.

## Ejemplos de prompts usados

La aplicación incluye plantillas para:

- Generar planes de hábitos: `app/prompts/habit_plan_prompt.txt`
- Evaluar progreso: `app/prompts/evaluate_progress_prompt.txt`
- Mejorar prompts: `app/prompts/improve_prompt_template.txt`

También pueden consultarse desde:

```bash
curl http://127.0.0.1:8000/prompt-examples
```

## Estrategia de commits

El proyecto busca commits pequeños, descriptivos y agrupados por intención: estructura inicial, endpoints, modelos, servicios, prompts, validaciones, pruebas y documentación.

Más detalle en `COMMITS.md`.

## Cómo correr pruebas

```bash
pytest
```

Resultado esperado:

```text
6 passed
```

## Posibles mejoras futuras

- Conectar con una API real de IA.
- Agregar base de datos.
- Guardar historial de planes.
- Agregar autenticación.
- Agregar métricas de progreso.
- Desplegar la API en Render, Railway o Fly.io.

## Conclusión

Habit Coach API queda preparada como una entrega universitaria clara y funcional. El proyecto demuestra organización modular, endpoints REST, validaciones, manejo de errores, pruebas básicas y uso consciente de prompting sin añadir complejidad innecesaria.
