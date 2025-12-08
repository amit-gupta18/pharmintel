from fastapi import FastAPI
from app.routes import chat, reports, upload
from app.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PharmaIntel Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router)
app.include_router(reports.router)
app.include_router(upload.router)

@app.get("/")
async def root():
    return {"message": "PharmaIntel Backend running", "env": settings.ENVIRONMENT}
