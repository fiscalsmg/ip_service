from fastapi import FastAPI

from app.entrypoint import tasks_router

app: FastAPI = FastAPI(
    title="Servicio de geolocalización",
    description="Ejercicio 2",
    docs_url="/docs",
)

app.include_router(tasks_router)
