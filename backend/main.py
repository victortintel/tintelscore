from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="TintelScore API",
    description="API de diagnóstico de crédito preditivo",
    version="1.0.0"
)

app.include_router(router)