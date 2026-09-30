from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import router


app = FastAPI(
    title="FitBuddy - AI Fitness Plan Generator",
    description="AI-powered personalized fitness plan generator using Gemini",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Application routes
app.include_router(router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "FitBuddy API is running"
    }