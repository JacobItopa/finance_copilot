from fastapi import FastAPI
from app.routes.upload import router as upload_router
from dotenv import load_dotenv
from app.routes.summary import router as summary_router
from app.routes.insights import router as insights_router
from app.routes.recommendations import router as recommendations_router
from app.routes.digest import router as digest_router
from app.routes.email_digest import router as email_digest_router

load_dotenv()

app = FastAPI(
    title="SME Financial Intelligence Copilot",
    version="0.1.0"
)

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(insights_router)
app.include_router(recommendations_router)
app.include_router(digest_router)
app.include_router(email_digest_router)