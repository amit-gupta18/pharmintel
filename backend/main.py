from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from agents import run_agents

from agents.master_agent import master_agent
from routers import agents

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents.router)

@app.get("/")
def home():
    return {"message": "PharmaIntel Backend running ✅"}


