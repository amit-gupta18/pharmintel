from fastapi import APIRouter
from app.schemas.request_schemas import QueryRequest
from app.core.agent_manager import master_agent

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/ask")
async def ask_agent(request: QueryRequest):
    result = await master_agent.run(request.query)
    return result
