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

## Sugerencias de commits

1. `chore: create fastapi project structure`
2. `feat: add health check endpoint`
3. `feat: add habit plan generation endpoint`
4. `docs: add api usage instructions`

