# Habit Coach API

API REST construida con Python y FastAPI para generar planes de hábitos personalizados usando prompts estructurados.

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

La documentación automática estará disponible en:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Arquitectura

El proyecto usa una versión simple de MVC adaptada a una API REST:

- `models/`: modelos Pydantic para validar entradas y estructurar respuestas.
- `views/`: funciones que construyen las respuestas de la API.
- `controllers/`: coordinan las peticiones entre rutas, servicios y vistas.
- `services/`: contienen la lógica de negocio y generación de prompts.
- `routes/`: exponen los endpoints de FastAPI.
- `prompts/`: guarda plantillas reutilizables para prompting.

## Endpoints

### Health check

```bash
curl http://127.0.0.1:8000/health
```

Respuesta esperada:

```json
{
  "status": "ok",
  "message": "Habit Coach API running"
}
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

## Prompting Strategy

La aplicación usa prompts como plantillas separadas dentro de `app/prompts/`. Cada endpoint construye un prompt dinámico con los datos recibidos y luego simula una respuesta coherente, sin conectarse todavía a una API externa de IA.

- Roles: los prompts indican un rol claro, por ejemplo coach de hábitos o asistente especializado en evaluación de progreso.
- Contexto del usuario: se agregan datos como objetivo, nivel, tiempo disponible, hábitos completados, hábitos pendientes y notas personales.
- Formato JSON: los prompts piden una estructura de salida concreta para facilitar respuestas consistentes y fáciles de consumir por una API.
- Mejora iterativa: `/improve-prompt` transforma un prompt básico en uno más específico al agregar rol, contexto, instrucciones, formato esperado y restricciones.

## Sugerencias de commits para la segunda fase

1. `feat: add progress evaluation models`
2. `feat: add progress evaluation endpoint`
3. `feat: add prompt improvement service`
4. `feat: add prompt examples endpoint`
5. `docs: update readme with prompting strategy`

