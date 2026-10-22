from fastapi import FastAPI
from app.routers import health, assets

app = FastAPI(title="Inventory Service")

# @app.get("/health")
# def health():
#     return {"status": "ok"}

app.include_router(health.router)
app.include_router(assets.router)