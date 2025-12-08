from typing import TypedDict, Annotated, List, Dict, Any

class AgentState(TypedDict):
    query: str
    results: Dict[str, Any]
    steps: List[str]
