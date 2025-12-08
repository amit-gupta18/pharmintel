from pydantic import BaseModel

class AgentTask(BaseModel):
    task_id: str
    description: str
    assigned_agent: str
