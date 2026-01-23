from fastapi import FastAPI
from app.routes.upload import router as upload_router
from dotenv import load_dotenv
from app.routes.summary import router as summary_router
from app.routes.insights import router as insights_router

load_dotenv()

app = FastAPI(
    title="SME Financial Intelligence Copilot",
    version="0.1.0"
)

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(insights_router)