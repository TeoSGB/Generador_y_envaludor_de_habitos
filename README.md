# Habit Coach API

Habit Coach API es una API REST construida con Python y FastAPI para generar, evaluar y mejorar planes de hábitos personalizados usando principios de prompt engineering.

La aplicación no usa base de datos ni conexión real con APIs externas de IA. Las respuestas son simuladas, pero están organizadas como si en una siguiente fase se conectara un modelo de lenguaje.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

Documentación automática:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Ejecutar pruebas

```bash
pytest
```

## Arquitectura

El proyecto usa una versión simple de MVC adaptada a una API REST:

- `models/`: modelos Pydantic para validar entradas y estructurar respuestas.
- `views/`: funciones que construyen las respuestas de la API.
- `controllers/`: coordinan las peticiones entre rutas, servicios y vistas.
- `services/`: contienen la lógica de negocio y generación de prompts.
- `routes/`: exponen los endpoints de FastAPI.
- `prompts/`: guarda plantillas reutilizables para prompting.
- `tests/`: contiene pruebas básicas con pytest.

## Endpoints

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

Valores válidos para `level`:

- `principiante`
- `intermedio`
- `avanzado`

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

## Validaciones y errores

La API usa Pydantic para validar datos antes de ejecutar la lógica de negocio:

- `goal`, `available_time`, `objective` y otros textos no pueden estar vacíos.
- `level` solo acepta `principiante`, `intermedio` o `avanzado`.
- `original_prompt` debe tener mínimo 10 caracteres.
- `completed_habits` debe ser una lista con al menos un elemento.
- Las listas de hábitos no deben contener textos vacíos.

Las respuestas de error tienen una estructura clara:

```json
{
  "error": "Validation error",
  "message": "Please review the request data and try again.",
  "details": []
}
```

Para simular errores internos durante pruebas manuales se puede enviar `simulate_error` dentro de algunos campos de texto.

## Prompting Strategy

La aplicación usa prompts como plantillas separadas dentro de `app/prompts/`. Cada endpoint construye un prompt dinámico con los datos recibidos y luego simula una respuesta coherente.

- Roles: los prompts indican un rol claro, por ejemplo coach de hábitos o asistente especializado en evaluación de progreso.
- Contexto del usuario: se agregan datos como objetivo, nivel, tiempo disponible, hábitos completados, hábitos pendientes y notas personales.
- Formato JSON: los prompts piden una estructura de salida concreta para facilitar respuestas consistentes y fáciles de consumir por una API.
- Mejora iterativa: `/improve-prompt` transforma un prompt básico en uno más específico al agregar rol, contexto, instrucciones, formato esperado y restricciones.

## Estrategia de commits

La idea del proyecto es mantener commits pequeños, descriptivos y fáciles de revisar.

Secuencia sugerida para esta tercera fase:

1. `feat: add root api information endpoint`
2. `refactor: improve request validations`
3. `feat: add error handling responses`
4. `test: add pytest coverage for api endpoints`
5. `docs: update readme with testing instructions`

