from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.plan import router as plan_router
from app.routes.progress import router as progress_router
from app.routes.prompts import router as prompts_router


app = FastAPI(
    title="Habit Coach API",
    description="API REST para generar planes de hábitos personalizados usando prompts estructurados.",
    version="0.1.0",
)

# Routers separados para mantener la aplicación preparada para crecer.
app.include_router(health_router)
app.include_router(plan_router)
app.include_router(progress_router)
app.include_router(prompts_router)
