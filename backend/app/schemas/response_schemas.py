from pydantic import BaseModel
from typing import Any, Dict, Optional

class AgentResponse(BaseModel):
    response: str
    data: Optional[Dict[str, Any]] = None
