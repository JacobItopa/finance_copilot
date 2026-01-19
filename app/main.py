from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(
    title="SME Financial Intelligence Copilot",
    version="0.1.0"
)

app.include_router(upload_router)
