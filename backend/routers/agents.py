from fastapi import APIRouter
from pydantic import BaseModel
from agents.master_agent import master_agent

router = APIRouter(prefix="/agents", tags=["agents"])

class QueryRequest(BaseModel):
    query: str

@router.post("/run")
def run_agent(request: QueryRequest):
    result = master_agent.run(request.query)
    return result
