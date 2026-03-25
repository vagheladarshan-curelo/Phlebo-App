from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import router as api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Phlebo-App API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
